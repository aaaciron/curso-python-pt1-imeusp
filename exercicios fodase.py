def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i=i+1
    return(fat)

n = 1
while n > 0:
    print(fatorial(n))
    n = int(input("Digite um número inteiro: "))
