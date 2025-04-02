
cadastro = {
            'matricula': 2000168933,
            'dia_cadastro': 25,
            'mes_cadastro': 10,          # Dicionario
            'turma': '2E'
              }

print(cadastro['matricula']) # Imprime somente a matricula.

cadastro['turma'] = '2F' # Atualizou o valor da 'turma'.
print(cadastro)

cadastro['modalidade'] = 'EAD' # Adicionou outros dados para o dicionario
print(cadastro)

cadastro.pop('turma') # Remove um dado especifico do dicionario.
print(cadastro)

print(cadastro.items()) # Retorna uma lista de pares chave-valor do dicionário.

print(cadastro.keys()) # Retorna uma lista das chaves do dicionário.

print(cadastro.values()) # Retorna uma lista dos valores do dicionário.





 


