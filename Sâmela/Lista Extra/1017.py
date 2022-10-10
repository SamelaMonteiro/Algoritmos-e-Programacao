# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1017

tempo_gasto = int (input())
velocidade_media = int (input())
distancia_percorrida = tempo_gasto * velocidade_media
litros = distancia_percorrida/12

print("%.3f"%litros)