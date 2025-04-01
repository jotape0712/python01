
while True:
    numero = int(input('Digite um número: '))
    
    if numero < 2:
        print('Digite um numero maior ou igual a 2!')  
    else:
        primo = True
        for i in range(2, numero):  
            if numero % i == 0:  
                primo = False
                break
        if primo:
            print('Primo')
        else:
            print('Não primo')