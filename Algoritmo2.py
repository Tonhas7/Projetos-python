# Lista que armazena os contatos da agenda
agenda = []

# Variável global para marcar se a agenda foi alterada desde a última gravação
alterada = False

# Função para solicitar e retornar o nome do usuário, usando um valor padrão se nenhum nome for fornecido
def pede_nome(padrao=""):
    nome = input("Nome: ")  # Solicita o nome do usuário
    if nome == "":  # Se nenhum nome for fornecido
        nome = padrao  # Usa o valor padrão
    return nome  # Retorna o nome

# Função para solicitar e retornar o telefone do usuário, usando um valor padrão se nenhum telefone for fornecido
def pede_telefone(padrao=""):
    telefone = input("Telefone: ")  # Solicita o telefone do usuário
    if telefone == "":  # Se nenhum telefone for fornecido
        telefone = padrao  # Usa o valor padrão
    return telefone  # Retorna o telefone

# Função para solicitar e retornar o endereço do usuário, usando um valor padrão se nenhum endereço for fornecido
def pede_endereco(padrao=""):
    endereco = input("Endereço: ")  # Solicita o endereço do usuário
    if endereco == "":  # Se nenhum endereço for fornecido
        endereco = padrao  # Usa o valor padrão
    return endereco  # Retorna o endereço

# Função para solicitar e retornar a cidade do usuário, usando um valor padrão se nenhuma cidade for fornecida
def pede_cidade(padrao=""):
    cidade = input("Cidade: ")  # Solicita a cidade do usuário
    if cidade == "":  # Se nenhuma cidade for fornecida
        cidade = padrao  # Usa o valor padrão
    return cidade  # Retorna a cidade

# Função para solicitar e retornar o UF do usuário, usando um valor padrão se nenhum UF for fornecido
def pede_uf(padrao=""):
    uf = input("UF: ")  # Solicita o UF do usuário
    if uf == "":  # Se nenhum UF for fornecido
        uf = padrao  # Usa o valor padrão
    return uf  # Retorna o UF

# Função para exibir os dados completos de um contato
def mostra_dados(nome, telefone, endereco, cidade, uf):
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereco} Cidade: {cidade} UF: {uf}")  # Exibe todos os dados do contato

# Função para solicitar e retornar o nome do arquivo
def pede_nome_arquivo():
    return input("Nome do arquivo: ")  # Solicita o nome do arquivo e o retorna

# Função para pesquisar um contato pelo nome na agenda e retornar o índice do contato
def pesquisa(nome):
    mnome = nome.lower()  # Converte o nome para minúsculas para pesquisa insensível a maiúsculas
    for p, e in enumerate(agenda):  # Percorre a agenda com índices
        if e[0].lower() == mnome:  # Compara o nome do contato (minúsculo) com o nome pesquisado
            return p  # Retorna o índice do contato se encontrado
    return None  # Retorna None se o contato não for encontrado

# Função para adicionar um novo contato à agenda
def novo():
    global agenda, alterada  # Usa as variáveis globais agenda e alterada
    nome = pede_nome()  # Solicita o nome do novo contato
    telefone = pede_telefone()  # Solicita o telefone do novo contato
    endereco = pede_endereco()  # Solicita o endereço do novo contato
    cidade = pede_cidade()  # Solicita a cidade do novo contato
    uf = pede_uf()  # Solicita o UF do novo contato
    agenda.append([nome, telefone, endereco, cidade, uf])  # Adiciona o novo contato à agenda
    alterada = True  # Marca a agenda como alterada

# Função para confirmar uma operação (por exemplo, apagar ou gravar) com o usuário
def confirma(operacao):
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()  # Solicita a confirmação e converte para maiúsculas
        if opcao in "SN":  # Verifica se a resposta é válida (S ou N)
            return opcao  # Retorna a resposta do usuário
        else:
            print("Resposta inválida. Escolha S ou N.")  # Mensagem de erro para resposta inválida

# Função para apagar um contato da agenda
def apaga():
    global agenda, alterada  # Usa as variáveis globais agenda e alterada
    nome = pede_nome()  # Solicita o nome do contato a ser apagado
    p = pesquisa(nome)  # Pesquisa o contato na agenda
    if p is not None:  # Se o contato for encontrado
        if confirma("apagamento") == "S":  # Confirma a operação de apagamento
            del agenda[p]  # Remove o contato da agenda
            alterada = True  # Marca a agenda como alterada
    else:
        print("Nome não encontrado.")  # Mensagem de erro se o contato não for encontrado

# Função para alterar os dados de um contato existente
def altera():
    global alterada  # Usa a variável global alterada
    p = pesquisa(pede_nome())  # Solicita o nome do contato e pesquisa na agenda
    if p is not None:  # Se o contato for encontrado
        nome = agenda[p][0]  # Obtém o nome atual do contato
        telefone = agenda[p][1]  # Obtém o telefone atual do contato
        endereco = agenda[p][2]  # Obtém o endereço atual do contato
        cidade = agenda[p][3]  # Obtém a cidade atual do contato
        uf = agenda[p][4]  # Obtém o UF atual do contato
        print("Encontrado:")  # Informa que o contato foi encontrado
        mostra_dados(nome, telefone, endereco, cidade, uf)  # Mostra os dados atuais do contato
        nome = pede_nome(nome)  # Solicita um novo nome, usando o nome atual como padrão
        telefone = pede_telefone(telefone)  # Solicita um novo telefone, usando o telefone atual como padrão
        endereco = pede_endereco(endereco)  # Solicita um novo endereço, usando o endereço atual como padrão
        cidade = pede_cidade(cidade)  # Solicita uma nova cidade, usando a cidade atual como padrão
        uf = pede_uf(uf)  # Solicita um novo UF, usando o UF atual como padrão
        if confirma("alteração") == "S":  # Confirma a operação de alteração
            agenda[p] = [nome, telefone, endereco, cidade, uf]  # Atualiza o contato na agenda
            alterada = True  # Marca a agenda como alterada
    else:
        print("Nome não encontrado.")  # Mensagem de erro se o contato não for encontrado

# Função para listar todos os contatos na agenda
def lista():
    print("\nAgenda\n" + "-" * 30)  # Exibe o cabeçalho da lista de contatos
    for posicao, e in enumerate(agenda):  # Percorre a agenda com índices
        print(f"Posição: {posicao} ", end="")  # Exibe a posição do contato
        mostra_dados(e[0], e[1], e[2], e[3], e[4])  # Mostra os dados do contato
    print("-" * 30 + "\n")  # Exibe o rodapé da lista de contatos

# Função para ler a última agenda gravada, se houver
def lê_última_agenda_gravada():
    ultima = ultima_agenda()  # Obtém o nome do último arquivo de agenda gravado
    if ultima is not None:  # Se um nome de arquivo for encontrado
        leia_arquivo(ultima)  # Lê o arquivo de agenda

# Função para obter o nome do último arquivo de agenda gravado
def ultima_agenda():
    try:
        arquivo = open("ultima_agenda.dat", "r", encoding="utf-8")  # Abre o arquivo de última agenda
        ultima = arquivo.readline()[:-1]  # Lê o nome do arquivo da última agenda gravada
        arquivo.close()  # Fecha o arquivo
        return ultima  # Retorna o nome do arquivo
    except FileNotFoundError:  # Se o arquivo não for encontrado
        return None  # Retorna None

# Função para atualizar o nome do arquivo da última agenda gravada
def atualiza_ultima(nome):
    arquivo = open("ultima_agenda.dat", "w", encoding="utf-8")  # Abre o arquivo de última agenda para escrita
    arquivo.write(f"{nome}\n")  # Grava o nome do arquivo da última agenda
    arquivo.close()  # Fecha o arquivo

# Função para ler os contatos de um arquivo e atualizar a agenda
def leia_arquivo(nome_arquivo):
    global agenda, alterada  # Usa as variáveis globais agenda e alterada
    arquivo = open(nome_arquivo, "r", encoding="utf-8")  # Abre o arquivo de contatos
    agenda = []  # Limpa a agenda
    for l in arquivo.readlines():  # Lê todas as linhas do arquivo
        dados = l.strip().split("#")  # Divide a linha em partes
        # Ajuste para lidar com cinco partes: nome, telefone, endereço, cidade, UF
        if len(dados) == 5:
            nome, telefone, endereco, cidade, uf = dados
            agenda.append([nome, telefone, endereco, cidade, uf])  # Adiciona o contato à agenda
    arquivo.close()  # Fecha o arquivo
    alterada = False  # Marca a agenda como não alterada

# Função para ler uma agenda de um arquivo, e perguntar se deseja salvar alterações não salvas
def lê():
    global alterada  # Usa a variável global alterada
    if alterada:  # Se a agenda foi alterada
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")  # Solicita ao usuário
        if confirma("gravação") == "S":  # Se o usuário deseja salvar
            grava()  # Grava a agenda
    print("Ler\n" + "-" * 30)  # Exibe o cabeçalho de leitura
    nome_arquivo = pede_nome_arquivo()  # Solicita o nome do arquivo para leitura
    leia_arquivo(nome_arquivo)  # Lê o arquivo de contatos
    atualiza_ultima(nome_arquivo)  # Atualiza o nome do último arquivo de agenda gravado

# Função para ordenar os contatos da agenda por nome usando o método de ordenação por bolha
def ordena():
    global alterada  # Usa a variável global alterada
    fim = len(agenda)  # Obtém o número total de contatos
    while fim > 1:  # Enquanto houver mais de um contato para ordenar
        i = 0  # Índice inicial
        trocou = False  # Flag para verificar se houve troca
        while i < (fim - 1):  # Percorre a lista para comparar pares de contatos
            if agenda[i][0] > agenda[i + 1][0]:  # Compara os nomes dos contatos
                agenda[i], agenda[i + 1] = agenda[i + 1], agenda[i]  # Troca os contatos se necessário
                trocou = True  # Marca que houve troca
            i += 1  # Avança o índice
        if not trocou:  # Se não houve troca, a lista está ordenada
            break
    alterada = True  # Marca a agenda como alterada

# Função para gravar a agenda em um arquivo
def grava():
    global alterada  # Usa a variável global alterada
    if not alterada:  # Se a agenda não foi alterada
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")  # Solicita confirmação
        if confirma("gravação") == "N":  # Se o usuário não deseja gravar
            return  # Sai da função
    print("Gravar\n" + "-" * 30)  # Exibe o cabeçalho de gravação
    nome_arquivo = pede_nome_arquivo()  # Solicita o nome do arquivo para gravação
    arquivo = open(nome_arquivo, "w", encoding="utf-8")  # Abre o arquivo para escrita
    for e in agenda:  # Percorre todos os contatos
        arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")  # Grava o contato no arquivo com todos os dados
    arquivo.close()  # Fecha o arquivo
    atualiza_ultima(nome_arquivo)  # Atualiza o nome do último arquivo de agenda gravado
    alterada = False  # Marca a agenda como não alterada

# Função para validar e retornar um valor inteiro dentro de um intervalo específico
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))  # Solicita um valor inteiro
            if inicio <= valor <= fim:  # Verifica se o valor está dentro do intervalo
                return valor  # Retorna o valor válido
        except ValueError:  # Se o valor não for um número inteiro
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")  # Mensagem de erro

# Função para exibir o menu e retornar a opção escolhida pelo usuário
def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")  # Exibe a quantidade de contatos e o estado da agenda
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)  # Solicita e retorna a opção escolhida pelo usuário

# Lê a última agenda gravada, se houver
lê_última_agenda_gravada()

# Loop principal do programa
while True:
    opcao = menu()  # Exibe o menu e obtém a opção escolhida pelo usuário
    if opcao == 0:  # Se a opção for 0 (Sair)
        break  # Sai do loop e encerra o programa
    elif opcao == 1:  # Se a opção for 1 (Novo)
        novo()  # Adiciona um novo contato
    elif opcao == 2:  # Se a opção for 2 (Altera)
        altera()  # Altera um contato existente
    elif opcao == 3:  # Se a opção for 3 (Apaga)
        apaga()  # Apaga um contato
    elif opcao == 4:  # Se a opção for 4 (Lista)
        lista()  # Lista todos os contatos
    elif opcao == 5:  # Se a opção for 5 (Grava)
        grava()  # Grava a agenda em um arquivo
    elif opcao == 6:  # Se a opção for 6 (Lê)
        lê()  # Lê uma agenda de um arquivo
    elif opcao == 7:  # Se a opção for 7 (Ordena por nome)
        ordena()  # Ordena a agenda por nome
