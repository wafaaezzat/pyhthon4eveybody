score=input('enter score')
try:
    scoref=float(score)
except:
    print('enter numeric value')
    quit()
if (scoref<0)|(scoref>1):
    print('out of range')
elif scoref>=0.9:
    print('A')
elif scoref>=0.8:
    print('B')
elif scoref>=0.7:
    print('C')
elif scoref>=0.6:
    print('D')
elif scoref<0.6:
    print('F')
