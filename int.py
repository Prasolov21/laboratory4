#задание 7
a=1
b=4
x=a
e=0.000001
y=0
s=0
while x<b:
    x=x+e
    y=(x**2)*((x+1)**(-2))
    s=s+(y*e)
print(s)