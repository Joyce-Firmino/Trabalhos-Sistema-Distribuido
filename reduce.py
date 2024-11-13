import threading


final = "final.txt"

lock = threading.Lock()  # Lock para evitar problemas de concorrência
   
def reduce(palavra, valor):
    with lock:
        #print(f"Thread concorrendo para escrever: {palavra}")  # Mensagem de concorrência
        with open(final, "a") as arquivoFinal:
            arquivoFinal.write(f"{palavra}\n") 
    print(f"{palavra} {len(valor)}")