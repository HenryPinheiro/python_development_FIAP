print("Bem vindo ao sistema de peso por Kg!")

preco_quilo = float(input("Informe o valor cobrado por quilo: "))
peso_prato = float(input("Informe o peso do prato do cliente em Gramas: "))

preco_prato = preco_quilo * peso_prato
preco_prato = preco_prato / 1000

if peso_prato >= 1000:
    print("O peso do prato ultrapassou o limite, pagamento fixo de R$70,00")

print(f"O valor do prato é R${preco_prato:.2f}")