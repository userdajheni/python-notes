# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

number = int(input())
time_work = int(input())
valor_hora = float(input())

salario = time_work * valor_hora

print("NUMBER =",number)
print("SALARY = U$ {:.2F}".format(salario))