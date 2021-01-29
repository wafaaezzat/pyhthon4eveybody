fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if line.find('From:'):
        print(line)
