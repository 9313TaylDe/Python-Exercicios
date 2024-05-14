saldo = float(input("Digite o valor do seu saldo: "))
saque = float(input("Digite o valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} na operação ")