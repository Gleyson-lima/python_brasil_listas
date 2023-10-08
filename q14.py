peso_peixes=int(input("informe a qtde de peixes em quilos:" ))
if peso_peixes>50:
    excesso=peso_peixes-50
    multa=excesso*4
    print(f"excesso: {excesso} KG, total da multa: {multa} R$")
else:
 print("tudo certo voçê não excedeu o peso estabelecido")
