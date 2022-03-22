#задание 17
x=1
x0=0
n=0
s=0
e=0.000001
while abs(x-x0)>e:
    x=x0
    n=n+1
    x0=1/((36*(n**2))-(24*n)-5)
    s=s+x0
    print(x0,s,n,x-x0)