print('-='* 20)
print('\033[7mVamos jogar Pedra, Papel, Tesoura!\033[m')
print('-='* 20)
jog = int(input('''Escolha:
[0] Pedra
[1] Papel
[2] Tesoura
Qual será sua jogada? '''))
print('-='* 20)
from random import randint
lista = ['Pedra','Papel','Tesoura']
pc = randint (0,2)

print('Vamos lá...')
print('-='* 20)
from time import sleep
print('\033[31mPEDRA\033[m')
sleep (1)
print('\033[32mPAPEL\033[m')
sleep (1)
print('\033[33mTESOURA\033[m')

print('-='* 20)
print(f'Você escolheu \033[1m{lista[jog]}\033[m')
print(f'Eu escolhi \033[1m{lista[pc]}\033[m')
print('-='* 20)

#PC JOGA PEDRA
if pc == 0:
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Você ganhou!')
    elif jog == 2:
        print('Você perdeu!')

#PC JOGA PAPEL
elif pc == 1:
    if jog == 0:
        print('Você perdeu!')
    elif jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Você ganhou!')

#PC JOGA TESOURA
elif pc == 2:
    if jog == 0:
        print('Você ganhou!')
    elif jog == 1:
        print('Você perdeu!')
    elif jog == 2:
        print('Empate!')