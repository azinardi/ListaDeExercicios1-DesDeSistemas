turno = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno):").upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Valor inválido.")



