# The cod is a mini kalkylator 
#Цикл 1 : исключаем вариацию ввода не верного знака операции 
while True :
    want = input("Что делаем ? (+ , - ,  * ,  : )")
    if want in ["+" , "-" , "*" , ":"] :
        break
    else : 
        print("Вы ввели не правильный знак операции ")
        
#Цикл 2 : исключаем вариацию ввода не числа
while True :
    try :
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        
        if want == "+" :
            c = a + b 
        elif want == "-" :
            c = a - b 
        elif want == "*" :
            c = a * b
        elif want == ":" :
            c = a / b
        else :
            print("Вы ввели не правильный знак операции ")
        break
    except ValueError :
        print("Вы ввели не число ")
print(f"Результат : {c}")