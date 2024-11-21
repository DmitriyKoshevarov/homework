#Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Переводим множество students в список, отсортированный в алфавитом порядке
students = sorted(students)
#Создаем пустой словарь
avg_grades = {}
#Запускаем цикл для обращения к каждому студенту и его оценкам с переводом списков в кортежи при помощи функции zip
for student, grade in zip(students, grades): avg_grades[student] = sum(grade) / len(grade)
#Выводим полученный словарь на экран
print(avg_grades)