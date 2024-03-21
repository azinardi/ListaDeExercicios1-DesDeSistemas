numero = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))

if numero < 1 or numero > 10:
    print("Número inválido.")
else:
    print("Tabuada do", numero, ":")
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        print(numero, "X", contador, "=", resultado)
        contador += 1






