import math

signal_power = 9
signal_noise = 10

ratio  = signal_power / signal_noise

decibels = 10 * math.log10(ratio)

print(decibels)