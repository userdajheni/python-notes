# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Exemplo de entrada: 576

# Exemplo de saída: 576
					# 5 nota(s) de R$ 100,00
					# 1 nota(s) de R$ 50,00
					# 1 nota(s) de R$ 20,00
					# 0 nota(s) de R$ 10,00
					# 1 nota(s) de R$ 5,00
					# 0 nota(s) de R$ 2,00
					# 1 nota(s) de R$ 1,00 

n = int(input())
print(n)

notas_100 = n // 100 # o operador // entrega o inteiro da divisão
resto_100 = n % 100 # o operador % entrega o resto da divisão, neste caso, o que falta para a gente dividir
print(f"{notas_100} nota(s) de R$ 100,00")

notas_50 = resto_100 // 50
resto_50 = resto_100 % 50
print(f"{notas_50} nota(s) de R$ 50,00")

notas_20 = resto_50 // 20
resto_20 = resto_50 % 20
print(f"{notas_20} nota(s) de R$ 20,00")

notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
print(f"{notas_10} nota(s) de R$ 10,00")

notas_5 = resto_10 // 5
resto_5 = resto_10 % 5
print(f"{notas_5} nota(s) de R$ 5,00")

notas_2 = resto_5 // 2
resto_2 = resto_5 % 2
print(f"{notas_2} nota(s) de R$ 2,00")

notas_1 = resto_2 // 1
print(f"{notas_1} nota(s) de R$ 1,00")

