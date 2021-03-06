from random import randint

chislo = int(randint(0, 10))

print("Игра угадай число от 1 до 10!")
gotovnost = input("Готовы?: ")

if gotovnost == "Да":
	otvet = int(input("Бот загадал число от 1 до 10! Угадывай: "))
	if otvet == chislo:
		print("Малочик ,угадал")
		pass
	elif otvet > chislo:
		print("Не угодал) Загаданное число окозалось меньше)")
		pass
	elif otvet < chislo:
		print("Не угодал) Загаданное число оказалось больше)")
		pass
	else:
		pass
elif gotovnost == "Нет":
	print("Удали майнкрафт")

else:
	print("Ваш уровень развития слишком мал, чтобы угадывать числа.")




