##funções

def somar():
    print(primeiro_numero + segundo_numero)

def subtrair():
    print(primeiro_numero - segundo_numero)

def multiplicar():
    print(primeiro_numero * segundo_numero)

def dividir():
    print(primeiro_numero / segundo_numero)




primeiro_numero = int(input("Digite o primeiro número"))
segundo_numero = int(input("Digite o segundo numero"))

print("(1) = soma   (2) = subtração   (3) = multiplicação   (4) = divisão")
escolha = int(input("Escolha a operação: "))



if(escolha == 1):
    somar()
elif(escolha == 2):
    subtrair()
elif(escolha == 3):
    multiplicar()
elif(escolha == 4):
    dividir()