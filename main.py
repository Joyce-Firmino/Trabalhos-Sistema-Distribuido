from concurrent.futures import ThreadPoolExecutor
import threading
from gerador import gerar_palavras_aleatorias # type: ignore
from reduce import reduce
from limpador import limpador
from sort import sort
from map import map

arquivo1 = "arquivo1.txt"
arquivo2 = "arquivo2.txt"
arquivo3 = "arquivo3.txt"
arquivo4 = "arquivo4.txt"
arquivoTemporario = "arquivoTemporario.txt"
final = "final.txt"


if __name__ == "__main__":    
    # Limpador dos arquivos
    
    # limpador(arquivo1)
    # limpador(arquivo2)
    # limpador(arquivo3)
    # limpador(arquivo4)
    limpador(arquivoTemporario)
    limpador(final)
    
    # Gerador de palavras aleatórias
    alfabeto = "abcde"
    min_tamanho = 1
    max_tamanho = 2
    qtd_palavras = 5

    # Gera as palavras
    # gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo1)
    # gerar_palavras_aleatorias(alfabeto, min_tamanho, max_tamanho, qtd_palavras, arquivo2)
    
    
    # Solicitar o padrão de busca
    # pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"  #Padrão CPF
    # pattern = r"^\s*\d{3}\.\d{3}\.\d{3}-\d{2}"  #Padrão CPF
    pattern =  r"[a-z]{4}" #Padrão 4 letras minusculas consecutivas
    # pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #Padrão email
    # pattern = r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}" #Padrão telefone

    
    
    # Abrindo os arquivos de entrada
    files = [open(arquivo1), open(arquivo2), open (arquivo3), open(arquivo4)]
    
    # Criando threads para processar os arquivos em paralelo
    t1 = threading.Thread(target=map, args=[arquivo1, files[0].read(), pattern])
    t2 = threading.Thread(target=map, args=[arquivo2, files[1].read(), pattern])
    t3 = threading.Thread(target=map, args=[arquivo3, files[2].read(), pattern])
    t4 = threading.Thread(target=map, args=[arquivo4, files[3].read(), pattern])
    
     # Iniciando as threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    # Esperando as threads terminarem
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    # Fechando os arquivos de entrada
    files[0].close()
    files[1].close()
    files[2].close()
    files[3].close()
    
    # Organizando os dados iguais
    resultado = sort()
    
    # Usando ThreadPoolExecutor para processar cada item de `resultado`
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for palavra, valor in resultado.items():
            executor.submit(reduce, palavra, valor)
