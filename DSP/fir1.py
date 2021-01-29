import math
import numpy
print("Welcome at fir1")
N = int(input("Enter N"))
n = int((N-1)/2)
print("n=", n)
gama = float(input("Enter gama \n"))
h=[]
h.append(round(gama/math.pi,3))
for i in range(1, (n+1)):
    h.append(round(math.sin(i*gama)/(i*3.14) ,3))
print("\n h = ", h)
x = float(input("first factor "))
y = float(input("second factor "))
w=[]
w.append(1)
for i in range(1, (n+1)):
    w.append(round(x + y*math.cos((i*math.pi)/n), 3))
print("\n w = ", w)
z=[]
for i in range(0, (n+1)):
    z.append(round(h[i]*w[i], 3))
print("\n h*w = ", z)
ir=[]
for i in range(-1,-(n+1),-1):
    ir.append(z[i])
for i in z:
    ir.append(i)
print("\n impuls=", ir)
sr=[]
sum=0
for i in ir:
    sum=sum+i
    sr.append(round(sum,3))
print("\n step", sr)
omga=[]
for i in numpy.arange(0,1.1,0.1):
    omga.append(round(i*math.pi,4))
print("\n omga = ", omga)
H=[]
for i in omga:
    sum=0
    for c in range (1,len(z)):
        sum=sum+2*z[c]*math.cos(i*c)
    sum=sum+h[0]
    H.append(sum)
print("\n H = ", H)
logs=[]
for i in H:
    if i < 0:
        i=i*-1
        logs.append(-1*20*math.log10(i))
    else:
        logs.append(20 * math.log10(i))
print("\n log= ",logs)
