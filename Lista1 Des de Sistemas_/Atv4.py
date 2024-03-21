num1 = int(input("Digite a área a ser pintada em metros quadrados:"))

coberturaporlitro = 5
litrosporlata = 18
precoporlata = 55.00

litrosnecessarios = (num1 / coberturaporlitro)
latasnecessarias = (litrosnecessarios / litrosporlata)
precototal = (latasnecessarias * precoporlata)

print(f"A quantidade de latas necessárias é: {latasnecessarias:.2f}")
print(f"O preço total será: {precototal:.2f}")

