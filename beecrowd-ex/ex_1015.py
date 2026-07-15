# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

# Distancia = raiz quadrada de (x2-x1)² + (y2-y1)²

#  O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2. Saída: Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# input --> Lê tudo o que o usuário digitou como uma única string.
# spplit --> Ele divide a string onde encontrar espaços. o que era "5 4 87" se torna ["5", "4", "87"]
# map --> pega cada elemento da lista e aplica a função float. Input recebe string e o map transformou em float.

p1 = (x2 - x1) ** 2
p2 = (y2 - y1) ** 2

# elevar a potencia, no caso, ao quadrado: ** 2

distancia = math.sqrt(p1 + p2) # função de raiz quadrada

print("{:.4f}".format(distancia)) # coloquei quatro casas decimais