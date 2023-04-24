def generator(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            yield j ** i
for i in generator(3, 4):
    print(i)