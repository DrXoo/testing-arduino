import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)

def  blink():
	print("Ejecución iniciada")

	iteracion = 0

	while iteracion < 30:
		
		print("Enciendo el LED")
		GPIO.output(17, True)

		time.sleep(1)

		print("Apago el LED")
		GPIO.output(17,False)

		time.sleep(1)

		iteracion=iteracion+1
	# Limpio las conexiones que he configurado para abanadonarlas
	GPIO.cleanup()

blink()
