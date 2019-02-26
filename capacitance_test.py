from machine import Pin, TouchPad
from time import sleep

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

    if 0.40 < capacitance_ratio < 0.95:
        print('Capacitance: {0}, Diff: {1}, Ratio: {2}'.format(
                  capacitance, threshold - capacitance, capacitance_ratio))
    sleep(0.2)

