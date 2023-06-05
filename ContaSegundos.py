S= int(input("Coloque o tempo em segundos para conversão: "))

Sf = S%60
M = S // 60
Mf = M%60
H = M//60
Hf = H%24
D = H//24

print(D,"dias",Hf,"horas,",Mf,"minutos e",Sf,"segundos")