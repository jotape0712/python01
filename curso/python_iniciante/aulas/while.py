contador = 1  # Inicializa a variável 'contador' com valor 1. Isso será usado para controlar quantas vezes o loop roda.
while contador <= 3:  # O loop continuará enquanto 'contador' for menor ou igual a 3.

    nome_aluno = input("Digite seu nome: ")  
    nota_1 = float(input('Digite a 1° nota: '))  
    nota_2 = float(input('Digite a 2° nota: '))  

    print(f'Média do aluno {nome_aluno} é: {(nota_1+nota_2)/2}')  

    contador = contador + 1  # Adiciona 1 ao valor do 'contador' a cada repetição do loop.
    # Outra forma de escrever isso seria: contador += 1 (é só uma forma mais curta de fazer o mesmo).