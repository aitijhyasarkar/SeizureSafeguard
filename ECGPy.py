import serial
import time
import numpy as np
import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import find_peaks

# Serial port configuration
SERIAL_PORT = '/dev/cu.usbmodem101'
BAUD_RATE = 115200

# ThingsBoard configuration
THINGSBOARD_SERVER = "thingsboard.cloud"
ACCESS_TOKEN = "1b0h822630kzcoygsqsw"

# MQTT client setup
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard
client.connect(THINGSBOARD_SERVER, 1883, 60)

PEAK_DISTANCE = 50  # Minimum distance between peaks (in samples)
PEAK_HEIGHT = 50  # Minimum peak height

# BPM averaging window (in seconds)
BPM_WINDOW = 10

# Function to get peaks from the ECG signal
def get_peak(ecg_signal):
    peaks, _ = find_peaks(ecg_signal, distance=PEAK_DISTANCE, height=PEAK_HEIGHT)
    return peaks

# Function to calculate BPM from the detected peaks
def calculate_bpm(peaks, sample_rate):
    if len(peaks) < 2:
        return 0 # Return 0 if there are fewer than 2 peaks

    intervals = np.diff(peaks) / sample_rate
    avg_interval = np.mean(intervals)
    bpm = 60 / avg_interval
    return bpm

#Driver function
def main():
    ecg_signal = []
    bpm_values = []  # Initialize the bpm_values list here
    sample_rate = 125
    last_update_time = time.time()
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)
    fig, ax = plt.subplots(figsize=(12, 6))
    line, = ax.plot([], [], lw=2)

    # Function to initialize the plot
    def init():
        ax.set_xlim(0, 5)
        ax.set_ylim(-200, 200)
        return line,

    # Function to update the plot with new data
    def update(frame):
        nonlocal bpm_values
        nonlocal last_update_time
        if ser.in_waiting:
            data_line = ser.readline().decode('utf-8').strip() # Read a line from the serial buffer
            try:
                signal = float(data_line)
                ecg_signal.append(signal)
                if len(ecg_signal) > sample_rate * 5:
                    ecg_signal.pop(0)
                peaks = get_peak(ecg_signal)
                bpm = calculate_bpm(peaks, sample_rate)
                bpm_values.append(bpm)

                # Calculate average BPM over the specified window
                window_size = int(BPM_WINDOW * sample_rate)
                if len(bpm_values) > window_size:
                    bpm_values = bpm_values[-window_size:]
                avg_bpm = np.mean(bpm_values)
                current_time = time.time()
                if current_time - last_update_time >= 2:
                    print(f"Average BPM (last {BPM_WINDOW} seconds): {avg_bpm:.2f}")
                    payload = {"BPM": avg_bpm}
                    client.publish('v1/devices/me/telemetry', json.dumps(payload))
                    print(f"Publishing message: {payload}")
                    last_update_time = current_time
                xdata = np.linspace(max(0, len(ecg_signal) / sample_rate - 5), len(ecg_signal) / sample_rate, len(ecg_signal))
                ydata = ecg_signal[-len(xdata):]
                line.set_data(xdata, ydata)
                ax.set_xlim(xdata[0], xdata[-1])  # Adjust x-axis limits for zooming

            # Handle any ValueError that may occur during data conversion
            except ValueError:
                pass

        return line,
    ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=1000 // (sample_rate * 2))
    plt.show() # Show the plot
    ser.close() # Close the serial port
    client.disconnect() # Disconnect from ThingsBoard
if __name__ == "__main__":
    main()