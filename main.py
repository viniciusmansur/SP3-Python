import os
from time import sleep

historicos = []
histcount = 0

#Função principal
def main():
    global histcount
    while True:
        print(f"MENU EXPLICATIVO DA CÂMERA: \n \n1. Modo pet \n2. Modo documento \n3. Modo Live Suggestions \n4. Histórico \n0. Sair")
        op = input("Digite a opção que deseja visualisar: ")
        if op == '1':
            histcount += 1
            opc1()
            os.system("cls" if os.name == "nt" else "clear")
        elif op == '2':
            histcount += 1
            opc2()
            os.system("cls" if os.name == "nt" else "clear")
        elif op == '3':
            histcount += 1
            opc3()
            os.system("cls" if os.name == "nt" else "clear")
        elif op == '4':
            opc4()
            os.system("cls" if os.name == "nt" else "clear")
        elif op == '0':
            ponto = '.'
            for _ in range(3):
                print(f"Saindo{ponto}")
                sleep(0.8)
                ponto += "."
            return
        else:
            print("Opção inválida")

#Função Modo pet - descrição
def opc1():
    os.system("cls" if os.name == "nt" else "clear")
    historicos.append("Modo Pet")
    print("Modo Pet:")
    print("Esse modo é focado em tirar fotos de forma automática de pets assim que a câmera for estabilizada e reconhecer o animal.")
    input("Digite algo para voltar: ")

#Função Modo documento - descrição
def opc2():
    os.system("cls" if os.name == "nt" else "clear")
    historicos.append("Modo Documento")
    print("Modo Documento:")
    print("Esse modo escaneia textos e os envias para a área de transferencia do celular.")
    input("Digite algo para voltar: ")

#Função Modo live suggestions - descrição
def opc3():
    os.system("cls" if os.name == "nt" else "clear")
    historicos.append("Modo Live Suggestions")
    print("Modo Live Suggestions:")
    print("Esse modo analisa a cena atual e sugere quais alterações nas configurações da câmera seriam ideias para aquela ocasião.")
    input("Digite algo para voltar: ")

#Função Histórico - mostra a histórico
def opc4():
    barra = '-------------------------'
    os.system("cls" if os.name == "nt" else "clear")
    print("Seu histórico: ")
    print("Você acessou 1 modo." if histcount == 1 else f"Você acessou {histcount} modos.")
    print(barra)
    print(f"Histórico: ", end='')
    for i in historicos:
        
        print(i, end=' | ')
    print(f"\n{barra}")
    input("Digite algo para voltar: ")

main()