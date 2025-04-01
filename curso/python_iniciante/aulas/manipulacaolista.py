

lista = ["João Pedro", 9.5, 9.0, 6.8, True]
media = (lista[1] + lista[2] + lista[3]) / 3

print(len(lista)) # len() serve para contar quantos elementos estão inseridos na lista.

print(lista[1:4]) # Seleciona um sobconjunto dentro da lista, neste caso selecionando somente os elementos dentro da []. Índice do primeiro elemento sera incluído na partição e fim e o índice do ultimo elemento sera excluído da partição, ficando somente 1 e 2.

print(lista[:3]) # Seleciona todos os elementos até o indice 3, ignorando o resto.

print(lista[3:]) # Seleciona todos os elementos a partir do indice 3, ignorando o resto.

print(lista[:]) # Retorna todos os dados da lista.


lista.append(media)  # Adiciona outro elemento no final da lista.
print(lista)  

lista.extend([10.0,8.0,9.0]) # Adiciona varios elementos no final da lista, com APPEND só podemos adicionar um.
print(lista)   

lista.remove(10.0) # Remove o elemento desejado.
print(lista)
