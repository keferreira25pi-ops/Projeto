from menu import ajuda, menu_principal, mostra_pergunta, mostra_pontos, fim_jogo
from logica import importar_perguntas

#Função para mostrar menu de níveis
def menu_niveis():
    print("\nEscolha o nível:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    try:
        return int(input("Opção: "))
    except ValueError:
        return 0  # valor inválido

#Função que roda as perguntas e soma pontos
def jogar(perguntas, acumulacao_pontos, nivel):
    print(f"\nVocê está jogando no nível {['Fácil', 'Médio', 'Difícil'][nivel-1]}")
    n = 1
    for pergunta in perguntas:
        resposta = mostra_pergunta(pergunta, n)
        n += 1
        resposta_final = resposta - 1

        if resposta_final == pergunta["Correta"]:
            print("Boa... acertou!!!")
            acumulacao_pontos += pergunta["Pontos"]
            print(f"Pontos total: {acumulacao_pontos}\n")
        else:
            print("Errou... próxima\n")

    return acumulacao_pontos

#Código principal 
acumulacao_pontos = 0

while True:
    op = menu_principal()  # 1 - jogar, 2 - regras, 3 - sair

    if op == 1:
        nivel_op = menu_niveis()  # variável local

        # Carrega o JSON correto de acordo com o nível
        if nivel_op == 1:
            perguntas = importar_perguntas("perguntas_facil.json")
        elif nivel_op == 2:
            perguntas = importar_perguntas("perguntas_medias.json")
        elif nivel_op == 3:
            perguntas = importar_perguntas("perguntas_dificil.json")
        else:
            print("Nível inválido! Voltando ao menu principal.\n")
            continue

        # Passa a variável local para a função jogar
        acumulacao_pontos = jogar(perguntas, acumulacao_pontos, nivel_op)
        mostra_pontos(acumulacao_pontos)
        fim_jogo()

    elif op == 2:
        print("\nAs regras:")
        print("1 - Escolha um nível")
        print("2 - Responda as perguntas")
        print("3 - Acertos somam pontos conforme dificuldade\n")

    elif op == 3:
        print(f"\nSaindo... Pontuação final: {acumulacao_pontos} pontos. Adeus!\n")
        break
