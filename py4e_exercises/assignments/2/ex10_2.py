name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst1=list()
lst2=list()
dct=dict()
for line in handle:
    if line.startswith('From'):
        lst1=line.split()
        if len(lst1)<3:continue
        lst2=lst1[5].split(':')
        h=lst2[0]
        dct[h]=dct.get(h,0)+1
for k,v in sorted(dct.items()):
    print(k,v)
