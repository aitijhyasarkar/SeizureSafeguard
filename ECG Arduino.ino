#define SAMPLE_RATE 60 //Define the sampling rate for reading the ECG signal
#define BAUD_RATE  //Define the baud rate for serial communication
#define INPUT_PIN 4 //Define the input pin for the ECG signal

//Setup function to initialize pin modes and start serial communication
void setup() {
  pinMode(INPUT_PIN, INPUT); //Set the input pin mode for ECG signal
	Serial.begin(BAUD_RATE); //Start serial communication with the defined baud rate
}

//Driver Function
void loop() {
	static unsigned long past = 0;
	unsigned long present = micros(), interval = present - past;
	past = present;
	static long timer = 0;
	timer -= interval;
	if(timer < 0){
		timer += 1000000 / SAMPLE_RATE;
		float sensor_value = analogRead(INPUT_PIN), signal = ECGFilter(sensor_value);
		Serial.println(signal);
	}
}

//Function to filter the ECG signal using a 4th-order Butterworth band-pass filter
float ECGFilter(float input) {
  float output = input;
  {
    static float z1, z2; // filter section state
    float x = output - (0.53145496*z1) - (0.10706232*z2);
    output = (0.21617864*x) + (0.43235728*z1) + (0.21617864*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2; // filter section state
    float x = output - (0.75075465*z1) - (0.51109754*z2);
    output = (1.00000000*x) + (2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2; // filter section state
    float x = output - (-1.90310089*z1) - (0.90585346*z2);
    output = (1.00000000*x) + (-2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2;
    float x = output - (-1.95885465*z1) - (0.96156569*z2);
    output = (1.00000000*x) + (-2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  return output;
}