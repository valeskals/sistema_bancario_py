def realizar_saque(saldo, extrato, num_saques):
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    if 0 < valor_saque <= saldo:
        if valor_saque <= 500 and num_saques < 3:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            num_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        elif valor_saque > 500:
            extrato += f"Tentativa de saque: R$ {valor_saque:.2f}. Limite de saque é R$ 500.00.\n"
            print("O valor solicitado ultrapassa o limite permitido de R$ 500,00.")
        else:
            extrato += f"Tentativa de saque: R$ {valor_saque:.2f}. Limite diário de saques excedido.\n"
            print("Limite diário de saques excedido.")
    else:
        print("Saldo insuficiente ou valor inválido.")
        
    return saldo, extrato, num_saques

def realizar_deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. Não foi possível realizar a operação.")

    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    print(f"Saldo: R$ {saldo:.2f}\n{extrato}")

def main():
    saldo = 0
    num_saques = 0
    extrato = "Confira o seu extrato abaixo:\n"

    while True:
        print("""
  ==================================================
  Bem-vind@ ao ValBank.
  Informe qual operação deseja realizar.
  1 - Saque | 2 - Depósito | 3 - Extrato | 4 - Sair
  ==================================================
  """)

        operacao = int(input("Digite a operação que deseja realizar: "))

        if operacao == 1:
            saldo, extrato, num_saques = realizar_saque(saldo, extrato, num_saques)
        elif operacao == 2:
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif operacao == 3:
            mostrar_extrato(saldo, extrato)
        elif operacao == 4:
            print("Obrigado por utilizar nosso serviço.")
            break
        else:
            print("Operação inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
