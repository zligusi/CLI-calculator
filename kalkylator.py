# The cod is a mini kalkylator 
import time
from colorama import Fore , Back , Style


hg = 0
while hg < 1 :        
    while True :           # проверка на число
        try :  
            print(Fore.CYAN)              
            a = int(input("Введите первое число : "))
            break
        except ValueError :
            print(Back.RED)
            print(Fore.BLACK)
            print("Вы ввели не число ")

    while True :# цикл  / знак операции
        print(Fore.GREEN)
        want = input("Что делаем ? (+ , - ,  * ,  : , ** ) : ")
        if want in ["+" , "-" , "*" , ":" , "**"] :
            break
        else : 
            print(Back.RED)
            print(Fore.BLACK)
            print("Вы ввели не правильный знак операции ")
        
    while True :        #проверка на число
        try :
            print(Fore.CYAN)
            b = int(input("Введите второе число : "))
            break
        except ValueError :
            print(Back.RED)
            print(Fore.BLACK)
            print("Вы ввели не число ")
            
    if want == "+" :
        c = a + b 
    elif want == "-" :
        c = a - b 
    elif want == "*" :
        c = a * b
    elif want == ":" :
        c = a / b
    elif want == "**" :
        c = a ** b
        
    print(Fore.LIGHTMAGENTA_EX)
    print(f"Результат : {c}")
    print(Fore.LIGHTYELLOW_EX)
    
    while True :
        go = input(str("Хотите продолжить ? (yes / no ) : ")).strip().lower()
        if go in ["yes" , "no"]:
            break
    if go == "yes" :
        print("Продолжим !")
        time.sleep(2)
    elif go == "no" :
        print(Back.BLUE)
        print(Fore.BLACK)
        print("До свидания !")
        exit()