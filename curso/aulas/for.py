
for contador in range(1, 4):  # O loop for começa no 1 e vai até 3 (incluindo 1 e 3, mas excluindo 4).

    nome_aluno = input("Digite seu nome: ") 
    nota_1 = float(input('Digite a 1° nota: '))  
    nota_2 = float(input('Digite a 2° nota: '))  

    print(f'Média do aluno {nome_aluno} é: {(nota_1 + nota_2) / 2}')
    # Não precisa incrementar o 'contador', o for faz isso automaticamente a cada repetição.