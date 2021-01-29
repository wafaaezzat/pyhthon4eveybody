fname=input('enter file: ')
if len(fname)<1: fname='regex.txt'
handle=open(fname)

x=list()
import re

for line in handle:
    line = line.rstrip()
    y=re.findall('[0-9]+',line)
    x=x+y
sum=0
for item in x :
    sum=sum+int(item)
print(x)
print(sum)
