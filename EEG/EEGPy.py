import serial
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from scipy.fftpack import fft

# Serial port configuration
SERIAL_PORT = '/dev/cu.usbmodem101'  # Update this to your serial port
BAUD_RATE = 115200

SAMPLE_RATE = 125  # Sampling rate of the EEG data
BUFFER_SIZE = 256  # Buffer size for FFT (must be a power of 2)

# Function to calculate FFT of the EEG signal
def calculate_fft(eeg_signal, sample_rate):
    fft_result = fft(eeg_signal)
    freqs = np.fft.fftfreq(len(fft_result), 1 / sample_rate)
    return freqs, np.abs(fft_result)

# Driver function
def main():
    eeg_signal = []
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)

    # Initialize plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    line1, = ax1.plot([], [], lw=2)
    line2, = ax2.plot([], [], lw=2)

    # Set titles and labels for plots
    ax1.set_title('EEG Signal')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude')
    ax2.set_title('FFT of EEG Signal')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Amplitude')

    # Function to initialize the plot
    def init():
        ax1.set_xlim(0, BUFFER_SIZE / SAMPLE_RATE)
        ax2.set_xlim(0, SAMPLE_RATE / 2)
        return line1, line2

    # Function to update the plot with new data
    def update(frame):
        if ser.in_waiting:
            data_line = ser.readline().decode('utf-8').strip()  # Read a line from the serial buffer
            try:
                signal = float(data_line)
                eeg_signal.append(signal)
                if len(eeg_signal) > BUFFER_SIZE:
                    eeg_signal.pop(0)

                if len(eeg_signal) == BUFFER_SIZE:
                    # Update the time-domain plot
                    x_data = np.linspace(0, BUFFER_SIZE / SAMPLE_RATE, BUFFER_SIZE)
                    line1.set_data(x_data, eeg_signal)

                    # Calculate and update the FFT plot
                    freqs, fft_result = calculate_fft(eeg_signal, SAMPLE_RATE)
                    line2.set_data(freqs[:BUFFER_SIZE // 2], fft_result[:BUFFER_SIZE // 2])

                    # Adjust y-limits dynamically
                    min_amp = min(eeg_signal)
                    max_amp = max(eeg_signal)
                    ax1.set_ylim(min_amp, max_amp)

                    max_fft_amp = max(fft_result)
                    ax2.set_ylim(0, max_fft_amp)
            except ValueError:
                pass
        return line1, line2
    ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=1000 // SAMPLE_RATE)
    plt.tight_layout()
    plt.show()  # Show the plot
    ser.close()  # Close the serial port
if __name__ == "__main__":
    main()
