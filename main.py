import random


def adivinha_o_numero():
    # Jogo  1 - Advinhe o número
    tentativasJogador: int = 0
    print('Oi. Qual o seu nome? ')
    nome = input()
    numero: int = random.randint(1, 20);
    print('Ok, {0}, eu estou pensando em um número entre 1 e 20'.format(nome))
    while tentativasJogador < 6:
        print('Chute um número... ')
        chute = input()
        chute: int = int(chute)

        tentativasJogador = tentativasJogador + 1

        if chute < numero:
            print('Seu palpite foi menor que o número')
        elif chute > numero:
            print('Seu palpite foi maior que o número')
        else:
            break
    if chute == numero:
        tentativas = str(tentativasJogador)
        if tentativasJogador > 1:
            print('Muito bem, {0}! Você descobriu meu número em {1} tentativas'.format(nome, tentativas))
        else:
            print('Muito bem, {0}! Você descobriu meu número em apenas {1} tentativa'.format(nome, tentativas))
    else:
        numero = str(numero)
        print('Perdeu. O número que pensei foi ' + numero)

def maior_de_tres():
    print('Programa para descobrir o maior de 3 números.')
    n1 = int(input('Entre com o primeiro número '))
    n2 = int(input('Entre com o segundo número '))
    n3 = int(input('Entre com o terceiro número '))
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    print('O maior número é ' + str(maior))

def sexo():
    letra = input('Qual seu sexo? (M)asculino ou (F)eminino? ')
    if letra == 'M' or letra == 'm':
        print('Masculino')
    elif letra == 'F' or letra == 'f':
        print('Feminino')
    else:
        print('Sexo inválido')

#adivinha_o_numero()
#maior_de_tres()
#sexo()



