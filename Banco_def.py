AGENCIA = "0001"
usuarios = []
contas = []

# Função para criar usuário
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        print("❌ Já existe um usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, bairro, cidade - UF): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("✅ Usuário criado com sucesso!")

# Função para criar conta corrente
def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("❌ Usuário não encontrado.")
        return

    senha = input("Escolha uma senha para a conta: ")
    numero_conta = len(contas) + 1

    contas.append({
        "agencia": AGENCIA,
        "numero": numero_conta,
        "usuario": usuario,
        "senha": senha,
        "saldo": 0,
        "extrato": "",
        "limite": 500,
        "numero_saques": 0,
        "limite_saques": 3,
        "congelada": False
    })
    print(f"✅ Conta {numero_conta} criada com sucesso!")

# Função para listar contas
def listar_contas():
    for conta in contas:
        print(f"""
        Agência: {conta['agencia']}
        Número da Conta: {conta['numero']}
        Titular: {conta['usuario']['nome']}
        Conta congelada: {'Sim' if conta['congelada'] else 'Não'}
        """)

# Função para congelar conta
def congelar_conta():
    numero = int(input("Informe o número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero), None)

    if conta:
        conta["congelada"] = True
        print("🧊 Conta congelada com sucesso.")
    else:
        print("❌ Conta não encontrada.")

# Função de depósito (positional only)
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado.")
    else:
        print("❌ Valor inválido.")
    return saldo, extrato

# Função de saque (keyword only)
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("❌ Limite de saques atingido.")
    elif valor > limite:
        print("❌ Valor excede o limite por saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado.")
    else:
        print("❌ Valor inválido.")
    return saldo, extrato, numero_saques

# Função de extrato (positional + keyword only)
def mostrar_extrato(saldo, /, *, extrato):
    print("\n📄 EXTRATO")
    print(extrato if extrato else "Sem movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Menu principal
def menu():
    while True:
        print("""
        [1] Criar usuário
        [2] Criar conta
        [3] Listar contas
        [4] Congelar conta
        [5] Depositar
        [6] Sacar
        [7] Mostrar extrato
        [0] Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            listar_contas()
        elif opcao == "4":
            congelar_conta()
        elif opcao == "5":
            numero = int(input("Número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta and not conta["congelada"]:
                valor = float(input("Valor do depósito: "))
                conta["saldo"], conta["extrato"] = deposito(conta["saldo"], valor, conta["extrato"])
            else:
                print("❌ Conta não encontrada ou congelada.")
        elif opcao == "6":
            numero = int(input("Número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta and not conta["congelada"]:
                valor = float(input("Valor do saque: "))
                conta["saldo"], conta["extrato"], conta["numero_saques"] = saque(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["limite"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["limite_saques"]
                )
            else:
                print("❌ Conta não encontrada ou congelada.")
        elif opcao == "7":
            numero = int(input("Número da conta: "))
            conta = next((c for c in contas if c["numero"] == numero), None)
            if conta:
                mostrar_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("❌ Conta não encontrada.")
        elif opcao == "0":
            print("👋 Encerrando o sistema.")
            break
        else:
            print("❌ Opção inválida.")

menu()
