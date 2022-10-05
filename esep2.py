#Сапи Аяжан
#лаборатория4
x = input()
y = input()
while not(x.isdigit() and y.isdigit()):
    x, y = input(), input()
print(int(x) + int(y))