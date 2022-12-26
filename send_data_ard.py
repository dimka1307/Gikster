import serial
import time

def main(servo_dvizhenja):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(str(servo_dvizhenja[0]).encode('utf-8'))
    #time.sleep(5)
    ser.write(str(servo_dvizhenja[1]).encode('utf-8'))
    #time.sleep(5)
    ser.write(str(servo_dvizhenja[2]).encode('utf-8'))
                
if __name__ == '__main__':
    main()