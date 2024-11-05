arquivoTemporario = "arquivoTemporario.txt"

# Função para ler e reduzir (agregar os valores do arquivo temporário)
def sort():
    with open(arquivoTemporario, 'r') as arquivo:
        conteudo = arquivo.read().splitlines()  # Lê o arquivo linha por linha
    resultado = {}
    for item in conteudo:
        palavra, valor = item.split(',')

        
        if palavra in resultado:
            resultado[palavra].append(valor)
        else:
            resultado[palavra] = [valor]
    print(f"resultado: {resultado}")
    return resultado