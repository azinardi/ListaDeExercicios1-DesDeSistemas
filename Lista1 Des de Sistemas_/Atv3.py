num1 = float(input("Digite quanto você ganha por hora:"))
num2 = float(input("Digite o número de horas trabalhadas no mês:"))

salario = (num1 * num2)
inss = (salario * 5) / 100
sindicato = (salario * 2) / 100
ir = (salario * 12) / 100
salarioliquido = (salario - inss - sindicato - ir)

print("O salário bruto é:", salario)
print("O desconto do Inss é:", inss)
print("O desconto do sindicato é:", sindicato)
print("O salário líquido é:", salarioliquido)
