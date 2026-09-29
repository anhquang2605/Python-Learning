def func(n):
    a, b = 0, 1
    while a < n:  
        yield a
        a, b = b, a + b
    print();

func(100)


t = 'hello', 'world', 123
print(t)
print(t[0])
print(t[1])
print(t[2])

#unpacking assignment
a, b, c = t
print(a)
print(b)
print(c)