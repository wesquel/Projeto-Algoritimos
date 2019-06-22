################################################ - VARIAVEIS - #########################################################

from copy import deepcopy
print('Colocar ,as entradas, separadas por espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis.
saida = []  # Saidas.
lista_verdade = []  # Tabela verdade nao invertida.
lista2_verdade = []  # Tabela verdade Invertida (Completa).
Grupos = []
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1.
Contagem = 0  # contagem dos grupos
Soma_Dos_Grupos = 0
Saidas_Validas = []
numero = []
Grupo_de_Simplificacão = []
Total = []

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

for t in range(Tabela_Verdade):  # For pra inversão da tabela.
    lista2 = []
    for t1 in range(len(entradas)):
        modificador = lista_verdade[t1]
        lista2.append(modificador[t])
    lista2_verdade.append(lista2)
for t3 in range(Tabela_Verdade):
    print(lista2_verdade[t3])

################################################## - SAIDA - ###########################################################

print('Saida Separada por espaços, Sua saida deve ter pelo menos', Tabela_Verdade, 'Termos')
while (len(saida) > Tabela_Verdade) or (len(saida) < Tabela_Verdade):  # Saida.
    saida = input().split(' ')
    if len(saida) > Tabela_Verdade:
        print('O numero de termos na saida possui',len(saida) - Tabela_Verdade,'a mais que o permitido.')
    elif len(saida) < Tabela_Verdade:
        print('O numero de termos na saida possui',Tabela_Verdade - len(saida), 'a menos que o permitido.')
print('SAIDAS', saida)
print('TABELA VERDADE 2', lista2_verdade)

########################################## - QUAIS SAIDAS SÃO VALIDAS - ################################################

for h1 in range(Tabela_Verdade):
    if saida[h1] == '1':
        Saidas_Validas.append(lista2_verdade[h1])
        numero.append(h1)
print('SAIDA VALIDAS', Saidas_Validas, '\n')
print('NUMERO', numero, '\n')

########################################## - SAIDA SEM SIMPLIFICAÇÃO - #################################################

print('SAIDA SEM A SIMPLIFICAÇÃO: ', end='')
for k0 in range(len(entradas)):
    if k0 == 0:
        print('f{' + entradas[k0], end='')
    elif k0 == (len(entradas)) - 1:
        print(',' + entradas[k0] + '} = ', end='')
    else:
        print(',' + entradas[k0], end='')
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

############################################ - MONTAGEM DE GRUPOS - ####################################################

reset = 0
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
    print(Grupos)
print(len(Grupos))

################################################ - SIMPLIFICAÇÃO - #####################################################
GrupoInicial= []
soma01 = 0
soma0 = 0
soma1 = 0
soma2 = 0
test = 0
gruposempar = []
Usados = []
while True :
    if soma01 != 0:
        Grupos = GrupoInicial
        test = 1
    for l0 in range(len(Grupos)):  # dividindo os grupos
        modificador = Grupos[l0]  # GRUPOS
        print('MODIFICADOR',modificador)
        print('SubGrupo:',l0, modificador)
        print(l0,len(Grupos))
        if soma01 != 0:
            if len(Grupo_de_Simplificacão) != 0:
                GrupoInicial.append(Grupo_de_Simplificacão)
            Grupo_de_Simplificacão = []
            soma2 = 0

        for l1 in range(len(modificador)):
            modificador_1 = modificador[l1]  # SUB
            print('MODIFICADOR 1 ',modificador_1)
            print(' SELEÇAO:', l0, modificador_1, l1)
            if l0 < len(Grupos) - 1:
                for l2 in range (len(Grupos[l0+1])):
                    modificador_2 = Grupos[l0+1]
                    modificador_3 = modificador_2[l2]
                    for l3 in range(len(entradas)):
                        if modificador_1[l3] != modificador_3[l3]:
                            soma0 = soma0 + 1
                            soma1 = l3
                    if soma0 == 1:
                        print('grupos somados',modificador_1, modificador_3)
                        Grupo_de_Simplificacão.append(deepcopy(modificador_1))
                        Usados.append(deepcopy(modificador_3))
                        Usados.append(deepcopy(modificador_1))
                        Grupo_de_Simplificacão[soma2][soma1] = '-'
                        soma2 = soma2 + 1
                        print('sdasd',modificador_1)
                        print('Grupo de Simplificaçao',Grupo_de_Simplificacão)
                    elif soma0 > 1:
                        gruposempar.append(modificador_1)
                        gruposempar.append(modificador_3)
                    soma0 = 0
        soma01 = 1
    if GrupoInicial == Grupos:
        break


print('Grupo de Simplificação',Grupo_de_Simplificacão)
print('Grupo Inicial',GrupoInicial)
print('Grupos',Grupos)
print('Usados',Usados)
print('grupo sem par',gruposempar)
Grupos_Isolados = []

for g0 in range(len(gruposempar)): # Separando que nao Tem Par.
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

print('Grupos Isolados: ',Grupos_Isolados)

for e0 in range(len(GrupoInicial)): ### Separando os Grupos
    modificador = GrupoInicial[e0]
    for e1 in range(len(modificador)):
        modificador_1 = modificador[e1]
        Check_Grupos = False
        for e2 in range (len(gruposempar)):
            if modificador_1 == gruposempar[e2]:
                Check_Grupos = True
        for e3 in range(len(Total)):
            if modificador_1 == Total[e3]:
                Check_Grupos = True
        if Check_Grupos == False:
            Total.append(modificador_1)
print(Total)
