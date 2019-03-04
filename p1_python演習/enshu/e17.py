from nlp.e15 import tf_idf
from nlp.e16 import cosine_sim
import numpy as np

path = 'dataset/data.txt'
docs = list()
with open(path) as f:
    for s_line in f:
        s_line = s_line.rstrip()
        docs.append(s_line.split("と"))

print('docs : ', docs)

terms = list()
with open(path) as f:
    for t_line in f:
        t_line = t_line.rstrip()
        terms = terms + t_line.split("と")
terms = list(set(terms))
print('terms: ', terms)

x = np.zeros((len(docs),len(docs)))
y = tf_idf(terms, docs)
for i, doc in enumerate(docs):
    for j, term in enumerate(docs):
        x[i][j] = cosine_sim(y[i], y[j])

print(x)