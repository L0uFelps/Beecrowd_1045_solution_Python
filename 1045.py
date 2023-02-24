x,y,z = input().split()

aa = float(x)
bb = float(y)
cc = float(z)

list = []

list.append(aa)
list.append(bb)
list.append(cc)

list.sort(reverse=True)

a = list[0]
b = list[1]
c = list[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c:
        print("TRIANGULO EQUILATERO")
    if a == b and a != c or a == c and a != b or b == a and b != c or b == c and b != a or c == a and c != b or c == b and c != a:
        print("TRIANGULO ISOSCELES")
