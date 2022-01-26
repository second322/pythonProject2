a = 'Hello'
print(a, type(a))
b = 3
print(b, type(b))
c = 3.2
print(c, type(c))
d = bytes(1)
print(d, type(d))
e = [10]
print(e, type(e))
f = tuple('1', )
print(f, type(f))
g = set(a)  # Убирает повторяющиеся элементы в множестве
print(g, type(g))
h = frozenset(a)
print(h, type(h))
l = {'a': 'A'}
print(l, type(l))

Str1 = 'Hello '
Str2 = 'World'
Str_Sum = Str1 + Str2
print(Str_Sum)

print(a, b)


i = 0
for i in b, c, d, e, f, g, h, l:
    print(i, 'Type', type(i))
    i += 1

print('end')
print('10) В консоле после каждый переменной есть название переменной')
