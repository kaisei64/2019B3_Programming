a = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
b = a.replace(".", "")
c = b.split()

ones = [0, 4, 5, 6, 7, 8, 14, 15, 18]

dict = {}
for i, word in enumerate(c):
    if i in ones:
        dict[word[0]] = i + 1
    else:
        dict[word[0:2]] = i + 1

print(dict)
