n = int(input("Digite um número inteiro: "))
s = 0
i = 0
l = len(str(n))
if l == 1:
	print(n)
else:
	while i < l:
		r = n % 10
		n = n // 10
		s = s + r
		i = i + 1
print(s)