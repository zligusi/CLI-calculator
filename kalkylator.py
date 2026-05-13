# The cod is a mini kalkylator 
import time


hg = 0
while hg < 1000 :        
    while True :           # проверка на число
        try :                
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
        
    while True :        #проверка на число
        try :
            b = int(input("Введите второе число : "))
            break
        except ValueError :
            print("Вы ввели не число ")
            
    if want == "+" :
        c = a + b 
    elif want == "-" :
        c = a - b 
    elif want == "*" :
        c = a * b
    elif want == ":" :
        c = a / b

    print(f"Результат : {c}")
    
    while True :
        go = input(str("Хотите продолжить ? (yes / no ) : ")).strip().lower()
        if go in ["yes" , "no"]:
            break
    if go == "yes" :
        print("Продолжим !")
        time.sleep(2)
    elif go == "no" :
        print("До свидания !")
        exit()