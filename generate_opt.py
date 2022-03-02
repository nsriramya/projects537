import math as m
import random as r
import string as s
n=int(input("enter otp n value="))#4 or 6
def generate_opt(n):
    otp=""
    d=s.digits#0123456789
    for k in range(n):#k=0
        otp=otp+d[m.floor(r.random()*10)]
    return otp
print("OTP=",generate_opt(n))
#0.56 0.21 0.87 0.97
#otp=0+d[m.floor(0.56*10)]
#otp=0+d[m,floor(5.6)]
#otp=0+d[5]
#otp=0+5
#otp=5
