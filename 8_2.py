string_a=input("enter string")

def palindrom(string_a):
    k=len(string_a)
    counter=0

    if k%2==0:
         for i in range((k-1)//2):
             if string_a[i]==string_a[k-i]:
                 counter+=1
                 if counter==(k-1)/2:
                     print("palindrom")
             else:
                print('not palindrom')
                break
    else:
         for i in range((k-1)//2):
            if string_a[i] == string_a[k - 1-i]:
                counter += 1
                if counter==(k-1)//2:
                    print("palindrom")
            else:
                print('not palindrom')
                break

palindrom(string_a)



