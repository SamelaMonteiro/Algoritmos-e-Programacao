# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1019

N= int(input())
h= N/3600
r= N%3600

minutos = r/60
segundos = r%60

print("%i:%i:%i"%(h,minutos,segundos))