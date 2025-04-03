
gabarito = ["A", "B", "B", "D", "C", "A", "D", "C", "A"] # Lista contendo o gabarito correto das questões


respostas = ["B", "C", "B", "A", "C", "A", "D", "A", "C"] # Lista contendo as respostas do aluno

nota_aluno = 0 
# Variável para armazenar a nota final do aluno

# Loop para comparar as respostas do aluno com o gabarito
for i in range(0, len(gabarito)): # Itera de 0 até o tamanho da lista 'gabarito'
    if respostas[i] == gabarito[i]: # Verifica se a resposta do aluno está correta
        nota_aluno += 1 # Incrementa a nota do aluno para cada resposta correta
        

print(f"Sua nota na prova é {nota_aluno}!")