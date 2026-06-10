# calcular volume de uma esfera
# sendo raio = R
# formula do volume = (4/3) * pi * R³
# considere pi = 3.14159

pi = 3.14159

R = float(input())

volume = (4/3) * pi * (R ** 3)

print("VOLUME = {:.3f}".format(volume))