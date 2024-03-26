print("Cadastro de Doadores de sangue")
nome = input("Por favor, digite seu nomecompleto: ")
peso = float(input("Digite seu peso em Kg: "))
altura = int(input("Digite sua altura em cm: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2024 - ano_nascimento
peso_minimo = peso > 50
idade_minima = idade >= 16

texto_saida = f"\n\tFICHA DE RESULTADO:\n\n\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE: {idade} Anos\n\tTEM PESO MINIMO PARA DOAR: {peso_minimo}\n\tTEM IDADE MINIMA PARA DOAR: {idade_minima}"
print(texto_saida)
