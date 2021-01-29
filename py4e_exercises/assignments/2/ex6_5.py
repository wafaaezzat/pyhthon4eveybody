text = "X-DSPAM-Confidence:    0.8475";
num=text.find(':')
str1=text[num+1:]
str2=str1.lstrip()
print(float(str2))
