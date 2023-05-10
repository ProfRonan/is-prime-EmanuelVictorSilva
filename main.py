num  =  int(input("Dígite um número inteiro:"))
if num < 0 or num == 0:
    print("Número inválido")
else:
    a = 0
    for i in range(2,num  ):
        if num % i == 0:
            a = a + 1
    if a > 0 or num == 1:
        print("Não primo")

    else:
        print("Primo")
            

