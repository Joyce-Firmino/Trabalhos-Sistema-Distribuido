import threading
import re

arquivoTemporario = "arquivoTemporario.txt"
lock = threading.Lock()  # Lock para evitar problemas de concorrência

# Função para mapear linhas que correspondem ao padrão e registrá-las no arquivo temporário
def map(nome, value, pattern):
    with lock:
        with open(arquivoTemporario, "a") as temporario:
            linhas = value.splitlines()
            for linha in linhas:
                if re.search(pattern, linha):  # Verifica se a linha dá match com o padrão
                    temporario.write(f"{nome}: {linha}\n")  # Escreve a linha e o nome do arquivo no arquivo temporário
