#when we will do real life testing, the data will go back to 0 as we given new data to read and analysis.


import time

high_heart_beat = 0
high_pressure = 0
fast_body_movement = 0
high_altitude_brain_wavelength = 0


def read_data_from_hardware():
    high_heart_beat = np.random.rand()
    high_pressure = np.random.rand()
    fast_body_movement = np.random.rand()
    high_altitude_brain_wavelength = np.random.rand()
    return [high_heart_beat, high_pressure, fast_body_movement, high_altitude_brain_wavelength]

while True:
    high_heart_beat = 0
    high_pressure = 0
    fast_body_movement = 0
    high_altitude_brain_wavelength = 0
    features = read_data_from_hardware()
    prediction = predict_seizure(features)
    print("Prediction:", prediction)
    time.sleep(300)  