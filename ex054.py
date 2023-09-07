""" Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas ainda não atigiram a ma
ioridade e quantas já são maiores
"""
from datetime import date

atual = date.today().year
totMaior = 0
totMenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em quem ano a {}° pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totMaior))
print('E também tivemos {} pessoas menores de idade'.format(totMenor))
