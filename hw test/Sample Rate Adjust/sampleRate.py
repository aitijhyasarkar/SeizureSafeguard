import numpy as np
import scipy.signal

# Define the parameters
sample_rate = 60  # Hz
order = 4
lowcut = 0.5  # Hz
highcut = 20  # Hz

# Generate the filter coefficients
sos = scipy.signal.butter(order, [lowcut, highcut], btype='band', output='sos', fs=sample_rate)

# Print the filter coefficients
print(sos)