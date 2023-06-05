def éPrimo(n):
    i = 1
    d = 0
    while i <= n:
        if n%i == 0:
                d = d+1
        i=i+1
    if d == 2:
        return True
    else:
        return False
def maior_primo(n):
    while n > 0:
        if éPrimo(n) == True:
            return n
        else:
            n = n-1
    print(n)
