print("Promoção loja HP!!!")

total_compra = float(input("Informe o valor total da compra: "))
forma_pagamento = int(input("Selecione a forma de pagamento: \n[1] - Boleto \t[2] - Cartão"))

if forma_pagamento == 1:
    total_compra = total_compra * 0.95
    print(f"O valor total da compra com desconto fica: R${total_compra}")
elif forma_pagamento == 2:
    parcelas = int(input("Em quantas parcelas será pago: "))
    parcela = total_compra / parcelas
    print(f"O pagamento será feito em {parcelas} parcelas de R${parcela:.2f}")
