import time
from random import randint
def loading():
    print("loding......")
    time.sleep(1)
    for i in range(1,16):
        print(i,end=",")
        time.sleep(1)
    print("\n...loading end")
loading()