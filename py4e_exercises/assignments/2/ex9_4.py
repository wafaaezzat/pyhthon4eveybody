name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
words=list()
for line in handle:
    if line.startswith('From:'):
        words=line.split()

        counts[words[1]]=counts.get(words[1],0)+1

big_k=None
big_v=None

for key,val in counts.items():
    if big_v == None or val > big_v:
        big_v=val
        big_k=key
print(big_k,big_v)
    
