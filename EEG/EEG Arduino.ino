#define SAMPLE_RATE 125
#define BAUD_RATE 115200
#define INPUT_PIN A0

void setup() {
    Serial.begin(BAUD_RATE); // Start serial communication with the defined baud rate
}

void loop() {
    static unsigned long past = 0;
    unsigned long present = micros();
    unsigned long interval = present - past;
    past = present;

    static long timer = 0;
    timer -= interval;

    if (timer < 0) {
        timer += 1000000 / SAMPLE_RATE;
        float sensor_value = analogRead(INPUT_PIN);
        float signal = EEGFilter(sensor_value);
        Serial.println(signal);
    }
}

// Band-Pass Butterworth IIR digital filter
float EEGFilter(float input)
{
  float output = input;
  {
    static float z1, z2; // filter section state
    float x = output - (-0.11639771*z1) - (0.04483919*z2);
    output = (0.07432421*x) + (0.14864841*z1) + (0.07432421*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2; // filter section state
    float x = output - (-0.13361455*z1) - (0.45757204*z2);
    output = (1.00000000*x) + (2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2; // filter section state
    float x = output - (-1.95310104*z1) - (0.95374812*z2);
    output = (1.00000000*x) + (-2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2; // filter section state
    float x = output - (-1.98068998*z1) - (0.98132053*z2);
    output = (1.00000000*x) + (-2.00000000*z1) + (1.00000000*z2);
    z2 = z1;
    z1 = x;
  }
  return output;
}