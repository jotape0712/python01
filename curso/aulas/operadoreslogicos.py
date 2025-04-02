t1 = t2 = True   # Da o mesmo valor para duas variaveis
f1 = f2 = False 

if t1 and t2:  # and deve funcionar quando tiver dois valores true
  print('expressão verdadeira')  
else:
  print('expressão falsa')


if t1 or f2:  # or deve funcionar quando tiver pelo menos um valor true
  print('expressão verdadeira')  
else:
  print('expressão falsa')

if not t1:  # not deve funcionar invertendo o resultado booleano, transformando o true em false
  print('expressão verdadeira')
else:
  print('expressão falsa')