n = int(input("Digite um número inteiro: "))
i = 1
d = 0
while i <= n:
        if n%i == 0:
                d = d+1
        i=i+1
if d == 2:
        print("primo")
else:
        print("não primo")
