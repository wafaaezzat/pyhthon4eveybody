fname=input('enter the file name:')
fh=open(fname)
count=0
for line in fh:
    line=line.rstrip()
    wds=line.split()
    if len(wds)< 1:
        continue
    if wds[0]!='From':
        continue
    print(wds[1])
    count=count+1
print('sum of FROM:IS   ',count)
