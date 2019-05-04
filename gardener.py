from machine import Pin, TouchPad
from time import sleep

def start_pump(duration=3):
    RELAY(0)    # on
    sleep(duration)
    RELAY(1)    # off


if __name__ == "__main__":

    # setup
    RELAY = Pin(15, Pin.OUT)
    
    # turn RELAY off at startup
    RELAY(1)
    WATERING_TIME = '2:51'

    surface = TouchPad(Pin(12))
    threshold = []

    # scan surface to calibrate
    for x in range(12):
        threshold.append(surface.read())
        sleep(0.2)

    threshold = sum(threshold)/len(threshold)

    while True:
        capacitance = surface.read()
        capacitance_ratio = capacitance / threshold

        if 0.40 < capacitance_ratio < 0.90:
            print('Capacitance: {0}, Diff: {1}, Ratio: {2}'.format(
                    capacitance, threshold - capacitance, capacitance_ratio))
            start_pump()

        sleep(0.2)
