print('Colocar as Entradas Separadas por Espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis
saidas = []  # saidas
lista_verdade = []  # Tabela verdade nao invertida
lista2_verdade = []  # Tabela verda Invertida (Completa)
print(entradas)
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1
for x in range(len(entradas)):  # For para as entradas.
    Repeticao = int(Repeticao / 2)
    Contador = 0  # Contador para o while
    lista2 = []  # Lista de repetição
    while Contador != Tabela_Verdade:  # Montando a tabela.
        for z in range(Repeticao):
            lista2.append(0)
            Contador += 1
        for g in range(Repeticao):
            lista2.append(1)
            Contador += 1
    lista_verdade.append(lista2)
for t in range(Tabela_Verdade): # for pra inversao da tabela
    lista2 = []
    for t1 in range(len(entradas)):
        a = lista_verdade[t1]
        lista2.append(a[t])
    lista2_verdade.append(lista2)
for t3 in range(Tabela_Verdade):
    print(lista2_verdade[t3])
Numero_de_Saidas = int(input('Número de Saídas: '))
for o in range(Numero_de_Saidas):
    n1 = input()
    saidas.append(n1)
print(saidas)
//232
