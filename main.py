import serial
import numpy as np
import cv2

ser = serial.Serial(
    port="COM5",
    baudrate=115200, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1, 
)

print(f"Połączono z: {ser.name}")

try:
    while True:
        if ser.in_waiting >= 4: 
            data = ser.read(4) 
            x1 = data[0] #LSB pierwszej liczby
            x2 = data[1] #MSB pierwszej liczby
            y1 = data[2] #LSB drugiej liczby
            y2 = data[3] #MSB drugiej liczby
            
            x = x2 << 8 | x1
            y = y2 << 8 | y1
            
            
            cur_x = int(1000 - (x / 4095) * 1000)
            cur_y = int(1000 - (y / 4095) * 1000)
            
            img = np.zeros((1000, 1000, 3),np.uint8)
            
            cv2.circle(img, (cur_x, cur_y), 40, (200,60,30), -1)
            cv2.imshow("ss", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
except KeyboardInterrupt:
    print("Zamykanie połączenia...")
    ser.close()


cv2.destroyAllWindows()