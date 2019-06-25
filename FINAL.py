from copy import deepcopy

print('Colocar, as entradas, separadas por espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis.

################################################ - VARIAVEIS - #########################################################
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1.

saida = []  # Saidas.
lista_verdade = []  # Tabela verdade nao invertida
lista2_verdade = []  # Tabela verdade Invertida (Completa).
Grupos = []  # Divisão
Saidas_Validas = []  # Saidas que Possuem 1
Grupo_de_Simplificacão = []  # Grupo de Simplificaçao/ Reset
Total = []  # Final dos Grupos
gruposempar = []  # Grupos que nao Possuem Par
Usados = []  # Elementos do Grupos Usados
GrupoInicial = []  # Reset dos Grupos
Grupos_Isolados = []  # Grupos sem par Separados

Contagem = 0  # contagem dos grupos
soma01 = 0  # Varivael de Soma para os reset's
soma0 = 0  # Varivael de Soma para os reset's
soma1 = 0  # Varivael de Soma para os reset's
soma2 = 0  # Varivael de Soma para os reset's
reset = 0  # Varivael de Soma para os reset's
Soma_Dos_Grupos = 0  # Varivael de Soma para os reset's
somaprint = 0  # Varivael de Soma para os reset's

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

for t in range(Tabela_Verdade):  # For pra inversão da tabela.
    lista2 = []
    for t1 in range(len(entradas)):
        modificador = lista_verdade[t1]
        lista2.append(modificador[t])
    lista2_verdade.append(lista2)

################################################## - SAIDA - ###########################################################
check = True
print('Saída Separada por espaços, Sua saída deve ter pelo menos', Tabela_Verdade, 'Termos.')
while (len(saida) > Tabela_Verdade) or (len(saida) < Tabela_Verdade) or (check == False):  # Saida.
    check = True
    saida = input().split(' ')
    for d0 in range(len(saida)):
        if (saida[d0] != '0') and (saida[d0] != '1'):
            check = False
    if check == False:
        print('A saída deve ser composta apenas com 0 ou 1, separados por espaços.')
    elif len(saida) > Tabela_Verdade:
        print('O número de termos na saída possui', len(saida) - Tabela_Verdade, 'a mais que o permitido.')
    elif len(saida) < Tabela_Verdade:
        print('O número de termos na saída possui', Tabela_Verdade - len(saida), 'a menos que o permitido.')

########################################## - QUAIS SAIDAS SÃO VALIDAS - ################################################

for h1 in range(Tabela_Verdade):
    if saida[h1] == '1':
        Saidas_Validas.append(lista2_verdade[h1])

########################################## - SAIDA SEM SIMPLIFICAÇÃO - #################################################
check5 = True
print('Saida: ', end='')
for k0 in range(len(entradas)):
    if k0 == 0:
        print('f{' + entradas[k0], end='')
    elif k0 == (len(entradas)) - 1:
        print(',' + entradas[k0] + '} = ', end='')
    else:
        print(',' + entradas[k0], end='')

for k2 in range(len(saida)):
    somaprint += int(saida[k2])
somaentradas = 0
if len(entradas) == 1:
    print('} =',end=' ')
    check5 = False
    for d3 in range(len(saida)):
        if saida[d3] == '1':
            somaentradas += 1
    if somaentradas == 2:
        print('1')
    elif somaentradas == 1:
        for d4 in range(len(entradas)):
            if saida[d4] == '1':
                print(entradas[0]+"'")
            elif saida[d4] == '0':
                print(entradas[0])
    elif somaentradas == 0:
        print('0')

elif somaprint == (len(saida)):
    print('1')
    check5 = False
elif somaprint == 0:
    print('0')
    check5 = False

    check5 = False
if check5 == True:
    for k in range(len(Saidas_Validas)):
        modificador = Saidas_Validas[k]
        for k1 in range(len(entradas)):
            if modificador[k1] == 0:
                if k1 == len(entradas) - 1:
                    if k == len(Saidas_Validas) - 1:
                        print(entradas[k1] + "'")
                    else:
                        print(entradas[k1] + "'", end=' + ')
                else:
                    print(entradas[k1] + "'", end='')
            elif modificador[k1] == 1:
                if k1 == len(entradas) - 1:
                    if k == len(Saidas_Validas) - 1:
                        print(entradas[k1])
                    else:
                        print(entradas[k1], end=' + ')
                else:
                    print(entradas[k1], end='')

if somaprint == 1:
    check5 = False

############################################ - MONTAGEM DE GRUPOS - ####################################################

for j1 in range(len(Saidas_Validas)):  # Indentificando os grupos
    modificador = Saidas_Validas[j1]
    for j2 in range(len(entradas)):
        Soma_Dos_Grupos += modificador[j2]
    if Soma_Dos_Grupos > reset:
        reset = Soma_Dos_Grupos
    Soma_Dos_Grupos = 0
for j3 in range(reset + 1):  # Adicionando
    Sub_Grupos = []
    for j4 in range(len(Saidas_Validas)):
        modificador = Saidas_Validas[j4]
        for j5 in range(len(entradas)):
            Soma_Dos_Grupos += modificador[j5]
        if Soma_Dos_Grupos == j3:
            if len(modificador) != 0:
                Sub_Grupos.append(modificador)
        Soma_Dos_Grupos = 0
    if len(Sub_Grupos) != 0:
        Grupos.append(Sub_Grupos)

################################################ - SIMPLIFICAÇÃO - #####################################################

while True:
    if soma01 != 0:
        Grupos = GrupoInicial
    for l0 in range(len(Grupos)):  # dividindo os grupos
        modificador = Grupos[l0]  # GRUPOS
        if soma01 != 0:
            if len(Grupo_de_Simplificacão) != 0:
                GrupoInicial.append(Grupo_de_Simplificacão)
            Grupo_de_Simplificacão = []
            soma2 = 0

        for l1 in range(len(modificador)):
            modificador_1 = modificador[l1]  # SUB
            if l0 < len(Grupos) - 1:
                for l2 in range(len(Grupos[l0 + 1])):
                    modificador_2 = Grupos[l0 + 1]
                    modificador_3 = modificador_2[l2]
                    for l3 in range(len(entradas)):
                        if modificador_1[l3] != modificador_3[l3]:
                            soma0 += 1
                            soma1 = l3
                    if soma0 == 1:
                        Grupo_de_Simplificacão.append(deepcopy(modificador_1))
                        Usados.append(deepcopy(modificador_3))
                        Usados.append(deepcopy(modificador_1))
                        Grupo_de_Simplificacão[soma2][soma1] = '-'
                        soma2 += 1
                    elif soma0 > 1:
                        gruposempar.append(modificador_1)
                        gruposempar.append(modificador_3)
                    soma0 = 0
        soma01 = 1
    if GrupoInicial == Grupos:
        break

############################################# - SEPARAÇÃO DOS GRUPOS - #################################################

for g0 in range(len(gruposempar)):  # Separando que nao Tem Par.
    Check_Grupos = False
    Check_Isolados = False
    for g1 in range(len(Usados)):
        if gruposempar[g0] == Usados[g1]:
            Check_Grupos = True
    for g2 in range(len(Grupos_Isolados)):
        if gruposempar[g0] == Grupos_Isolados[g2]:
            Check_Isolados = True
    if (Check_Grupos == False) and (Check_Isolados == False):
        Grupos_Isolados.append(gruposempar[g0])

for e0 in range(len(GrupoInicial)):  # Separando os Grupos
    modificador = GrupoInicial[e0]
    for e1 in range(len(modificador)):
        modificador_1 = modificador[e1]
        Check_Grupos = False
        for e2 in range(len(gruposempar)):
            if modificador_1 == gruposempar[e2]:
                Check_Grupos = True
        for e3 in range(len(Total)):
            if modificador_1 == Total[e3]:
                Check_Grupos = True
        if Check_Grupos == False:
            Total.append(modificador_1)
for e4 in range(len(Grupos_Isolados)):
    if len(Grupos_Isolados[e4]) != 0:
        Total.append(Grupos_Isolados[e4])

################################################ - SAIDA COM SIMPLIFICAÇÃO - ###########################################

if len(Total) == 0:
    check5 = False
if check5 == True:
    print('Saida Simplificada: ', end='')
    for k5 in range(len(entradas)):
        if k5 == 0:
            print('f{' + entradas[k5], end='')
        elif k5 == (len(entradas)) - 1:
            print(',' + entradas[k5] + '} = ', end='')
        else:
            print(',' + entradas[k5], end='')
    for k6 in range(len(Total)):
        modificador = Total[k6]
        for k7 in range(len(entradas)):
            if modificador[k7] == 0:
                if k7 == len(entradas) - 1:
                    if k6 == len(Total) - 1:
                        print(entradas[k7] + "'")
                    else:
                        print(entradas[k7] + "'", end=' + ')
                else:
                    print(entradas[k7] + "'", end='')
            elif modificador[k7] == 1:
                if k7 == len(entradas) - 1:
                    if k6 == len(Total) - 1:
                        print(entradas[k7])
                    else:
                        print(entradas[k7], end=' + ')
                else:
                    print(entradas[k7], end='')
            elif modificador[k7] == "-":
                if k7 == len(entradas) - 1:
                    if k6 == len(Total) - 1:
                        print(end='')
                    else:
                        print(end=' + ')
                else:
                    print(end='')
