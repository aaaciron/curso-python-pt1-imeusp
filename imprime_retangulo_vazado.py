l = int(input("digite a largura: "))
h = int(input("digite a altura: "))

print(l * "#")

while h > 2:
    print("#" + (l - 2)*" " + "#")
    h = h -1

print(l*"#")
