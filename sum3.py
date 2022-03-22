#задание 27
import math
x=1
x0=0
n=0
s=0
e=0.000001
while abs(x-x0)>e:
    x=x0
    n=n+1
    x0=math.log(n*((2*n)+1)/((n+1)*((2*n)-1)))
    s=s+x0
    print(x0 ,s,n)
