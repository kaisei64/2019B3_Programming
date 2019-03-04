from math import log
import pandas as pd
import math


def idf(term, docs):
    df = 0
    for doc in docs:
        df += term in doc

    return math.log10(N / df) + 1


docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
N = len(docs)


result = []
for j in range(len(terms)):
    t = terms[j]
    result.append(idf(t, docs))

idf_ = pd.DataFrame(result, index=terms, columns=["IDF"])
print(idf_)