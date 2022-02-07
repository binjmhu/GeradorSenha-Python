from random import choice
import sys

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
PUNC = "!@#$%&*()_+-=[]|,./?><"


while True:
    
    print("Digite o tamanho da senha desejada:", end=" ")
    tamanho = int(input())
    if tamanho <= 0:
        sys.exit(0)

    maiuscula = ""
    while maiuscula != "N" and maiuscula != "S":
        print("Deseja o uso de letras maiúsculas? Sim[S] / Não[N]", end=" ")
        maiuscula = input().upper()
        useUpper = True if maiuscula == "S" else False
        
    numeros = ""
    while numeros != "N" and numeros != "S":
        print("Deseja o uso de números? Sim[S] / Não[N]", end=" ")
        numeros = input().upper()
        useNumbers = True if numeros == "S" else False
    
    pontuacao = ""
    while pontuacao != "N" and pontuacao != "S":
        print("Deseja o uso de pontuação? Sim[S] / Não[N]", end=" ")
        pontuacao = input().upper()
        usePunc = True if pontuacao == "S" else False

    valores = LOWER

    if useUpper: valores += UPPER
    if useNumbers: valores += NUMBERS
    if usePunc: valores += PUNC

    senha = ''
    for i in range(tamanho):
      senha += choice(valores)
  
    print('\n'+ "Senha Gerada: "+senha+'\n')
    
    repetir = ""
    while repetir != "N" and repetir != "S":
        print("Gerar nova senha? Sim[S] / Não[N]")
        repetir = input().upper()
    if repetir == "N": break
    else: pass