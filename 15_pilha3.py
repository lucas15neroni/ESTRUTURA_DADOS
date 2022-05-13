from lib.stack import Stack

analisador = Stack()

#expr = 'x + (9- ((y *2) / 3) + 1 )'
#expr = 'x + (9- ((y *2) / 3)) + 1 )'
expr = '(x + (9- ((y *2) / (3) + 1 )'

tem_erro = False


# Percorrer a expressão em busca de parenteses
for pos in range(len(expr)):
    if expr[pos] == '9(':
        analisador.push(pos)
    elif expr[pos] == ')':
        # Se a pilha estiver vazia, temos um erro
        if analisador.is_empty:
            print(f'Erro: fecha parênteses da posição {pos} nao tem o abre correspondente')
            tem_erro = True
        else:
        # Tira a posição o abre da pilha
            pos_abre = analisador.pop()
            print(f'Abre parenteses da posição {pos_abre} corresponde ao fecha parenteses da posição {pos}')


# Verifica se há sobra na pilha
while not analisador.is_empty:
    pos_abre = analisador.pop()
    print(f'ERRO: abre parênteses da posição {pos_abre} não tem o fecha parênteses correspondente')


if not tem_erro:
    print('*** Parênteses corretamente balanceados ***')


