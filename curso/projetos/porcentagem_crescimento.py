
bacterias_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9] # Lista que armazena o número de bactérias em cada dia


percentual_crescimento = [] # Lista vazia que vai guardar o percentual de crescimento entre os dias


for i in range(1, len(bacterias_dia)): # Loop que percorre os dias (começa no segundo dia, índice 1)
    
    crescimento = 100 * (bacterias_dia[i] - bacterias_dia[i - 1]) / bacterias_dia[i - 1] # Calcula o percentual de crescimento usando a fórmula:


    
    
    percentual_crescimento.append(crescimento)   # Adiciona o resultado calculado na lista percentual_crescimento


    print("Percentual de crescimento por dia: ", percentual_crescimento) # Exibe a lista com todos os percentuais de crescimento calculados