fname=input('enter file: ')
if len(fname)<1: fname='intro.txt'
handle=open(fname)

for line in handle:
    wds=line.split()
    print(wds)
