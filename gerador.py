import random

def gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, nome_arquivo):
    palavras = []
    
    for _ in range(qtd_palavras):
        tamanho_palavra = random.randint(min_tamanho, max_tamanho)
        palavra = ''.join(random.choice(alfabeto) for _ in range(tamanho_palavra))
        palavras.append(palavra)
    
    salvar_palavras_no_arquivo(nome_arquivo, palavras)

def salvar_palavras_no_arquivo(nome_arquivo, palavras):
    with open(nome_arquivo, "w") as arquivo:
        # Usa join para unir as palavras com um espaço entre elas
        arquivo.write(" ".join(palavras))


