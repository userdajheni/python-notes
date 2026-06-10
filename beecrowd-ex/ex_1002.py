# A fórmula para calcular a área de uma circunferência é: area = π . raio². 
# Considerando para este problema que π = 3.14159
# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
# Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area com 4 casas após o ponto decimal.


# fazer um numero ** 3 é elevar ao cubo. O asterisco é o expoente.
# função round arredonda casas depois da virgula - mas ele não mostra o zero
# {:.4f}.format arredonda as casas decimais e mostra o zero

raio = float(input())

n = 3.14159

# area = round((n * (raio ** 2)),4) --> aqui não mostra o zero

area = n * (raio ** 2)

print("A={:.4f}".format(area))