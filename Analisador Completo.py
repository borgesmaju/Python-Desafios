soma = 0
maior = 0
menor = 0
maiormasc = 0
nomevelho = ''
totmulher20 = 0

for p in range (1,5):
    print('-=' * 5, f'{p}º PESSOA','-=' * 5)
    nome = str(input(f'\033[1mNome: \033[m')).strip()
    idade = int(input(f'\033[1mIdade: \033[m'))
    sexo = str(input(f'\033[1mSexo (M/F/O): \033[m')).upper().strip()

    soma = soma + idade
    media = soma / 4

# HOMEM MAIS VELHO
    if p == 1 and sexo == 'M':
        maiormasc = idade
        nomevelho = nome
    if idade > maiormasc and sexo == 'M':
        maiormasc = idade
        nomevelho = nome

# QUANTIDADE DE MULHERES SUB20
    if sexo == 'F' and idade < 20:
     totmulher20 += 1

print('Analisando...')
from time import sleep
sleep (1)
print(f'''A média das idades do grupo é {media}.
O nome do homem mais velho é {nomevelho}.
A quantidade de mulheres com menos de 20 anos é {totmulher20}''')