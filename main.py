num  =  int(input("Dígite um número inteiro:"))
if num < 0 or num == 0:
    print("Número inválido")
else:
    primo = True
    for i in range(2,num):
        if num % i == 0:
            print("Não primo")
            primo = False

    
            

