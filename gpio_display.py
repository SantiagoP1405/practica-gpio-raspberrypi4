import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    a = 18
    GPIO.setup(a, GPIO.OUT)
    b = 23
    GPIO.setup(b, GPIO.OUT)
    c = 24
    GPIO.setup(c, GPIO.OUT)
    d = 17
    GPIO.setup(d, GPIO.OUT)
    e = 27
    GPIO.setup(e, GPIO.OUT)
    f = 22
    GPIO.setup(f, GPIO.OUT)
    g = 10
    GPIO.setup(g, GPIO.OUT)
    while True:
        # 0
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,1)
        time.sleep(1)
        
        #1
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
        time.sleep(1)

        #2
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
        GPIO.output(g,0)
        time.sleep(1)

        #3
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,0)
        time.sleep(1)

        #4
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

        #5
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

        #6
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

        #7
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
        time.sleep(1)

        #8
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

        #9
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

        #A
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)
        
        #b
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)
        
        #C
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,1)
        time.sleep(1)
        
        #d
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
        GPIO.output(g,0)
        time.sleep(1)

        #E
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)
        
        #F
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
        GPIO.output(g,0)
        time.sleep(1)

if __name__=="__main__":
    main()