#задание 27
import math
a=0
b=1
x=a
s=0
i=0
e=0.000001
while i<=1000000:
    y=(x**2)*math.cos(x)
    if (i==0) or (i==1000000):
        s=s+y
    if (i%2)>0 and (i!=1000000) and (i!=0):
        s=s+(y*4)
    if (i%2)==0 and (i!=1000000) and (i!=0):
        s=s+(y*2)
    x=x+e
    i = i + 1
s=s*(e/3)
print(s)