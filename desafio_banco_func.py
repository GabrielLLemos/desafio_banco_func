
LIMITE_SAQUES = 3

#Funções

def depositar(saldo, extrato, /):
    valor = float(input("Valor do Deposito: "))

    saldo += valor
    print(f"Novo Saldo: {saldo:.2f}")
    extrato.append(f"Valor depositado: R${valor:.2f}")
    return float(saldo)

def sacar(*, saldo, numero_saques, extrato):
    valor_saque = float(input("Valor de Saque: "))

    if saldo < valor_saque:
        print(f"Não é possível sacar, saldo insuficiente.\nValor atual: {saldo}")
    elif numero_saques > 2:
        print(f"Limite de saques atingido, não é possível sacar. \nSaldo: {saldo}")
    else:    
        saldo -= valor_saque
        print(f"Saque realizado com sucesso. \nNovo saldo: {saldo}")
        extrato.append(f"Valor sacado: R${valor_saque:.2f}")
        numero_saques += 1
    return float(saldo), numero_saques

def extrato_conta(saldo, / , *, extrato):

    print("Extrato: ")
    for i in range(0,len(extrato),1):
        print(extrato[i])
    print(f"Saldo: {saldo:.2f}")
    
def criar_usuario(usuarios):
    nome = input("Seu nome: ")
    data_nascimento = input("Sua data de nascimento: ")
    cpf = input("Seu CPF (apenas números): ")

    usuario = verificar_cpf(cpf, usuarios)
    if usuario is not None:
        print(f"\nCPF informado já está cadastrado. {usuario[2]}\n")
        return
    else:
        print("Usuário verificado.")

    endereco = input("Endereço contendo(Logradouro, número, bairro, cidade e estado): ")
    
    dados = {
        "nome":nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }    

    print(f"Dados da conta: {usuarios}")
    print("Criando Conta!\n")
    return dados

def verificar_cpf(cpf, usuarios):
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            cpf = usuario.values()
            cpf_lista = list(cpf)
            return cpf_lista

def criar_conta(numero_conta, usuarios, contas):
    agencia = "0001"

    cpf = input("Em qual CPF a conta será criada? ")
    usuario = verificar_cpf(cpf, usuarios)

    if usuario is not None:
        if usuario[2] == cpf:
            dados_usuario = dict(nome = usuario[0], data_nascimento = usuario[1], cpf = usuario[2], endereco = usuario[3])
            
            conta_dados = {
                "agencia": agencia,
                "numero_conta": numero_conta,
                "dados_usuario": dados_usuario
            }
               
            contas.append(conta_dados)
            print("Conta criada com sucesso!")
            print(conta_dados)
    else:
        print("\nUsuário não existe!\nNecessário criar usuário.")
        return

def listar_contas(contas):
    
    for conta in contas:
        print(f"""
            Nome: {conta['dados_usuario']['nome']}
            CPF: {conta['dados_usuario']['cpf']}
            Data de Nascimento: {conta['dados_usuario']['data_nascimento']}
            Endereço: {conta['dados_usuario']['endereco']}
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            """)
   

def navegar_menu():
    saldo = 1000
    extrato = []
    numero_saques = 0
    usuarios = []
    numero_conta = 1
    contas = []

    menu = """

    [CC] Criar Nova Conta
    [CRU] Criar Usuário
    [LC] Listar Contas
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

    => """

    while True:
        
        opcao = input(f"Escolha uma opção do Menu: {menu}")

        if opcao == "CC":
            criar_conta(numero_conta, usuarios, contas)
            numero_conta += 1
        
        elif opcao == "CRU":
            dados = criar_usuario(usuarios)
            usuarios.append(dados)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "D":
            saldo = depositar(saldo, extrato)
        
        elif opcao == "S":
            saldo, numero_saques = sacar(saldo = saldo, numero_saques = numero_saques, extrato=extrato)
        
        elif opcao == "E":
            extrato_conta(saldo, extrato=extrato)
        
        elif opcao == "Q":
            break

        else:
            print("Opção inválida!")


navegar_menu()