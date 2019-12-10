#Just an easy sample to test the time lib
import time
print('I can count the seconds:')
i = 1
 
while True:
    print("Are passed ",i," seconds from the start...")
    i += 1
    time.sleep(1.0)  # 1 second delay