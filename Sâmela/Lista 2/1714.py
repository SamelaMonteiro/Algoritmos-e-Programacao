# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valor = float(input(""))
lucro0 = 0.45
lucro1 = 0.30

if valor < 20:
   valor_lucro = valor * lucro0
   lucro = valor_lucro + valor
   print("Valor de venda: R$%.2f" % lucro)

if valor > 20:
   valor_lucro = valor * lucro1
   lucro = valor_lucro + valor
   print("Valor de venda: R$%.2f" % lucro)
