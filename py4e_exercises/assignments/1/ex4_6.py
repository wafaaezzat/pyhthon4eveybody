def computepay(h,r):
    if h>40:
        pay=(h-40)*0.5*r+h*r
    else:
        pay=h*r
    return pay

hrs=input('enter hours\n')
hrsf=float(hrs)
rate=input('enter rate per hour\n')
ratef=float(rate)
p=computepay(hrsf,ratef)
print('pay=',p)
