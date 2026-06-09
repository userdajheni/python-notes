# Crie um script que leia dois numeros e tente mostrar a soma entre eles

x = input("Digite um numero: ")
y = input("Digite outro numero: ")

soma = int(x) + int(y)

print("A soma entre eles e: ",soma)

# input retorna string mesmo que voce digite um numero. 
# Então quando voce recebe os dados voce precisa transforma-los em numeros novamente
# para isso voce pode usar int ou float por exemplo

A = int(input("Digite um numero: "))
B = int(input("Digite outro numero: "))

somando = A + B

print("A soma entre eles e:",somando)

# Você pode verificar qual é o tipo da variavel:
alguma_coisa = input("Digite:")
print(type(alguma_coisa))

alguma_coisa_int = int(input("Digite:"))
print(type(alguma_coisa_int))