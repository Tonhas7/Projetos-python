def calcular_moda(lista):
    # Cria um dicionário para armazenar a frequência de cada elemento
    frequencias = {}

    # Conta a frequência de cada elemento na lista
    for elemento in lista:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1

    # Inicializa a lista para armazenar a moda e a variável para a maior frequência
    moda = []
    maior_frequencia = 0

    # Percorre o dicionário de frequências para determinar a moda
    for elemento, frequencia in frequencias.items():
        # Se a frequência atual é maior que a maior frequência registrada
        if frequencia > maior_frequencia:
            moda = [elemento]  # Atualiza a lista de moda com o novo elemento
            maior_frequencia = frequencia  # Atualiza a maior frequência
        # Se a frequência atual é igual à maior frequência registrada
        elif frequencia == maior_frequencia:
            moda.append(elemento)  # Adiciona o elemento à lista de moda

    # Retorna a lista de modas e a maior frequência
    return moda, maior_frequencia


# Entrada dos dados
lista = []
i = 1

# Solicita ao usuário a entrada de 10 elementos para a lista
while i <= 10:
    elem = int(input('Digite um elemento da lista: '))
    lista.append(elem)  # Adiciona o elemento à lista
    i += 1

# Chama a função calcular_moda para obter a moda e a frequência
moda, frequencia = calcular_moda(lista)

# Exibe a lista original e os resultados calculados
print('Lista:', lista)
print('Moda:', moda)
print('Frequência:', frequencia)