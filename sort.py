arquivoTemporario = "arquivoTemporario.txt"

def sort():
    with open(arquivoTemporario, 'r') as arquivo:
        conteudo = arquivo.read().splitlines()  # Lê o arquivo linha por linha
    return conteudo 