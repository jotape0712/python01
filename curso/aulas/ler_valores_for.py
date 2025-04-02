
cadastro = {
            'matricula': 2000168933,  
            'dia_cadastro': 25,       
            'mes_cadastro': 10,       
            'turma': '2E'             
              }

# Inicia um loop "for" que itera sobre cada par chave-valor do dicionário
for chaves, valores in cadastro.items():  # "items()" retorna as chaves e os valores do dicionário
    print(chaves, valores)  # Imprime a chave e o valor correspondente em cada iteração