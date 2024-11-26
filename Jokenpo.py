#Crie o famoso jogo Jokenpo

#Entendo as regras

# Cada jogador deve escolher um dos três símbolos, pedra, papel ou tesoura
#Os jogadores devem esticar a mão simultaneamente para mostrar o símbolo escolhido

# Na qual
# Pedra ganha da tesoura
# Tesoura ganha do papel
# Papel empata com papel e ganha da pedra ##

import random
from time import sleep

#Entrada do usuário
            
print('''Escolha um número conforme abaixo:
[1] - Pedra
[2] - Tesoura
[3] - Papel''')
print('-=-' * 20)

escolhido = int (input('Escolha um valor para iniciar o jogo:'))
print('JO')            
sleep(1)
print('KEN')
sleep(1)
print('POOOO!!')
sleep(1)
print('-=-' * 20)

#Valor aleatório escolhido
computador = random.choice([1,2,3])

#Nomeando escolhas
opcoes = {1: 'Pedra', 2: 'Tesoura', 3: 'Papel'}
print(f'Você esolheu: {opcoes[escolhido]}')
print('-=-' * 20)
print(f'O computador escolheu: {opcoes[computador]}')
print('-=-' * 20)


#Determinando o vencedor

if escolhido == computador:
    print('O jogo empatou')

elif (escolhido == 1 and computador ==2) or (escolhido == 2 and computador ==3 ) or (escolhido == 3 and computador ==1):
    print('Voce venceu ! Parabéns,Fera')
    print('-=-' * 20)
    
else:
    print('Você perdeu ! Mas não desista guerreiro')
    print('-=-' * 20)

print('Fim do programa, HZ')
print('-=-' * 20)



