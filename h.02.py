################################################ - VARIAVEIS - #########################################################

print('Colocar ,as entradas, separadas por espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis.
saida = []  # Saidas.
lista_verdade = []  # Tabela verdade nao invertida.
lista2_verdade = []  # Tabela verdade Invertida (Completa).
Grupos = []
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1.
Contagem = 0 # contagem dos grupos
Soma_Dos_Grupos = 0
Saidas_Validas =[]
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

########################################## - QUAIS SAIDAS SÃO VALIDAS - ################################################

for h1 in range(Tabela_Verdade):
    if saida[h1] == '1':
        Saidas_Validas.append(lista2_verdade[h1])
print('SAIDA',Saidas_Validas)

############################################ - MONTAGEM DE GRUPOS - ####################################################
reset = 0
for j1 in range (len(Saidas_Validas)):# Indentificando os grupos
    modificador = Saidas_Validas[j1]
    for j2 in range (len(entradas)):
        Soma_Dos_Grupos += modificador[j2]
    print(Soma_Dos_Grupos)
    if Soma_Dos_Grupos > reset:
        reset = Soma_Dos_Grupos
    Soma_Dos_Grupos = 0
for j3 in range(reset):
    Sub_Grupos = []
    for j4 in range(len(Saidas_Validas)):
        modificador = Saidas_Validas[j4]
        for j5 in range(len(entradas)):
            Soma_Dos_Grupos += modificador[j5]
        if Soma_Dos_Grupos - 1 == j3:
            Sub_Grupos.append(modificador)
        print(Sub_Grupos)
        Soma_Dos_Grupos = 0
    Grupos.append(Sub_Grupos)
    print(Grupos)
print(Grupos[0])



