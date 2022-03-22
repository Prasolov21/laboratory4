#задание 7
x=1
x0=0
n=-1
s=0
e=0.000001
while abs(x-x0)>e:
    x=x0
    n=n+1
    x0=(3/(2**(n+2)))-(2/(3**(n+3)))
    s=s+x0
    print(x0 ,s,n)