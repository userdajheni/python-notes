# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# a função split() pega uma string e corta onde houver espaços
# exemplo:
# dados = "jheni 28"
# print(dados.split())
# resultado: ['jheni', '28']

# isso é uma lista com dois itens
# guardar cada item em uma variavel: nome, idade = dados.split()

# é como se fosse:
# lista = dados.split()
# nome = lista[0]
# idade = lista[1]

# resultado: nome = 'jheni' idade = '28'

# cod_peca1, num_peca1, valor_peca1 = input().split() --> INPUT SEMPRE É STRING

# para transformar a entrada em numero use a funcao MAP

cod_peca1, quant_peca1, valor_peca1 = map(float, input().split())
cod_peca2, quant_peca2, valor_peca2 = map(float, input().split())

total_peca1 = quant_peca1 * valor_peca1
total_peca2 = quant_peca2 * valor_peca2

soma = total_peca1 + total_peca2

print("VALOR A PAGAR: R$ {:.2f}".format(soma))