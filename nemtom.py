import threading
import time

input_ = int(input("Ener the seconds: "))
seconds = range(input_)
a = list(seconds)
a.reverse()

b = list(range(10))
b.reverse()

def timer():
    for i in a:
        
        if i > 1:
            print("{} seconds left".format(i))
            time.sleep(1)

        if i == 10:
            
            print("{} Seconds passed".format(i))
            trigger = input("Continue the thread?\n")
            
            if trigger == "yes":
                
                for i in b:
                    if i > 1:
                        print("{} seconds left".format(i))
                        time.sleep(1)

                    elif i == 1:
                        print("{} seconds left".format(i))
                        time.sleep(1)
                        print("No time left my son!!!")
                        time.sleep(1)

        if i < 10:
            break
thread1 = threading.Thread(target=timer)
thread1.start()