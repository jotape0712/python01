caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']



caes.insert(1, 'Golden Retriever') # Insere o elemento em uma determinada posição da lista.
print(caes)

print(caes.pop(1)) # Remove o elemento de uma determinada posição da lista e retorna o elemento excluido.
print(caes)

print(caes.index('Pastor Alemão'))  # Retorna o índice de um elemento específico na lista.

caes.sort() # Organiza os elementos da lista em ordem crescente ou decrescente. Caso sejam palavras, a ordem é dada por sequência alfabética ou inversa à ela.
print(caes)

