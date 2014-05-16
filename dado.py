# PROYECTO DE LA SEMANA 3
# por > Leonardo Enrique Castillo	
# castillo.leo@gmail.com

# Disposicion de leds
# 0a-----0b
# |      |
# |      |
# 0c--0d-0e
# |      |
# |      |
# 0f-----0g 

num = [
    #a b c d e f g Leds
    [0, 0, 0, 1, 0, 0, 0], # 1
    [0, 0, 1, 0, 1, 0, 0], # 2
    [0, 1, 0, 1, 0, 1, 0], # 3
    [1, 1, 0, 0, 0, 1, 1], # 4
    [1, 1, 0, 1, 0, 1, 1], # 5
    [1, 1, 1, 0, 1, 1, 1], # 6
    [0, 0, 0, 0, 0, 0, 0], # blank
];
import wiringpi2
import time
import sys
import random
io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

# activation pins
Pins = [ 1, 2, 3, 4, 5, 6 ]

# setup all pins
for i in range(0, len(Pins)):
    io.pinMode(Pins[i],io.OUTPUT)    
    io.digitalWrite(Pins[i],io.LOW)

# main loop
# to terminate the loop press CTRL+C
while True:
    num = random.randint (1, 6) # genera numero
    segmentsToLit = numero[num]
        for led in range(0, 6):
            # True or False based on segmentDigits table
            val = bool(segmentsToLit[led])
            io.digitalWrite(Pins[led],val)
        # short pause
        time.sleep(3)
		for led in range(0, 6):
            io.digitalWrite(Pins[led],io.HIGH)
        # short pause
        time.sleep(1)