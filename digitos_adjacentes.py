n = int(input("Digite um número inteiro: "))
a = n%10
adj_iguais = False
i = 0

while n>0 and not adj_iguais:
    if (n//10)%10 == a:
        adj_iguais = True
    else:
        i = i+1
    a = (n//10)%10
    n = n//10
if adj_iguais:
    print("sim")
else:
    print("não")
