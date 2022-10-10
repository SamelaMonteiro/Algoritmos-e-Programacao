# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

num = int(input())

fatorial = 1
cont = num

while cont >= 1:
    fatorial = fatorial * cont
    cont = cont - 1

print("%i! = %i" %(num, fatorial))