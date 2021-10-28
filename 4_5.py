fib_1=1
fib_2=1
print(fib_1)
print(fib_2)
i=0
while i <15:
    fib_sum=fib_1+fib_2
    fib_1=fib_2
    fib_2=fib_sum
    print(fib_sum)
    i+=1
