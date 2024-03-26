texto = "Este texto quebra de linha \naqui. Porém aqui temos uma \ttabulação"
print(texto)

texto = "texto em minusculas AINDA É texto"

#Deixa apenas a primeira letra com o maisculula
print(texto.capitalize())

#Muda as letras do texto para maisusculas ou minusculas
print(texto.upper())
print(texto.lower())

#Verificar partes de um texto, retornando (True) ou (False)
print(texto.startswith("Tex")) #Inicio
print(texto.endswith("!")) #Final
print(texto.count("m")) #Quantidade de algum caractere
print("em" in texto) #Verifica se algo esta no texto

print(texto.replace("AINDA", "com certeza"))