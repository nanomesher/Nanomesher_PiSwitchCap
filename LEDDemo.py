'''
Copyright [2018] [Nanomesher Limited - www.nanomesher.com]

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either e$
'''


import time
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setwarnings(False)

print("This program will blink the LED twice")

GPIO.setup(12, GPIO.OUT)
GPIO.output(12,False)

GPIO.setup(12, GPIO.OUT)
GPIO.output(12,True)

time.sleep(2)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,False)
time.sleep(2)

GPIO.setup(12, GPIO.OUT)
GPIO.output(12,True)

time.sleep(2)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,False)
