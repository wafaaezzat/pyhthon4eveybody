fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word=line.split()
    for element in word:
        if not element in lst:
            lst.append(element)
        else:
            continue
lst.sort()
print(lst)
