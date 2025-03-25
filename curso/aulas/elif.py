media = float(input('Digite a média: '))  

if media >= 6.0:
  print('Aprovado(a)')
elif 6.0 > media >= 4.0: # elif serve como um segundo if
  print('Recuperação')
else:
  print('Reprovado(a)')