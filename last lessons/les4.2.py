a = int(input())
b = int(input())
c = input()

if b == 0 and c == "/":
    print("На ноль делить нельзя!")
elif c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
else:
    print("Неверная операция")


