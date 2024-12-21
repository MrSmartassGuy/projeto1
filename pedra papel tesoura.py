from itertools import repeat
from random import Random
from turtledemo.forest import randomize
from time import sleep
import random

def comeco():

 escolha = str(input("Qual vais escolher? Pedra, papel ou tesoura?"))
 if escolha == "pedra":
     print("Escolheu pedra!")
 elif escolha == "papel":
     print("Escolheu papel!")
 elif escolha == "tesoura":
     print("Escolheu tesoura!")
 else:
     print("Isso não é uma opção")
comeco()

def jogo():
    escolha2 = random.randint(1,3)
    sleep(2)
    print("O adversário escolheu...")
    if escolha2 == 1:
        print("...pedra!")
    sleep(1)
    if escolha2 == 2:
        print("...papel!")
    sleep(1)
    if escolha2 == 3:
        print("...tesoura!")
    sleep(1)
jogo()

def ganhar():
    print("Pedra,")
    sleep(1)
    print("Papel,")
    sleep(1)
    print("Tesoura!")
    sleep(1)
    if escolha2 == 1 and escolha == "pedra":
        print("Empate!")
    sleep(1)
    if escolha2 == 2 and escolha == "papel":
        print("Empate!")
    sleep(1)
    if escolha2 == 3 and escolha == "tesoura":
        print("Empate!")
    sleep(1)
    if escolha2 == 1 and escolha == "papel":
        print("Ganhaste!")
    sleep(1)
    if escolha2 == 2 and escolha == "tesoura":
        print("Ganhaste!")
    sleep(1)
    if escolha2 == 3 and escolha == "pedra":
        print("Ganhaste!")
    sleep(1)
    if escolha2 == 2 and escolha == "pedra":
        print("Perdeste!")
    sleep(1)
    if escolha2 == 1 and escolha == "tesoura":
        print("Perdeste!")
    sleep(1)
    if escolha2 == 3 and escolha == "papel":
        print("Perdeste!")
    sleep(1)
ganhar()





