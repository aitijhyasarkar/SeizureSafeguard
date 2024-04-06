from serial import Serial
import time, pyautogui
def milis():
    return int(round(time.time() * 1000))
ser = Serial('COM7', 115200, timeout=1.00) # Arduino serial port interface
# Timing variable
timer = milis()
latency =  24
# Infinite loop
while True:
    try:
        data = ser.readline().decode('utf-8').strip() # Process serial data
        # Debounce
        # if((milis() - timer) > latency):
        #     timer = milis()
            # Virtual spacebar
        if(int(data)):
            pyautogui.press('space')  
            print("jump")
        ser.flushInput()
    except Exception as e:
        print(e, "\nBlink now...xcgdf")
        continue