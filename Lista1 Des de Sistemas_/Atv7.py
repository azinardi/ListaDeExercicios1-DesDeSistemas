salario_atual = float(input("Digite o salário atual: R$"))

if salario_atual <=280:
    percentual_aumento = 25
elif salario_atual <= 700:
    percentual_aumento = 22
elif salario_atual <= 1500:
    percentual_aumento = 20
else:
    percentual_aumento = 5
    
aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + aumento

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")




