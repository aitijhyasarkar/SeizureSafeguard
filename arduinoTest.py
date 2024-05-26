import threading
import serial
import time
import numpy as np
import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import find_peaks
from scipy.fftpack import fft
# import pickle

# Serial port configuration
EEG_SERIAL_PORT = '/dev/cu.usbserial-0001'  # Update as necessary
ECG_SERIAL_PORT = '/dev/cu.usbmodem101'  # Update as necessary
BAUD_RATE = 115200

# ThingsBoard configuration
THINGSBOARD_SERVER = "thingsboard.cloud"
ACCESS_TOKEN = "1b0h822630kzcoygsqsw"

# # Load the trained seizure detection model
# with open('ML Algos/seizure_model.pkl', 'rb') as model_file:
#     seizure_model = pickle.load(model_file)

# MQTT client setup
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_SERVER, 1883, 60)

# Sample rates
EEG_SAMPLE_RATE = 125
ECG_SAMPLE_RATE = 60

# Buffer sizes
EEG_BUFFER_SIZE = 256
ECG_BUFFER_SIZE = 300  # 5 seconds buffer at 60Hz

# Initialize buffers
eeg_signal = []
ecg_signal = []
bpm_values = []

# Initialize time for BPM update
last_update_time = time.time()

lock = threading.Lock()

# Function to calculate FFT of the EEG signal
def calculate_fft(eeg_signal, sample_rate):
    fft_result = fft(eeg_signal)
    freqs = np.fft.fftfreq(len(fft_result), 1 / sample_rate)
    return freqs, np.abs(fft_result)

# Function to get peaks from the ECG signal
def get_peak(ecg_signal):
    peaks, _ = find_peaks(ecg_signal, distance=50, height=50)
    return peaks

# Function to calculate BPM from the detected peaks
def calculate_bpm(peaks):
    sample_rate=125
    if len(peaks) < 2:
        return 0
    intervals = np.diff(peaks) / sample_rate
    avg_interval = np.mean(intervals)
    bpm = 60 / avg_interval
    return bpm

# # Function to process the EEG signal and detect seizures
# def process_eeg_signal(eeg_signal):
#     # Extract features from the EEG signal
#     freqs, fft_result = calculate_fft(eeg_signal, EEG_SAMPLE_RATE)
#     features = np.array(fft_result[:EEG_BUFFER_SIZE // 2])

#     # Ensure the feature vector matches the model's expected input size
#     if len(features) < 129:
#         features = np.append(features, [0] * (129 - len(features)))
#     elif len(features) > 129:
#         features = features[:129]
#     features = features.reshape(1, -1)
#     seizure_prediction = seizure_model.predict(features)
#     return seizure_prediction

# Function to read EEG data
def read_eeg_data():
    global eeg_signal
    ser_eeg = serial.Serial(EEG_SERIAL_PORT, BAUD_RATE)
    time.sleep(2)
    while True:
        if ser_eeg.in_waiting:
            data_line = ser_eeg.readline().decode('utf-8').strip()  # Read a line from the serial buffer
            try:
                signal = float(data_line)
                with lock:
                    eeg_signal.append(signal)
                    if len(eeg_signal) > EEG_BUFFER_SIZE:
                        eeg_signal.pop(0)
            except ValueError:
                pass

# Function to read ECG data
def read_ecg_data():
    global ecg_signal, bpm_values, last_update_time
    ser_ecg = serial.Serial(ECG_SERIAL_PORT, BAUD_RATE)
    time.sleep(2)
    while True:
        if ser_ecg.in_waiting:
            data_line = ser_ecg.readline().decode('utf-8').strip()  # Read a line from the serial buffer
            try:
                signal = float(data_line)
                with lock:
                    ecg_signal.append(signal)
                    if len(ecg_signal) > ECG_BUFFER_SIZE:
                        ecg_signal.pop(0)

                    # Calculate BPM
                    peaks = get_peak(ecg_signal)
                    bpm = calculate_bpm(peaks)
                    bpm_values.append(bpm)

                    # Calculate average BPM over the specified window
                    window_size = int(10 * ECG_SAMPLE_RATE)
                    if len(bpm_values) > window_size:
                        bpm_values = bpm_values[-window_size:]
                    avg_bpm = np.mean(bpm_values)
                    current_time = time.time()
                    if current_time - last_update_time >= 2:
                        print(f"BPM: {avg_bpm:.2f}")
                        client.publish('v1/devices/me/telemetry', json.dumps({"BPM": avg_bpm}))
                        last_update_time = current_time
            except ValueError:
                pass

# Initialize plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
line3, = ax3.plot([], [], lw=2)

# Set titles and labels for plots
ax1.set_title('EEG Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax2.set_title('FFT of EEG Signal')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude')
ax3.set_title('ECG Signal')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Amplitude')
ax1.yaxis.set_tick_params(labelleft=False)
ax2.yaxis.set_tick_params(labelleft=False)
ax3.yaxis.set_tick_params(labelleft=False)
ax1.set_yticks([])
ax2.set_yticks([])
ax3.set_yticks([])

# Function to initialize the plot
def init():
    ax1.set_xlim(0, EEG_BUFFER_SIZE / EEG_SAMPLE_RATE)
    ax2.set_xlim(0, EEG_SAMPLE_RATE / 2)
    ax3.set_xlim(0, 5)
    return line1, line2, line3

# Function to update the plot with new data
def update(frame):
    global eeg_signal, ecg_signal
    with lock:
        if len(eeg_signal) == EEG_BUFFER_SIZE:

            # Update the time-domain plot for EEG
            x_data_eeg = np.linspace(0, EEG_BUFFER_SIZE / EEG_SAMPLE_RATE, EEG_BUFFER_SIZE)
            line1.set_data(x_data_eeg, eeg_signal)
            ax1.set_ylim(min(eeg_signal), max(eeg_signal))  # Dynamic y-axis for EEG

            # Calculate and update the FFT plot for EEG
            freqs, fft_result = calculate_fft(eeg_signal, EEG_SAMPLE_RATE)
            line2.set_data(freqs[:EEG_BUFFER_SIZE // 2], fft_result[:EEG_BUFFER_SIZE // 2])
            ax2.set_ylim(0, max(fft_result))  # Dynamic y-axis for FFT

            # # Detect seizure using the model
            # seizure_prediction = process_eeg_signal(eeg_signal)
            # if seizure_prediction == 1:
            #     print("Seizure detected!")
            #     client.publish('v1/devices/me/telemetry', json.dumps({"seizure": True}))
            # else:
            #     client.publish('v1/devices/me/telemetry', json.dumps({"seizure": False}))

        if len(ecg_signal) >= ECG_BUFFER_SIZE:

            # Update the time-domain plot for ECG
            x_data_ecg = np.linspace(0, len(ecg_signal) / ECG_SAMPLE_RATE, len(ecg_signal))
            line3.set_data(x_data_ecg, ecg_signal)
            ax3.set_ylim(min(ecg_signal), max(ecg_signal))  # Dynamic y-axis for ECG
    return line1, line2, line3

# Initialize animation
ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=1000 // EEG_SAMPLE_RATE)
plt.tight_layout()

# Start the threads for reading data
eeg_thread = threading.Thread(target=read_eeg_data)
ecg_thread = threading.Thread(target=read_ecg_data)
eeg_thread.start()
ecg_thread.start()

plt.show()

# Close serial ports and disconnect MQTT client
eeg_thread.join()
ecg_thread.join()
client.disconnect()