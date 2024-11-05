from concurrent.futures import ThreadPoolExecutor
import threading
from gerador import gerar_palavras_aleatorias
from reduce import reduce
from limpador import limpador
from sort import sort
from map import map

arquivo1 = "arquivo1.txt"
arquivo2 = "arquivo2.txt"
arquivoTemporario = "arquivoTemporario.txt"
final = "final.txt"


if __name__ == "__main__":    
    # Limpador dos arquivos
    limpador(arquivo1)
    limpador(arquivo2)
    limpador(arquivoTemporario)
    limpador(final)
    
    # Gerador de palavras aleatórias
    alfabeto = "abcde"
    min_tamanho = 1
    max_tamanho = 2
    qtd_palavras = 5

    # Gera as palavras
    gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo1)
    gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo2)
    
    # Abrindo os arquivos de entrada
    files = [open(arquivo1), open(arquivo2)]
    
    # Criando threads para processar os arquivos em paralelo
    t1 = threading.Thread(target=map, args=[arquivo1, files[0].read()])
    t2 = threading.Thread(target=map, args=[arquivo2, files[1].read()])
    
    # Iniciando as threads
    t1.start()
    t2.start()
    
    # Esperando as threads terminarem
    t1.join()
    t2.join()
    
    # Fechando os arquivos de entrada
    files[0].close()
    files[1].close()
    
    # Organizando os dados iguais
    resultado = sort()
    
    # Usando ThreadPoolExecutor para processar cada item de `resultado`
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for palavra, valor in resultado.items():
            executor.submit(reduce, palavra, valor)




# from concurrent.futures import ThreadPoolExecutor
# import threading

# from gerador import gerar_palavras_aleatorias

# arquivo1 = "arquivo1.txt"
# arquivo2 = "arquivo2.txt"
# arquivoTemporario = "arquivoTemporario.txt"
# final = "final.txt"


# # Função para mapear palavras e escrevê-las no arquivo temporário
# def map(value):
#     with open(arquivoTemporario, "a") as temporario:
#         palavras = value.split()
#         for w in palavras:
#             temporario.write(f"{w},1\n")  # Usando vírgula como separador e nova linha a cada palavra

# # Função para ler e reduzir (agregar os valores do arquivo temporário)
# def sort():
#     with open(arquivoTemporario, 'r') as arquivo:
#         conteudo = arquivo.read().splitlines()  # Lê o arquivo linha por linha
#     resultado = {}
#     for item in conteudo:
#         palavra, valor = item.split(',')
#         valor = int(valor)
        
#         if palavra in resultado:
#             resultado[palavra].append(valor)
#         else:
#             resultado[palavra] = [valor]  
#     print(f"resultado: {resultado}")
    
#     return resultado

# def reduce(palavra, valor):
#     with open(final, "a") as arquivoFinal:
#         arquivoFinal.write(f"{palavra} {len(valor)}\n")   
#     print(f"{palavra} {len(valor)} ,")
          
    
# def limpador (arquivo):
#     with open(arquivo, "w") as arquivoFinal:
#         arquivoFinal.write("")
    
    
# if __name__ == "__main__":    
    
#     # limpador dos arquivos
#     limpador(arquivo1)
#     limpador(arquivo2)
    
#     #perguntar ao professor
#     limpador(arquivoTemporario)
#     limpador(final)
    
#     # gerador de palabras aleatorias
#     alfabeto = "ab"
#     min_tamanho = 2
#     max_tamanho = 4
#     qtd_palavras = 20

#     # Gera as palavras
#     gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo1)
#     gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo2)
    

#     # Abrindo os arquivos de entrada
#     files = [open(arquivo1), open(arquivo2)]
    
#     # Criando threads para processar os arquivos em paralelo
#     t1 = threading.Thread(target=map, args=[files[0].read()])
#     t2 = threading.Thread(target=map, args=[files[1].read()])
    
#     # Iniciando as threads
#     t1.start()
#     t2.start()
    
#     # Esperando as threads terminarem
#     t1.join()
#     t2.join()
    
#     # Fechando os arquivos de entrada
#     files[0].close()
#     files[1].close()
    
#     # sort para organizar os dados iguais
#     resultado = sort()
    
#  # Maximo de 10 threads:
#     with ThreadPoolExecutor(max_workers=5) as executor: 
#         for palavra, valor in resultado.items():
#             executor.submit(reduce, palavra, valor)