
numero = int(input("Escolha um numero para ver a tabuada: "))  
tabuada = 0  

# Cria um loop que vai de 0 até 10 (o range inclui o 0 e o 10, perfeito para a tabuada)
for tabuada in range(0, 11):  
    # Exibe a operação (multiplicação) no formato: numero x tabuada = resultado
    print(f"{numero} x {tabuada} = {numero * tabuada}")  