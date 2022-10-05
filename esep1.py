#Сапи Аяжан
#лаборатория4
string = str(input("Text: "))
upper = 0
lower = 0
for a in string:
	if a.isupper():
		upper += 1
	else:
		lower +=1

if upper > lower:
	print(s.upper())
else:
	print(s.lower())