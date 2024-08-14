lista = []
def retornaMes(valor):
    meses = ['','janeiro','fevereiro',\
             'março','abril','maio','junho','julho',\
             'agosto','setembro','outubro','novembro','dezembro']
    return meses[valor]

def retornaDia(v):
    dias = ['','Primeiro','Dois',\
             'Três','Quatro','Cinco','Seis','Sete',\
             'Oito','Nove','Dez','Onze','Doze','Treze',\
            'Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',\
            'Dezenove','Vinte','Vinte e um','Vinte e dois','Vinte e três',\
            'Vinte e quatro','Vinte e cinco','Vinte e seis','Vinte e sete',\
            'Vinte e oito','Vinte e nove','Trinta','Trinta e um']
    return dias[v]

def retornaData():
    data = input('Escreva um ano no formato(dd/mm/aaaa): \n')
    dia, mes, ano = data.split('/')
    valor = int(mes)
    v = int(dia)
    c = '{} de {} de {}'.format(retornaDia(v), retornaMes(valor), ano)
    lista.append(c)

    return c

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    print('''
1-Converter Data
2-Listar Datas por extenso
0-Sair''')

    return valida_faixa_inteiro("Escolha uma opção: ", 0, 2)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        retornaData()
    elif opcao == 2:
        print(lista)
