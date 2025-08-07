menu_texto = """
[1] Adicionar fundos
[2] Retirar fundos
[3] Ver extrato
[0] Encerrar

=> """

carteira = 0
limite_saque = 500
extrato = ""
saques_realizados = 0
MAX_SAQUES_DIARIOS = 3

while True:
    escolha = input(menu_texto)

    if escolha == "1":
        deposito = float(input("Valor para depósito: R$ "))

        if deposito > 0:
            carteira += deposito
            extrato += f"Crédito: R$ {deposito:.2f}\n"
            print(f"Depósito efetuado. \n$$  Novo saldo: R$ {carteira:.2f}  $$")
        else:
            print("Erro: valor de depósito inválido.")

    elif escolha == "2":
        saque = float(input("Valor para saque: R$ "))
        print("Atenção: valor máximo de saque é R$ 500,00 e são permitidos 3 saques por dia.")

        saldo_insuficiente = saque > carteira
        acima_do_limite = saque > limite_saque
        atingiu_limite_saques = saques_realizados >= MAX_SAQUES_DIARIOS

        if saldo_insuficiente:
            print("Erro: saldo insuficiente.")
        elif acima_do_limite:
            print("Erro: valor excede o limite por saque.")
        elif atingiu_limite_saques:
            print("Erro: limite diário de saques atingido.")
        elif saque > 0:
            carteira -= saque
            extrato += f"Débito: R$ {saque:.2f}\n"
            saques_realizados += 1
            print(f"Saque realizado com sucesso.\n** Saques restantes: {MAX_SAQUES_DIARIOS - saques_realizados} **")
            print(f"Saldo atual: R$ {carteira:.2f}")
        else:
            print("Erro: valor de saque inválido.")

    elif escolha == "3":
        print("\n========= EXTRATO DE CONTA =========")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\nSaldo final: R$ {carteira:.2f}")
        print("====================================")

    elif escolha == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
