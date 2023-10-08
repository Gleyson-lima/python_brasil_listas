ganho=float(input("quanto vc ganha por hora: "))
horas_trabalhadas=int(input("quantas horas vc trabalhou no mês: "))

salario_bruto=ganho*horas_trabalhadas

print(f"salario bruto: {salario_bruto}")
print(f"valor pago ao inss: {salario_bruto*0.08}")
print(f"valor pago ao sindicato: {salario_bruto*0.05}")
print(f"salario liquido: {salario_bruto-(salario_bruto*0.24)}")