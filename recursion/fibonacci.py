def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i, val in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=i, f=val))
     if i == 10:
         break

    