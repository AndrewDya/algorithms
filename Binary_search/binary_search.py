boy_number = int(input("Загадайте число от 1 до 100: "))
computer_number, answer_boy, count_number = 50, 0, 1
COUNT = 50
print(f"{count_number} попытка, число: {computer_number}")
while computer_number != boy_number:
	if boy_number > computer_number:
		answer_boy = 2
	elif boy_number < computer_number:
		answer_boy = 3
	if answer_boy == 2:
		computer_number = computer_number + COUNT // 2
		if COUNT > 1:
			COUNT //= 2
		elif COUNT == 1:
			computer_number = computer_number + COUNT
	elif answer_boy == 3:
		computer_number = computer_number - COUNT // 2
		if COUNT > 1:
			COUNT //= 2
		elif COUNT == 1:
			computer_number = computer_number - COUNT
	count_number += 1
	print(f"{count_number} попытка, число: {computer_number}")
print(
	f"{computer_number} = {boy_number}, за {count_number} попыток")
