import os # *
from time import sleep # *
import matplotlib.pyplot as plt

historicos = []
histcount = 0

#Função principal
def main():
    global histcount
    while True:
        print(f"MENU EXPLICATIVO DA CÂMERA: \n \n1. Modo pet \n2. Modo documento \n3. Modo Live Suggestions \n4. Histórico \n5. Gráficos\n0. Sair")
        op = input("Digite a opção que deseja visualisar: ")
        match op:
            case '1':
                histcount += 1
                opc1()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '2':
                histcount += 1
                opc2()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '3':
                histcount += 1
                opc3()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '4':
                opc4()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '5': # *
                histcount += 1
                opc5() # *
                os.system("cls" if os.name == "nt" else "clear") # *

            case '0':
                ponto = '.'
                for _ in range(3): # *
                    print(f"Saindo{ponto}")
                    sleep(0.8) # *
                    ponto += "."
                return
            
            case _:
                print("Opção inválida")

#Função Modo pet - descrição
def opc1():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Pet")
    print("Modo Pet:")
    print("Esse modo é focado em tirar fotos de forma automática de pets assim que a câmera for estabilizada e reconhecer o animal.")
    input("Digite algo para voltar: ")

#Função Modo documento - descrição
def opc2():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Documento")
    print("Modo Documento:")
    print("Esse modo escaneia textos e os envias para a área de transferencia do celular.")
    input("Digite algo para voltar: ")

#Função Modo live suggestions - descrição
def opc3():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Live Suggestions")
    print("Modo Live Suggestions:")
    print("Esse modo analisa a cena atual e sugere quais alterações nas configurações da câmera seriam ideias para aquela ocasião.")
    input("Digite algo para voltar: ")

#Função Histórico - mostra a histórico
def opc4():
    barra = '-------------------------'
    os.system("cls" if os.name == "nt" else "clear") # *
    print("Seu histórico: ")
    print("Você acessou 1 modo." if histcount == 1 else f"Você acessou {histcount} modos.")
    print(barra)

    print(f"Histórico: ", end='')
    for i in historicos: # *
        print(i, end=' | ')

    print(f"\n{barra}")
    input("Digite algo para voltar: ")

def opc5():
    os.system("cls" if os.name == "nt" else "clear") # *

    while True:
        print("\nGRÁFICOS DA PESQUISA: \n1. Aceitação dos modos\n2. Modo Documento por faixa etária\n3. Aceitação do Live Suggestions\n4. Aceitação do Modo Pet\n0. Voltar")
        op = input("- ")
        match op:
            case '1':
                modos = ['Documento', 'Pet', 'Live Suggestions']
                aprovacao = [43, 39, 31]

                plt.bar(modos, aprovacao)
                plt.title('Aceitação dos Modos da Câmera')
                plt.xlabel('Modos')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 43, '43')
                plt.text(1, 39, '39')
                plt.text(2, 31, '31')
                plt.ylim(0, 55)
                plt.show()

            case '2':
                idade = ['19 a 30 anos', 'Outras idades']
                documento = [34, 9]
 
                plt.bar(idade, documento)
                plt.title('Aceitação do Modo Documento por Idade')
                plt.xlabel('Faixa etária')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 34, '34')
                plt.text(1, 9, '9')
                plt.ylim(0, 40)
                plt.show()

            case '3':
                perfil = ['Trabalham com\nredes sociais', 'Outros participantes']
                live = [14, 17]

                plt.bar(perfil, live)
                plt.title('Aceitação do Live Suggestions')
                plt.xlabel('Perfil dos participantes')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 14, '14')
                plt.text(1, 17, '17')
                plt.show()

            case '4':
                avaliacao = ['Aprovaram', 'Não aprovaram']
                pet = [39, 16]
 
                plt.bar(avaliacao, pet)
                plt.title('Aceitação do Modo Pet')
                plt.xlabel('Avaliação')
                plt.ylabel('Quantidade de pessoas') 
                plt.text(0, 39, '39')
                plt.text(1, 16, '16')
                plt.ylim(0, 55)
                plt.show()

            case '0':
                return

            case _:
                print("Opção inválida")

main()