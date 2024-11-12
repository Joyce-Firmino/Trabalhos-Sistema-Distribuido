import threading

final = "final.txt"
lock = threading.Lock()  # Lock para evitar problemas de concorrência

# Função reduce para escrever as linhas que deram match no arquivo final
def reduce(linha):
    with lock:
        with open(final, "a") as arquivoFinal:
            arquivoFinal.write(linha + "\n")  # Escreve a linha correspondente no arquivo final
    print(linha)  # Imprime a linha correspondente