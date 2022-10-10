# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input())
hora_extra = float(input())

salario_min = 1192.40
valor_hra_ex = 10

salario_hra_ex = hora_extra * valor_hra_ex
salario_bruto = 3 * salario_min + salario_hra_ex

if salario_bruto > 2000.00:
  inss = salario_bruto * 0.12
else:
  inss = salario_bruto * 0.5

if salario_bruto > 2500.00:
  ir = salario_bruto * 0.20
else:
  ir = salario_bruto *0.0

salario_liquido = salario_bruto - inss - ir

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salario_bruto))
print("Salário líquido: R$%.2f" %(salario_liquido))