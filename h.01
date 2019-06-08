################################################ - VARIAVEIS - #########################################################

print('Colocar ,as entradas, separadas por espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis.
saida = []  # Saidas.
lista_verdade = []  # Tabela verdade nao invertida.
lista2_verdade = []  # Tabela verdade Invertida (Completa).
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1.
Contagem = 0 # contagem dos grupos
seila =[]
print(entradas)

######################################## - MONTAGEM DA TABELA VERDADE - ################################################

for x in range(len(entradas)):  # For para as entradas.
    Repeticao = int(Repeticao / 2)
    Contador = 0  # Contador para o while.
    lista2 = []  # Lista de repetição.
    while Contador != Tabela_Verdade:  # Montando a tabela.
        for z in range(Repeticao):
            lista2.append(0)
            Contador += 1
        for g in range(Repeticao):
            lista2.append(1)
            Contador += 1
    lista_verdade.append(lista2)

################################################# - INVERSÃO - #########################################################

for t in range(Tabela_Verdade): # For pra inversão da tabela.
    lista2 = []
    for t1 in range(len(entradas)):
        modificador = lista_verdade[t1]
        lista2.append(modificador[t])
    lista2_verdade.append(lista2)
for t3 in range(Tabela_Verdade):
    print(lista2_verdade[t3])

################################################## - SAIDA - ###########################################################

print('Saida Separade por espaço, Sua saida deve ter pelo menos',Tabela_Verdade,'Termos')
while (len(saida) > Tabela_Verdade) or (len(saida) < Tabela_Verdade): # Saida.
    saida = input().split(' ')
    if len(saida) > Tabela_Verdade:
        print('O Numero de Termos na Saida é maior que o permitido.')
    elif len(saida) < Tabela_Verdade:
        print('O Numero de Termos na Saida é menor que o permitido.')
print(saida)
print(lista2_verdade)

############################################ - MONTAGEM DE GRUPOS - ####################################################

for o1 in range(len(entradas)): # verificador de uns :).
    modificador = lista_verdade[o1]
    Contador = 0
    for o2 in range(Tabela_Verdade):
        Contador += 1
        if Contador <= len(entradas):
            Contagem = Contagem + modificador[o2]
        print('Contagem',Contagem)
        print(modificador[o2])
        print(Contador)

########################################## - QUAIS SAIDAS SÃO VALIDAS - ################################################

for h1 in range(Tabela_Verdade):
    if saida[h1] == '1':
        seila.append(h1)
print(seila)
