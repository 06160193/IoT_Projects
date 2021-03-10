
import RPi.GPIO as GPIO
import time
v=34300

output_pin = 12

TRIGGER_PIN=16
ECHO_PIN=18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
def measure() :
   GPIO.output(TRIGGER_PIN, GPIO.HIGH)
   time.sleep(0.00001)  #10us
   GPIO.output(TRIGGER_PIN, GPIO.LOW)

      
   while GPIO.input(ECHO_PIN) == GPIO.LOW :
      pulse_start=time.time()
        
   while GPIO.input(ECHO_PIN) == GPIO.HIGH :
      pulse_end=time.time()
   
   t=pulse_end-pulse_start
   d=t*v/2


   time.sleep(1)
   # Toggle the output every second
   print(d)
   
   if d > 20 :
      GPIO.output(output_pin, GPIO.LOW)
   else :
      if d < 10 :
         three = 0.5
      else :
         three=1
      time.sleep(three)
      GPIO.output(output_pin, GPIO.HIGH)
      time.sleep(three)
      GPIO.output(output_pin, GPIO.LOW)


if __name__ == '__main__':
   while True:
      measure()

GPIO.cleanup()
