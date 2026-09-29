import time
import random
while(z := int(input("最大數字是:"))) < 1:
    z = int(input("要大於1，重設 最大數字是:"))
t = random.randint(1,z)
m = 1
a = int(input(f"請猜一個數字({m}~{z}): "))
while(a!=t):
    if((a<t) and (a>m)):
        m = a
    elif((a<t) and (a<m)):
        print("你猜的數字小於最小值，請重新輸入")
    elif((a>t) and (a<z)):
        z = a
    elif((a>t) and (a>z)):
        print("你猜的數字大於最大值，請重新輸入")
    a = int(input(f"請猜一個數字({m}~{z}): "))
print("答對ㄌ")

