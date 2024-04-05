print("Promoção loja HP!!!")

total_compra = float(input("Informe o valor total da compra: "))
forma_pagamento = int(input("Selecione a forma de pagamento: \n[1] - Boleto \t[2] - Cartão"))

if forma_pagamento == 1:
    print(f"O desconto foi de: R${total_compra*0.05}")
    print(f"O valor total da compra com desconto fica: R${total_compra*0.95}")
elif forma_pagamento == 2:
    parcelas = int(input("Em quantas parcelas será pago: "))
    parcela = total_compra / parcelas
    print(f"O pagamento será feito em {parcelas} parcelas de R${parcela:.2f}")
