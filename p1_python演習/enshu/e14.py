from math import log
import pandas as pd
import math

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
N = len(docs)


def idf(term, doc):
    df = 0
    for doc in docs:
        df += term in doc

    return math.log10(N / df) + 1


result = []
for j in range(len(terms)):
    t = terms[j]
    d = docs[j]
    result.append(idf(t, d))

idf_ = pd.DataFrame(result, index=terms, columns=["IDF"])
print(idf_)