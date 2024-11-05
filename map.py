import threading


arquivoTemporario = "arquivoTemporario.txt"

lock = threading.Lock()  # Lock para evitar problemas de concorrência

# Função para mapear palavras e escrevê-las no arquivo temporário
def map(nome, value):
    with lock:
        with open(arquivoTemporario, "a") as temporario:
            palavras = value.split()
            for w in palavras:
                temporario.write(f"{w},1\n")