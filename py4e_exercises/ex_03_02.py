hrs=input("enter the hours: ")
rate=input("enter the rate: ")
try:
    hrsf=float(hrs)
    ratef=float(rate)
except:
    print("error plz enter numeric value")
    quit()
if hrsf>40:
    pay=(hrsf-40)*(ratef*0.5)+(ratef*hrsf)
else:
    pay=ratef*hrsf
print("pay=",pay)
