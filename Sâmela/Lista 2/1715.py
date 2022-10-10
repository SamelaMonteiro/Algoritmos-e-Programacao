# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

cod = int(input(""))
valor_compra = float(input(""))

if cod == 1:
  print("Valor total a ser pago: R$%.2f" % valor_compra)

elif cod == 2:
  desconto = valor_compra * 0.13
  total = valor_compra - desconto
  print("Valor total a ser pago: R$%.2f" % total)

elif cod == 3:
  desconto = valor_compra * 0.07
  total = valor_compra - desconto
  print("Valor total a ser pago: R$%.2f" % total)

else:
  print("OPÇÃO INVÁLIDA!")
