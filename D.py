def encontrar_maior_menor(dicionario):
    if not dicionario:
        return None, None

    # Obtém todos os valores do dicionário
    valores = dicionario.values()

    # Encontra o maior e o menor valor
    maior = max(valores)
    menor = min(valores)

    return maior, menor


def main():
    dicionario = {}

    print("Digite pares chave-valor para adicionar ao dicionário.")
    print("Digite 'sair' como chave para encerrar a entrada.")

    while True:
        chave = input("Digite a chave: ")
        if chave.lower() == 'sair':
            break

        valor = input("Digite o valor (numérico): ")
        try:
            valor = float(valor)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            continue

        dicionario[chave] = valor

    maior, menor = encontrar_maior_menor(dicionario)

    if maior is not None and menor is not None:
        print(f"O maior valor é: {maior}")
        print(f"O menor valor é: {menor}")
    else:
        print("O dicionário está vazio.")


if __name__ == "__main__":
    main()