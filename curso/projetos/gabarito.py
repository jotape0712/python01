
gabarito = ["A", "B", "B", "D", "C", "A", "D", "C", "A"]

respostas = ["B", "C", "B", "A", "C", "A", "D", "A", "C"]

nota_aluno = 0

for i in range(0, len(gabarito)):
    if respostas[i] == gabarito[i]:
        nota_aluno+=1
    
        
print(f"Sua nota na prova é {nota_aluno}!")

    


