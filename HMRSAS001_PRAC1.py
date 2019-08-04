import RPi.GPIO as GPIO
import time

# 1  2  4 BIN DIGITS
#31 32 33 CORRESPONDING PINS

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.output(6,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
print("setup done")
counter = 0

def pushbutton():
	global counter
	if(GPIO.input(17) == 1 and counter != 7):
		counter += 1
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if(GPIO.input(17) == 1 and counter == 7):
		counter = 0
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if(GPIO.input(4) == 1 and counter != 0):
		counter -= 1
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if(GPIO.input(4) == 1 and counter == 0):
		counter = 7
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	return

def led(c):
	binarystr = bin(c)[2:].zfill(3)
	for index, value in enumerate(binarystr):
		if(value == '1'):
			ledOn(index)
		else:
			ledOff(index)
	return

def ledOn(pin):
	if (pin == 0):
		GPIO.output(6,GPIO.HIGH)
	if (pin == 1):
		GPIO.output(12,GPIO.HIGH)
	if (pin == 2):
		GPIO.output(13,GPIO.HIGH)
	return

def ledOff(pin):
	if (pin == 0):
		GPIO.output(6,GPIO.LOW)
	if (pin == 1):
		GPIO.output(12,GPIO.LOW)
	if (pin == 2):
		GPIO.output(13,GPIO.LOW)
	return


try:
	while True:
		pushbutton()
		led(counter)
	GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.cleanup()

