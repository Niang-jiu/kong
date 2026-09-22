import random
import time
a = int(input("猜一個0-99間的整數"))
t = random.randint(0,99)
while (1):
    if (a==t):
        print("答對ㄌ")
        break
    elif (a>t):
        a=int(input("太大重猜"))
    else :
        a=int(input("太小重猜"))
