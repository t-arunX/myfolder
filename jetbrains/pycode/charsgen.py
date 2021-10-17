import itertools

gen = []
alpha = ''
for i in range(97, 123):
    alpha += chr(i)
"""for j in range(1, 27):
    fun = itertools.combinations(alpha, j)
    while True:
        try:
            print(next(fun))
        except StopIteration:
            break"""

print(alpha)