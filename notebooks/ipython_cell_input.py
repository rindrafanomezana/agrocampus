
from time import sleep
def fibonacci(n):
    f1, f2 = 1, 1
    res = []
    for i in range(n):
        f1, f2 = f2, f1+f2
        res.append(f1)
    return res

fibonacci(100)
