menu_opcoes = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_atual = 0
limite_saque = 500
extrato = []
numero_saques = 0
MAX_SAQUES_DIARIOS = 3

while True:
    escolha = input(menu_opcoes)
    
    if escolha == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo_atual += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif escolha == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo_insuficiente = valor_saque > saldo_atual
        saque_acima_limite = valor_saque > limite_saque
        excedeu_limite_saques = numero_saques >= MAX_SAQUES_DIARIOS
        
        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif saque_acima_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor_saque > 0:
            saldo_atual -= valor_saque
            extrato.append(f"Saque: R$ {valor_saque:.2f}")
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif escolha == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n".join(extrato))
        print(f"\nSaldo: R$ {saldo_atual:.2f}")
        print("==========================================")
    
    elif escolha == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
