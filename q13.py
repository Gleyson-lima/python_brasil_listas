altura=float(input("informe sua altura: "))
sexo=int(input("qual seu sexo? [1]homem, [2]mulher: "))
if sexo==1:
 peso_ideal=(72.7*altura) - 58
 print(f"seu peso ideal seria: {peso_ideal:.2f} kg")
if sexo==2:
 peso_ideal=(62.1*altura) - 44.7
 print(f"seu peso ideal seria: {peso_ideal:.2f} kg")
