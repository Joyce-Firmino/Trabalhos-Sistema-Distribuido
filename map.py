import re
import threading


arquivoTemporario = "arquivoTemporario.txt"

lock = threading.Lock()  # Lock para evitar problemas de concorrência

# Função para mapear palavras e escrevê-las no arquivo temporário
def map(nome, value, pattern):
    with lock:
        with open(arquivoTemporario, "a") as temporario:
            palavras = value.splitlines()
            for w in palavras:
                if re.search(pattern, w):
                    temporario.write(f"{w}:1\n")
