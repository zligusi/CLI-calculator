# The cod is a mini kalkylator 

while True :
    try :                #
        a = int(input("Введите первое число : "))
        break
    except ValueError :
        print("Вы ввели не число ")

while True :        # цикл  / знак операции
    want = input("Что делаем ? (+ , - ,  * ,  : )")
    if want in ["+" , "-" , "*" , ":"] :
        break
    else : 
        print("Вы ввели не правильный знак операции ")
        
while True :        
    try :
        b = int(input("Введите второе число : "))
        break
    except ValueError :
        print("Вы ввели не число ")

while True :         #Цикл / основной калькулятор 
    try :
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