import numpy as np
import math


def tf(term, doc):
    return doc.count(term) / len(doc)


def idf(term, docs):
    df = 0
    for doc in docs:
        df += term in doc

    return math.log10(len(docs) / df) + 1


def tf_idf(terms, docs):
    x = np.zeros((3, 3))
    for i, doc in enumerate(docs):
        for j, term in enumerate(terms):
            x[i][j] = tf(term, doc) * idf(term, docs)
    return x

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

print(tf_idf(terms, docs))
