# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salario_fixo = float(input())
quantidade_de_vendas = float(input())

bonus = float(quantidade_de_vendas * (15/100))

total = salario_fixo + bonus

print("TOTAL = R$ %0.2f" %total)