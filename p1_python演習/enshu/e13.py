from math import log
import pandas as pd

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
N = len(docs)

def tf(term, doc):
    return doc.count(term) / len(doc)


result = []
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(terms)):
        t = terms[j]

        result[-1].append(tf(t, d))

tf_ = pd.DataFrame(result, columns=terms)
print(tf_)
print()
print("0: ['リンゴ', 'リンゴ'], 1: ['リンゴ', 'レモン'], 2: ['レモン', 'ミカン']")