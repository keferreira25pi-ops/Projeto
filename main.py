from menu import ajuda, menu_principal, mostra_pergunta
from logica import importar_perguntas

perguntas = importar_perguntas("perguntas.json")

while True:
    op = menu_principal()
    if op == 1:
        n = 1
        for pergunta in perguntas:
            resposta = mostra_pergunta(pergunta, n)
            n += 1
            resposta_final = resposta - 1
            if resposta_final == pergunta["Correta"]:
                print("boa... acertou!!!")
                acumulacao_pontos = 0
                for pontos in acumulacao_pontos:
                    pontuacao = acumulacao_pontos =+ 10

            else:
                print("errou... próxima")
    elif op == 2:
        print("As regras")
    elif op == 3:
        print("A sair... Adeus... Fraco...")
        break




