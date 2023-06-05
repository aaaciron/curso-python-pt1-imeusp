if __nome__ == "__main__":
    pass

n = int(input('Digite um número: '))
v = []
while n > 0:
    lista.append(n)
    x = int(input('Digite um número: '))
    n = x

v_inversa = []
for z in range(len(v), 0, -1):
    v_inversa.append(lista[z - 1])

for i in v_inversa:
    print(i)
