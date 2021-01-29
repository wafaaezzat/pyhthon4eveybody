largest=0
smallest=0

while True:
    try:
        num=input('enter number\n')
        if num=="done":
            break
        numi=int(num)
        if largest<numi or largest==0:
            largest=numi
        if smallest>numi or smallest==0:
            smallest=numi
    except:
        print('invalid input')
print('max is  ',largest)
print('min is ',smallest)
