
#Hacemos el import de la libreria GPIO, la renombramos como GPIO
import RPi.GPIO as GPIO

#Cambiamos el modo de las GPIO a BCM (No se lo que significa
GPIO.setmode(GPIO.BCM)

#Hacemos que el pin 17 y 27 de las GPIO
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

# Pintamos por pantalla un mensajito
print("Import correcto y configuración correcta")
