a = []
b=[]
min_number=0
for i in range(1,7):
    a.append(int(input()))

for i in range(len(a)):
    if a[i]<=a[i+1]:
        b[i]=a[i]
print(b)
