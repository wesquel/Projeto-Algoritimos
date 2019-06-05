print('Colocar as Entradas Separadas por Espaço.')
entradas = input('Entradas: ').split(' ')  # Variaveis
saidas = []
lista_verdade = []
print(entradas)
Tabela_Verdade = 2 ** len(entradas)  # O Numero de 0 ou 1 que vai ter por entrada.
Repeticao = 2 ** len(entradas)  # 0 ou 1
for x in range(len(entradas)):  # For para as entradas.
    Repeticao = int(Repeticao/2)
    Contador = 0
    lista2 = []
    while Contador != Tabela_Verdade: # Montando a tabela.
        for z in range(Repeticao):
            lista2.append(0)
            Contador += 1
        for g in range(Repeticao):
            lista2.append(1)
            Contador += 1
    lista_verdade.append(lista2)
print(lista_verdade)
Numero_de_Saidas = int(input('Número de Saídas: '))
for o in range(Numero_de_Saidas):
    n1 = input()
    saidas.append(n1)
print(saidas)
