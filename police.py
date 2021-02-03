#!/usr/bin/env python3
from ev3dev.ev3 import *

us = UltrasonicSensor() 
assert us.connected, "Connect a single US sensor to any sensor port"

ev3.Sound.speak('Achtung. Einbrecher detektiert. Polizei  Polizei Polizei.').wait()
