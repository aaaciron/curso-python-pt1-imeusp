l = int(input("digite a largura: "))
h = int(input("digite a altura: "))

i = 1
n = 1

while n <= h:
    while i <= l:
        print("#",end="")
        i = i +1
    print()
    n = n + 1
    i = 1
