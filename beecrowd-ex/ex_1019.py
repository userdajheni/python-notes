# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# exemplo de entrada: 140153
# exemplo de saida: 38:55:53

n = int(input())

# lembrando que: 1 minuto tem 60 segundos, 1 hora tem 60 minutos que são 3.600 segundos

horas = n // 3600
resto_horas = n % 3600

minutos = resto_horas // 60
resto_minutos = resto_horas % 60

print(f"{horas}:{minutos}:{resto_minutos}")