def soma_pares(intervalo_inicial,intervalo_final):
    soma = 0
    for numero in range(intervalo_inicial, intervalo_final +1):
        if numero % 2 == 0:
            soma += numero
    return soma

inicio = 50
fim = 100
resultado = soma_pares(inicio,fim)
print('A soma dos números pares entre', inicio,'e', fim,'é:',resultado)