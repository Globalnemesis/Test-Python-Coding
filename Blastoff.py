import time
x=input("Countdown time in seconds: ")
while x>0:
    print "Time to Launch",x,"seconds"
    x=x-1
    time.sleep(1)
print "BLASTOFF!"
