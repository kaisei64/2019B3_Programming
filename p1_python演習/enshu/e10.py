import sys
import re

moji = sys.argv[1].split()

def n_gram(n, moji):
    result = []
    for it in range(0, len(sys.argv[1])):
        if it + n > len(moji):
            return result
        result.append(moji[it: it + n])

m = ''.join(moji)
print('単語bi-gram: ', n_gram(2, moji))
print('文字bi-gram: ', n_gram(2, m))