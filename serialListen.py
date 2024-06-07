import serial; import pyautogui
from serial import SerialException
from collections import namedtuple
import subprocess

init = serial.Serial(port="COM6", baudrate=9600)

Coordinates = namedtuple("Coordinates", ['x', 'y'])


def control(data):
    command = ''
    for i in range(len(data)):
        command += data[i]

    if command == "EC13FE01":
        print("OK BUTTON PRESSED")
        pyautogui.click()
    elif command == "E916FE01":
        print("UP BUTTON PRESSED")
        cords = Coordinates(0, -100)
        move(cords)
    elif command == "AF50FE01":
        print("RIGHT BUTTON PRESSED")
        cords = Coordinates(100, 0)
        move(cords)
    elif command == "E51AFE01":
        print("BOTTOM BUTTON PRESSED")
        cords = Coordinates(0, 100)
        move(cords)
    elif command == "AE51FE01":
        print("LEFT BUTTON PRESSED")
        cords = Coordinates(-100, 0)
        move(cords)
    elif command == "E619FE01":
        print("RETURN BUTTON PRESSED")
        pyautogui.hotkey("alt", "left")
    elif command == "CF3FE01":
        print("VOLUME DOWN BUTTON PRESSED")
        subprocess.run(["amixer", "set", "Master", "20%-"])
    elif command == "DF2FE01":
        print("VOLUME UP BUTTON PRESSED")
        subprocess.run(["amixer", "set", "Master", "20%+"])
    elif command == "BC43FE01":
        print("FULLSCREEN BUTTON PRESSED")
        pyautogui.press("F")
    elif command == "E718FE01":
        print("SCROLL UP BUTTON PRESSED")
        pyautogui.scroll(200)
    elif command == "EF10FE01":
        print("SCROLL DOWN BUTTON PRESSED")
        pyautogui.scroll(-200)


def move(cords):
    try:
        pyautogui.move(cords.x, cords.y)
    except pyautogui.FailSafeException as e:
        print("Fuck!", e)
        pyautogui.moveTo(pyautogui.size().width // 2, pyautogui.size().height // 2)


def listen():
    try:
        struct = list()
        while True:
            data = init.read()
            if data == b'\r' or data == b'\n':
                return struct
            struct.append(str(data, "utf-8"))
    except SerialException as e:
        print("Exception occurred!", e)


