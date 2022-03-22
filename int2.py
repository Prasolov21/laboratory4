#задание 17
import math
a=0
b=0.9
x=a
e=0.001
y=0
y0=0
s=0
while x<b:
    y0=x*math.asin(x)
    x=x+e
    y=x*math.asin(x)
    s=s+(((y+y0)/2)*e)
print(s)