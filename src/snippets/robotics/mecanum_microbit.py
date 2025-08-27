"""
Keyestudio Micro bit 4WD Mecanum Robot Car V2.0
https://www.keyestudio.com/products/keyestudio-micro-bit-4wd-mecanum-robot-car-v20-diy-smart-kit-with-microbit-board
https://docs.keyestudio.com/projects/KS4034/en/latest/
https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html

Resources:
https://docs.keyestudio.com/projects/KS4034/en/latest/docs/index.html#obtain-resources-important

View Hex-file in Online-Editor (drag and drop):
https://makecode.microbit.org/#editor
"""

def car_back():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)

def car_move_RF():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 0)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 0)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def drift_left():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 0)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def car_left():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def on_bluetooth_connected():
    global connect_flag, ble_val, color_num, speed_LF, speed_LB, speed_RF, speed_RB
    connect_flag = 1
    while connect_flag == 1:
        ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        serial.write_string(ble_val)
        serial.write_line("")
        if ble_val == "a":
            car_forward()
        elif ble_val == "b":
            car_left()
        elif ble_val == "c":
            car_back()
        elif ble_val == "d":
            car_right()
        elif ble_val == "k":
            car_left_move()
        elif ble_val == "h":
            car_right_move()
        elif ble_val == "g":
            car_move_RF()
        elif ble_val == "i":
            car_move_RB()
        elif ble_val == "j":
            car_move_LB()
        elif ble_val == "l":
            car_move_LF()
        elif ble_val == "s":
            mecanumRobotV2.state()
        elif ble_val == "t":
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
        elif ble_val == "u":
            mecanumRobotV2.set_led(LedCount.LEFT, LedState.OFF)
            mecanumRobotV2.set_led(LedCount.RIGHT, LedState.OFF)
        elif ble_val == "e":
            drift_left()
        elif ble_val == "f":
            drift_right()
        elif ble_val == "m":
            if color_num < 3:
                color_num = color_num + 1
            showcolor()
        elif ble_val == "n":
            if color_num > 0:
                color_num = color_num - 1
            showcolor()
        elif ble_val == "o":
            strip.clear()
            strip.show()
        elif ble_val == "v":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_LF = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_LF)
            serial.write_line("")
        elif ble_val == "w":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_LB = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_LB)
            serial.write_line("")
        elif ble_val == "x":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_RF = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_RF)
            serial.write_line("")
        elif ble_val == "y":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_RB = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_RB)
            serial.write_line("")

bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def car_move_LB():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 0)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 0)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)

def showcolor():
    if color_num == 0:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif color_num == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif color_num == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    strip.show()

def car_move_RB():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 0)

def tracking():
    if mecanumRobotV2.line_tracking(LT.LEFT) == 0 and (mecanumRobotV2.line_tracking(LT.CENTER) == 0 and mecanumRobotV2.line_tracking(LT.RIGHT) == 0):
        mecanumRobotV2.state()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 0 and (mecanumRobotV2.line_tracking(LT.CENTER) == 0 and mecanumRobotV2.line_tracking(LT.RIGHT) == 1):
        car_right()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 0 and (mecanumRobotV2.line_tracking(LT.CENTER) == 1 and mecanumRobotV2.line_tracking(LT.RIGHT) == 0):
        car_forward()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 0 and (mecanumRobotV2.line_tracking(LT.CENTER) == 1 and mecanumRobotV2.line_tracking(LT.RIGHT) == 1):
        car_right()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 1 and (mecanumRobotV2.line_tracking(LT.CENTER) == 0 and mecanumRobotV2.line_tracking(LT.RIGHT) == 0):
        car_left()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 1 and (mecanumRobotV2.line_tracking(LT.CENTER) == 0 and mecanumRobotV2.line_tracking(LT.RIGHT) == 1):
        car_forward()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 1 and (mecanumRobotV2.line_tracking(LT.CENTER) == 1 and mecanumRobotV2.line_tracking(LT.RIGHT) == 0):
        car_left()
    elif mecanumRobotV2.line_tracking(LT.LEFT) == 1 and (mecanumRobotV2.line_tracking(LT.CENTER) == 1 and mecanumRobotV2.line_tracking(LT.RIGHT) == 1):
        car_forward()

def car_right_move():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def drift_right():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 0)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)

def follow():
    mecanumRobotV2.set_servo(90)
    basic.pause(500)
    if mecanumRobotV2.ultra() <= 10:
        car_back()
    elif mecanumRobotV2.ultra() > 20 and mecanumRobotV2.ultra() <= 40:
        car_forward()
    else:
        mecanumRobotV2.state()

def car_move_LF():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 0)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 0)

def avoid():
    global distance, distance_l, diatance_r
    distance = mecanumRobotV2.ultra()
    if distance < 15:
        mecanumRobotV2.state()
        basic.pause(500)
        mecanumRobotV2.set_servo(160)
        basic.pause(500)
        distance_l = mecanumRobotV2.ultra()
        basic.pause(100)
        mecanumRobotV2.set_servo(20)
        basic.pause(200)
        diatance_r = mecanumRobotV2.ultra()
        basic.pause(200)
        mecanumRobotV2.set_servo(90)
        basic.pause(500)
        if distance_l > diatance_r:
            car_left()
            basic.pause(500)
        else:
            car_right()
            basic.pause(500)
    else:
        car_forward()

def car_forward():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def car_left_move():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)

def car_right():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)

diatance_r = 0
distance_l = 0
distance = 0
ble_val = ""
connect_flag = 0
strip: neopixel.Strip = None
color_num = 0
speed_RB = 0
speed_RF = 0
speed_LB = 0
speed_LF = 0
serial.redirect_to_usb()
speed_LF = 50
speed_LB = 50
speed_RF = 50
speed_RB = 50
color_num = 0
strip = neopixel.create(DigitalPin.P7, 4, NeoPixelMode.RGB)
led.enable(False)

def on_forever():
    if ble_val == "p":
        tracking()
    elif ble_val == "q":
        follow()
    elif ble_val == "r":
        avoid()
    elif ble_val == "s":
        mecanumRobotV2.state()
        mecanumRobotV2.set_servo(90)

basic.forever(on_forever)
