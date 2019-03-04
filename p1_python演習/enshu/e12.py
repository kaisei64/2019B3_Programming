path = 'dataset/data.txt'
s = list()
with open(path) as f:
    for s_line in f:
        s_line = s_line.rstrip()
        s.append(s_line.split("と"))

print('docs : ', s)

t = list()
with open(path) as f:
    for t_line in f:
        t_line = t_line.rstrip()
        t = t + t_line.split("と")
print('terms: ', list(set(t)))