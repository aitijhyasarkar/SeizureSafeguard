# in this code the module reads data every 5 minutes in loop when connected to the hardware

import time
import numpy as np 

def read_data_from_hardware():
    high_heart_beat = np.random.rand()
    high_pressure = np.random.rand()
    fast_body_movement = np.random.rand()
    high_altitude_brain_wavelength = np.random.rand()
    return [high_heart_beat, high_pressure, fast_body_movement, high_altitude_brain_wavelength]

while True:
    features = read_data_from_hardware()
    prediction = predict_seizure(features)
    print("Prediction:", prediction)

    time.sleep(300) 