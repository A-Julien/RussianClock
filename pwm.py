import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(35)
raw_input('press')
p.stop()
GPIO.cleanup()
