print('exercise 6.5 ')
str='X-DSPAM-Confidence:    0.8475';
ipos=str.find(':')
print(str)
print(ipos)
piece=str[ipos+1:]
print(float(piece))
