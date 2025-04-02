
numero1 = int(input("Digite um numero inteiro: "))  

numero2 = int(input("Digite outro numero inteiro: "))  

# Verifica se o primeiro número é menor que o segundo
if numero1 < numero2:

    # Usa o loop for para imprimir todos os números inteiros entre 'numero1' e 'numero2'
    # Começa de 'numero1 + 1' (ou seja, depois do primeiro número) e vai até 'numero2 - 1' (o ultimo antes do segundo numero)
    for i in range(numero1 + 1, numero2):  
        print(i)  # Mostra cada número entre os valores no terminal

# Verifica se o segundo número é menor que o primeiro
elif numero2 < numero1:  
    # Faz a mesma coisa que o caso acima, mas inverte a ordem
    # Começa de 'numero2 + 1' e vai até 'numero1 - 1'
    for i in range(numero2 + 1, numero1):  
        print(i)  # Mostra os números entre os valores no terminal

else:  
    print("Não há numeros inteiros entre esses dois valores!")  
  