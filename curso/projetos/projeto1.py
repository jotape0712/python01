
print("Escolha uma operação:") # Mostra as opções ao usuario.
print("1. Par ou impar")
print("2. Positivo ou negativo")
print("3. inteiro ou decimal")

operacao = input("Escolha uma operação (1, 2, 3): ") # Pede para o usuario escolher qual operação ira realizar antes de solicitar os dados.


if operacao == "1": # Se o usuario escolher a opção 1, executa o codigo abaixo
    numero1 = int(input("Digite um numero: "))
    if numero1 % 2 == 0:
        print(f"O numero {numero1} é par!")
    else:
        print(f"O numero {numero1} é impar!")

if operacao == "2": # Se o usuario escolher a opção 2, executa o codigo abaixo
    numero1 = float(input("Digite um numero: "))
    if numero1 >= 1:
        print("Esse numero é positivo!")
    elif numero1 <= -1:
        print("Esse numero é negativo!")
    elif numero1 == 0:
        print("0 é neutro")

if operacao == "3": # Se o usuario escolher a opção 3, executa o codigo abaixo
    numero1 = input("Digite um numero: ")
    if "." in numero1: # Verifica se existe um ponto dentro do dado inserido pelo usuario, se tiver quer dizer que é um numero decimal.
         print("Esse numero é decimal!")
    elif not "." in numero1:
         print("Esse numero é inteiro!")
    else:
        print("valor invalido!")

    
    