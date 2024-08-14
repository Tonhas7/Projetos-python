def contar_caracteres(frase):
    # Cria um dicionário vazio para armazenar a contagem dos caracteres
    contagem = {}

    # Itera sobre cada caractere na frase
    for caractere in frase:
        # Verifica se o caractere já está no dicionário
        if caractere in contagem:
            # Se estiver, incrementa o contador
            contagem[caractere] += 1
        else:
            # Caso contrário, adiciona o caractere ao dicionário com a contagem 1
            contagem[caractere] = 1

    return contagem


# Lê a frase do usuário
frase = input("Digite uma frase: ")

# Obtém o dicionário com a contagem dos caracteres
resultado = contar_caracteres(frase)

# Exibe o resultado
print(resultado)