class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: оценка не поставлена'
    
    def mdl(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            middle = sum(all_grades) / len(all_grades)
        else:
            middle = 0
        return middle

    def __ge__(self, lector):
        if isinstance(lector, Lecturer):
            return self.mdl() >= lector.mdl()
        else:
            return f'Функция не реализована'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mdl()}\n'
                f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}')
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  
    
    def mdl(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            middle = sum(all_grades) / len(all_grades)
        else:
            middle = 0
        return middle
     
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mdl()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка: оценка не поставлена'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

#Студенты
student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress.append('Git')
student.courses_in_progress.append('Python')
student.finished_courses.append('Введение в программирование')

student1 = Student('Байков', 'Сергей', 'male')
student1.courses_in_progress.append('Git')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('Введение в программирование')

#Лекторы
lector = Lecturer('Mickey', 'Rourke')
lector.courses_attached.append('Python')
lector.courses_attached.append('Git')
lector1 = Lecturer('John', 'Travolta')
lector1.courses_attached.append('Git')
lector1.courses_attached.append('Python')

#Ревьюеры
rew1 = Reviewer('Sam', 'Smith')
rew1.courses_attached.append('Git')
rew1.courses_attached.append('Python')
rew = Reviewer('Quentin', 'Tarantino')
rew.courses_attached.append('Python')
rew.courses_attached.append('Git')

#Оценки студентов для лекторов
student1.rate_lecturer(lector1, 'Git', 6)
student1.rate_lecturer(lector1, 'Python', 10)
student.rate_lecturer(lector, 'Python', 8)
student.rate_lecturer(lector, 'Git', 10)

#Оценки ревьюеров для студентов
rew1.rate_hw(student1, 'Git', 10)
rew1.rate_hw(student1, 'Git', 5)
rew1.rate_hw(student1, 'Python', 7)
rew1.rate_hw(student1, 'Python', 5)

rew1.rate_hw(student, 'Git', 8)
rew1.rate_hw(student, 'Git', 3)
rew1.rate_hw(student, 'Python', 4)
rew1.rate_hw(student, 'Python', 9)

#Вывод Студенты
print(student1)
print()
print(student)

print()
#Вывод Лекторы
print(lector1)
print()
print(lector)

print()
#Вывод Ревьюеры
print(rew1)
print()
print(rew)

print()
#Средние оценки студентов
students = [student, student1]
def mdl_students_grades():
    mdl_course_grades = []
    course_grades = {}
    for student in students:
        for course, grades in student.grades.items():
            if course in course_grades:
                course_grades[course] += [sum(grades) / len(grades)]
            else:
                course_grades[course] = [sum(grades) / len(grades)]
    for course, grades in course_grades.items():
        mdl_course_grades.append(f'{course}: {sum(grades) / len(grades)}')
    return f'Средние оценки студентов по курсам: {" ".join(mdl_course_grades)}'

print(mdl_students_grades())

print()
#Средние оценки лекторов
lectors = [lector, lector1]
def mdl_lector_grades():
    mdl_course_grades = []
    course_grades = {}
    for lector in lectors:
        for course, grades in lector.grades.items():
            if course in course_grades:
                course_grades[course] += [sum(grades) / len(grades)]
            else:
                course_grades[course] = [sum(grades) / len(grades)]
    for course, grades in course_grades.items():
        mdl_course_grades.append(f'{course}: {sum(grades) / len(grades)}')
    return f'Средние оценки лекторов по курсам: {" ".join(mdl_course_grades)}'

print(mdl_lector_grades())