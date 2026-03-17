
def menu_principal():
    print("\n-------------------------------------------\n")
    print("JOGO DE PERGUNTA!")
    print("\n-------------------------------------------\n")
    print("1 - jogar")
    print("2 - regras/ajuda")
    print("3 - sair")

    x = int(input("Escolha uma opcao: "))
    return x

def ajuda():
    print("\n-------------------------------------------\n")
    print("JOGO DE PERGUNTA!")
    print("\n-------------------------------------------\n")
    print("- Cada pergunta terá pontuação.")
    print("- Só á uma chance por pergunta.")
    print("- se você acertar a resposta, voce ganha um ponto. se errar a resposta, você não ganha ponto.")
    ajuda = input("Enter para voltar")
    return ajuda


def mostra_pergunta(pergunta, n):
    print("\n-------------------------------------------\n")
    print("Pergunta número: ", n)
    print("\n-------------------------------------------\n")
    print(pergunta["Pergunta"])
    conta = 1
    for resposta in pergunta["Respostas"]:
        print(f"{conta} - {resposta}")
        conta += 1
    print("Pontos: ", pergunta["Pontos"])
    op = int(input("Qual a sua opção 1, 2, 3 ou 4: "))
    return op
   
        