import serial

PORT = '/dev/cu.usbmodem3377327732371'
BAUD = 115200
ser = None
try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    while True:
        line = ser.readline()
        if not line:
            print("no data, check firmware")
            continue
        try:
            string = line.decode('utf-8')
            clean_string = string.strip()
            clean_parts = clean_string.split(",")
            t = int(clean_parts[0])
            value = int(clean_parts[1])
            print(f"t: {t}, value: {value}")
        except (ValueError, IndexError):
            print("bad or partial line, nothing to worry about")
except serial.SerialException:
    print("board is unplugged, check board")
except KeyboardInterrupt:
    print("You stopped the program")
finally:
    if ser is not None:
        ser.close()

