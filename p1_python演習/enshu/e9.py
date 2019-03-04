import sys
import random

for word in sys.argv[1:]:
    if len(word) <= 3:
        sys.stdout.write(word + " ")
    elif len(word) > 3:
        #sys.stdout.write(random.shuffle(a))
        b = random.sample(word, len(word))
        c = ''.join(b)
        sys.stdout.write(c + " ")
else:
    print()