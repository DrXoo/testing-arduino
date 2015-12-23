
#include <Wire.h>
#include <LCD.h> // For LCD
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C  lcd(0x27,2,1,0,4,5,6,7);



void setup()
{
  lcd.begin(16,2);
  //Iniciamos el fondo retroiluminado
  lcd.setBacklightPin(3,POSITIVE); // BL,BL_POL
  lcd.backlight();
  //Iniciamos la pantalla
}


void loop()
{
  lcd.home (); // Set cursor to 0,0
  lcd.setCursor (1,0);
  lcd.print("Domingo Garcia");//Escribimos en la primera linea
  lcd.setCursor(2,1);//Saltamos a la segunda linea
  lcd.print("Julia Romero");//Escribimos en la segunda linea
  lcd.backlight();
  //Tiempo de espera para que reinicie el ciclo
  delay(10000);
  
}
