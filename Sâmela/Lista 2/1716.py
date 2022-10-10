# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input("")
salario = float(input(""))

if plano == "A":
    novoSalario = (salario + (salario * 0.10))
    print("Novo salário: R$%.2f" % novoSalario)
    
elif plano == "B":
    novoSalario = (salario + (salario * 0.15))
    print("Novo salário: R$%.2f" % novoSalario)
    
elif plano == "C":
    novoSalario = (salario + (salario * 0.20))
    print("Novo salário: R$%.2f" % novoSalario)
