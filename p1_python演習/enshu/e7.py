a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
b = a.replace(",", "")
c = b.replace(".", "")
d = c.split()
e = [len(d[i]) for i in range(0, 15)]
print(e)