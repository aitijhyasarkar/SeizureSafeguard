#include <math.h>
#define SAMPLE_RATE 75
#define BAUD_RATE 115200
#define INPUT_PIN A2
#define OUTPUT_PIN 13
#define DATA_LENGTH 6
int data_index = 0;
bool peak = false;
void setup() {
  Serial.begin(BAUD_RATE);
  pinMode(INPUT_PIN, INPUT);
  pinMode(OUTPUT_PIN, OUTPUT);
}
void loop() {

  // Calculate elapsed time
  static unsigned long past = 0;
  unsigned long present = micros();
  unsigned long interval = present - past;
  past = present;

  // Run timer
  static long timer = 0;
  timer -= interval;

  // Sample
  if (timer < 0) {
    timer += 1000000 / SAMPLE_RATE;
    float sensor_value = analogRead(INPUT_PIN);
    float signal = EOGFilter(sensor_value) / 512;
    // Serial.println(signal);
    peak = Getpeak(signal);
    digitalWrite(OUTPUT_PIN, peak);
    if (peak) Serial.println(1);
    else Serial.println(0);
  }
}
bool Getpeak(float new_sample) {

  // Buffers for data, mean, and standard deviation
  static float data_buffer[DATA_LENGTH], mean_buffer[DATA_LENGTH], standard_deviation_buffer[DATA_LENGTH];

  // Check for peak
  if (new_sample - mean_buffer[data_index] > (DATA_LENGTH * 1.2) * standard_deviation_buffer[data_index]) {
    data_buffer[data_index] = new_sample + data_buffer[data_index];
    peak = true;
  } else {
    data_buffer[data_index] = new_sample;
    peak = false;
  }

  // Calculate mean
  float sum = 0.0, mean, standard_deviation = 0.0;
  for (int i = 0; i < DATA_LENGTH; ++i) sum += data_buffer[(data_index + i) % DATA_LENGTH]
  mean = sum / DATA_LENGTH;

  // Calculate standard deviation
  for (int i = 0; i < DATA_LENGTH; ++i) standard_deviation += pow(data_buffer[(i) % DATA_LENGTH] - mean, 2);

  // Update mean buffer
  mean_buffer[data_index] = mean;

  // Update standard deviation buffer
  standard_deviation_buffer[data_index] = sqrt(standard_deviation / DATA_LENGTH);

  // Update data_index
  data_index = (data_index + 1) % DATA_LENGTH;

  // Return peak
  return peak;
}

float EOGFilter(float input) {
  float output = input;
  {
    static float z1, z2;  // filter section state
    float x = output - 0.02977423 * z1 - 0.04296318 * z2;
    output = 0.09797471 * x + 0.19594942 * z1 + 0.09797471 * z2;
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2;  // filter section state
    float x = output - 0.08383952 * z1 - 0.46067709 * z2;
    output = 1.00000000 * x + 2.00000000 * z1 + 1.00000000 * z2;
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2;  // filter section state
    float x = output - -1.92167271 * z1 - 0.92347975 * z2;
    output = 1.00000000 * x + -2.00000000 * z1 + 1.00000000 * z2;
    z2 = z1;
    z1 = x;
  }
  {
    static float z1, z2;  // filter section state
    float x = output - -1.96758891 * z1 - 0.96933514 * z2;
    output = 1.00000000 * x + -2.00000000 * z1 + 1.00000000 * z2;
    z2 = z1;
    z1 = x;
  }
  return output;
}