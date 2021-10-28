list_a=[2,3,4,5]
counter=0

for i in list_a:
    if list_a[i]/2==0:
        i+=1
        counter+=1
print(counter)