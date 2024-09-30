print("##############################################\n")

notas = [8.0, 5.5, 9.3, 7.6, 3.1]

print(notas[0])
print(notas[1])
print(notas[2])
print(notas[3])
print(notas[4])

print("\n##############################################\n")

notas2 = [8.0, 5.5, 9.3, 7.6, 3.1]

print(notas2[0] + 2) # 10

notas2[3] = 0.5

print(notas2)

print("\n##############################################\n")

notas3 = [8.0, 5.5, 9.3, 7.6, 3.1]

for i in range(5):
    print(notas3[i])

print("\n##############################################\n")

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    lista[i] = 5*i

print(lista)

print("\n##############################################\n")

notas4 = [8.0, 5.5, 9.3, 7.6, 3.1]

print(notas4[-1])
print(notas4[-2])
print(notas4[-3])
print(notas4[-4])
print(notas4[-5],"\n")
# print(notas4[-6]) # IndexError: list index out of range
print(notas4[::-1])

print("\n##############################################\n")

notas5 = [8.0, 5.5, 9.3, 7.6, 3.1]

print(notas5[1:4])

print("\n##############################################\n")

notas6 = [8.0, 5.5, 9.3, 7.6, 3.1]

print(len(notas6))

for i in range(len(notas6)):
    print(notas6[i])

print("\n##############################################\n")

notas7 = [8.0, 5.5, 9.3, 7.6, 3.1]

for i in range(len(notas7)):
    print(notas7[i])

for i in notas7:
    print(i)
   
print("\n##############################################\n")

notas8 = [8.0, 5.5, 9.3, 7.6, 3.1]
notas8.append(9.5)
print(notas8) 

print("\n##############################################\n")

# notas9 = []

# n = int(input("Informe a quantidade de notas: "))
# for i in range(n):
#     dado = float(input("Informe a " + str(i+1) + "ª nota: "))
#     notas9.append(dado)

# print(notas9)

print("\n##############################################\n")

lista1 = [1, 2, 3, 4, 5]
lista2 = [27, 28, 29, 30, 33]

x = lista1 + lista2

print(x)

print("\n##############################################\n")

y = [1, 2, 3,]
z = 4*y

print(z)

print("\n##############################################\n")

x = [40, 30, 10, 20]
x.insert(1, 99)

print(x)

print("\n##############################################\n")

x = [40, 99, 30, 10, 20]

del x[2]
print(x)

print("\n##############################################\n")

x = [40, 99, 10, 20]

x.remove(10)
print(x)

print("\n##############################################\n")

x = [40, 99, 10, 20, 13, 20, 14]
n = x.count(20)

print(n)

print("\n##############################################\n")

x = [0 for i in range(5)]
print(x)

x = [2*i for i in range(5)]
print(x)