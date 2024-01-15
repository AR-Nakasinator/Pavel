from machine import Pin
from time import sleep_ms

pin = Pin("LED", Pin.OUT)
zprava = input("NECO NAPSANÉHO") 

print(zprava)
print(len(zprava))
print(range(len(zprava)))


abeceda = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
kod = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]


for i in range(len(zprava)):
  pismeno = zprava[i]
  print(abeceda.index(pismeno))
  pozice = abeceda.index(pismeno)
  print(kod[pozice])
  morse = (kod[pozice])
  print(morse)
  for i in range(len(morse)):
    if morse[i] == ".":
        pin.on()
        sleep_ms(100)
        pin.off()
        sleep_ms(100)
    elif morse[i] == "-":
        pin.on()
        sleep_ms(300)
        pin.off()
        sleep_ms(100)
    elif morse[i] == " ":
        sleep_ms(300)
        
