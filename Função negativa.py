def separar_positivos_negativos(lista):
    positivos = []
    negativos = []

    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)
    return positivos, negativos

def main():
    entrada = input('Digite uma lista de números inteiros separados por espaço: ')
    lista_numeros = list(map(int, entrada.split()))
    positivos, negativos = separar_positivos_negativos(lista_numeros)
    print("Números positivos:", positivos)
    print("Números negativos:", negativos)
if __name__ == '__main__':
    main()