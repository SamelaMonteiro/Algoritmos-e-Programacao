# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

salario_hora = float(input())
horas_mes = float(input())

salario_bruto = salario_hora * horas_mes
desconto_imposto = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
desconto_total = desconto_imposto + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - desconto_total

print("Salário bruto: R$%.2f" % salario_bruto)
print("Imposto: R$%.2f" % desconto_imposto)
print("INSS: R$%.2f" % desconto_inss)
print("Sindicato: R$%.2f" % desconto_sindicato)
print("Líquido: R$%.2f" % salario_liquido)