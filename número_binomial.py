def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
            fat = fat*i
            i=i+1
    return fat
def binomial(n,k):
    if n >= k:
        bino = fatorial(n)/((fatorial(k))*fatorial(n-k))
        return bino
    else:
        print("Impossível realizar a operação")
