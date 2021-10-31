a = []
for i in range(19):
    a.append(int(input()))
max=a[0]
for i in range(19):
    if a[i]>max:
        max=a[i]
print(max)
for i in range(19):
    if a[i]/2==0:
        a[i]=max
print(a)