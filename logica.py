import json

def importar_perguntas(ficheiro):
    perguntas = []
    with open(ficheiro, "r") as fich:
        perguntas = json.load(fich)
    
    return perguntas