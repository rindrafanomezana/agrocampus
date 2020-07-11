
f1, f2 = 1, 1
for n in range(10):
    print(f1, end=',')
    f1, f2 = f2, f1+f2
