first_number = int(input('Введите первое целое число:'))
second_number = int(input('Введите второе целое число:'))
third_number = int(input('Введите третье целое число:'))
if first_number == second_number == third_number:
    print(3)
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print(2)
else:
    print(0)