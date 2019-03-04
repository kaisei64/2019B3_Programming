from math import log
import pandas as pd
import numpy as np
import math

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


def idf(term, doc):
    df = 0
    for doc in docs:
        df += term in doc

    return math.log10(N / df) + 1

result2 = []
for j in range(len(terms)):
    t = terms[j]
    d = docs[j]
    result2.append(idf(t, d))

idf_ = pd.DataFrame(result2, index=terms, columns=["IDF"])

def tfidf(tf1, idf1):
    x = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            x[i][j] = tf1[i][j] * idf1[j]

    return x

print(tfidf(result, result2))