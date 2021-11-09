def first_func():
    a=int(input("enter how many cm to convert "))
    b=a*2.54
    print(f'{a} cm = {b} ')

#могла использовать и return со значениями но пока что не обязательно,хотела оставить крассивую строку)
def second_func():
    a=int(input("enter how many dm to convert "))
    b=a%2.54
    print(f'{a} dm = {b} cm ')

def third_func():
    a=int(input("enter how many miles to convert "))
    b=a*1.61
    print(f'{a} miles = {b} km ')

def fourth_func():
    a=int(input("enter how many km to convert "))
    b=a%1.61
    print(f'{a} km = {b} miles ')

def fifth_func():
    a=int(input("enter how ft  to convert "))
    b=a*0.45
    print(f'{a} ft = {b} kg')


def sixth_func():
    a = int(input("enter  km to convert "))
    b = a%0.45
    print(f'{a} ft = {b} kg')

def seventh_func():
    a = int(input("enter  kп to convert "))
    b = a%28.35
    print(f'{a} кг = {b} unc')

def eighth_func():
    a = int(input("enter  unc to convert "))
    b = a % 28.35
    print(f'{a} unc = {b} kg')
def ninth_func():
    a = int(input("enter  gl to convert "))
    b = a*4.55
    print(f'{a} gl = {b} litres')
def tenth_func():
    a = int(input("enter  gl to convert "))
    b = a%4.55
    print(f'{a}  litres = {b} gl')
def eleventh_func():
    a = int(input("enter  pintes to convert "))
    b = a*0.568
    print(f'{a} pintes  = {b} liters')
def twelfth_func():
    a = int(input("enter  gl to convert "))
    b = a%0.568
    print(f'{a}  litres = {b} pintes')



while(True):
    print("enter right option:")
    print("1. Дюймы в сантиметры\n 2. Сантиметры в дюймы \n3. Мили в километры\n4. Километры в мили\n5. Фунты в килограммы\n6. Килограммы в фунты\n7. Унции в граммы\n8. Граммы в унции\n9. Галлон в литры\n10. Литры в галлоны\n11. Пинты в литры\n12. Литры в пинты")
    a=int(input())
    if a<0 or a>12:
        print("unright variiant")
    else:
        if a==1:
            first_func()
        elif a==2:
            second_func()
        elif a==3:
            third_func()
        elif a==4:
            fourth_func()
        elif a==5:
            fifth_func()
        elif a==6:
            sixth_func()
        elif a==7:
            seventh_func()
        elif a==8:
            eighth_func()
        elif a==9:
            ninth_func()
        elif a==10:
            tenth_func()
        elif a==11:
            eleventh_func()
        elif a==12:
            twelfth_func()
        else:
            break