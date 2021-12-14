"""
Exercício Python 003:
Crie um programa que leia números,
adicione-os a uma lista e mostre a lista em ordem crescente e a soma entre eles.
"""
from time import sleep
from itertools import accumulate
from uteis import numera, abre, divide, encerra, words


titulo = 'SOMANDO VALORES LIDOS PELO TECLADO'

abre(titulo, 60)

numeros = list()
soma = 0
segue = ' '

while True:

    segue = ' '

    num = numera('Digite um número:     ')
    numeros.append(num)
    soma = accumulate(numeros)

    print()

    numeros.sort()
    print(f'As parcelas apresentadas até aqui são: \n{numeros}')
    print(f'A soma das parcelas até aqui apresentadas é {list(soma)[-1]}')

    divide(60)

    while segue not in 'SN':

        segue = words('Mais parcelas? [S/N] ').strip().upper()


    if segue in 'N':


        encerra(60, 'Encerrando...')
        print('visit on github: leonardinobre')

        sleep(5)

        break
