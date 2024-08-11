grades = [[3, 5, 5, 4, 3], [2, 3, 2, 2], [5, 5, 2, 4], [3, 4, 4], [4, 5, 5, 5, 5]]
students = {'Джон', 'Борис', 'Сандро', 'Клим', 'Арон'}
'''содержит неупорядоченную последовательность имён
 всех учеников в классе'''
grades_m = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]  # вычисляет средний балл для каждого ученика
students_sort = sorted(students)  # упорядочивания имён всех учеников в классе
dict1 = dict(zip(students_sort, grades_m))
'''составляет словарь, используя grades и students, 
где ключ имя ученика, а значение - его средний балл'''
print(dict1)  # выводит данные
