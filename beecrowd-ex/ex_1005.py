# Leia 2 valores flutuantes A e B, que correspondem a 2 notas de um aluno. 
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 
# A soma dos pesos portanto é 11. 
# Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

a = float(input())
b = float(input())

media = ((a * 3.5) + (b * 7.5)) / 11

# :.5f significa que quero 5 casas decimais

print("MEDIA = {:.5f}".format(media))