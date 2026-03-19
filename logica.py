import json

def importar_perguntas(ficheiro):
    """Carrega perguntas de um JSON"""
    try:
        with open(ficheiro, "r", encoding="utf-8") as fich:
            perguntas = json.load(fich)
        return perguntas
    except FileNotFoundError:
        print(f"Arquivo {ficheiro} não encontrado!")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro no JSON: {e}")
        return []

def calcular_pontos(acumulacao_pontos, pergunta):
    """Soma os pontos da pergunta ao total"""
    return acumulacao_pontos + pergunta["Pontos"]