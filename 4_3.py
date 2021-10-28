# 1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
import random

n = 5
m = 5

a = 1
b = 10

mat = [[random.randint(a,b) for x in range(m)] for i in range(n)]
for i in mat:
    for g in i:
        print(g, end=' ')
    print()

elem = mat[0][0]

'''for i in mat:
    for x in i:
        if x<elem:
            elem=x
print(elem)

su = 0

for i in mat:
    for x in i:
        su+=x
print(su)'''

sum_el = 0
sum_max = 0

print()
dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict2 = {}

keys = list(dict1.keys())
val = list(dict1.values())
dict1.clear()
i = 0
while i != len(keys):
    dict1[keys[i]+str(len(keys[i]))] = val[i]
    i += 1
print(dict1)