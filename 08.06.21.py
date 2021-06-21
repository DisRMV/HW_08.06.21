class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course):
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
            self.finished_courses.append(course)
        else:
            return f"Ошибка. Студент {self.name} {self.surname} не обучается на курсе '{course}'"

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
           and course in self.courses_in_progress and 0 < grade <= 10 and type(grade) == int:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        grades_sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                grades_sum += grade
                counter += 1
        return round(grades_sum / counter, 2)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} " \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} " \
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            if self.avg_grade() < other_student.avg_grade():
                return f"{self.name} {self.surname } учится хуже, чем {other_student.name} {other_student.surname}"
            elif self.avg_grade() == other_student.avg_grade():
                return 'У студентов одинаковая успеваемость'
            else:
                return f"{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}"
        else:
            return 'Такого студента не существует'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def avg_grade(self):
        grades_sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                grades_sum += grade
                counter += 1
        return round(grades_sum / counter, 2)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}"

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            if self.avg_grade() < other_lecturer.avg_grade():
                return f"{self.name} {self.surname } имеет оценку ниже, чем {other_lecturer.name} {other_lecturer.surname}"
            elif self.avg_grade() == other_lecturer.avg_grade():
                return 'У лекторов одинаковые оценки за лекции'
            else:
                return f"{other_lecturer.name} {other_lecturer.surname} имеет оценку ниже, чем {self.name} {self.surname}"
        else:
            return 'Такого лектора не существует'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Darth', 'Vader', 'male')
best_student.finished_courses += ['Git', 'Some course']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

cool_student = Student('Frodo', 'Baggins', 'male')
cool_student.courses_in_progress += ['Git', 'Python', 'Some course']
cool_student.grades['Git'] = [10, 10]
cool_student.grades['Python'] = [10, 10]
cool_student.grades['Some course'] = [10, 10]
cool_student.add_courses('Some course')
print(cool_student.finished_courses)
print(cool_student.avg_grade())
print(best_student)
print(best_student > cool_student)

cool_mentor = Mentor('John', 'McClane')
cool_mentor.courses_attached += ['Python']
best_mentor = Mentor('Tony', 'Montana')

best_lecturer = Lecturer('King', 'Schultz')
best_lecturer.courses_attached += ['Python', 'Git']
best_lecturer.grades['Git'] = [10, 10]
cool_lecturer = Lecturer('Ace', 'Ventura')
cool_lecturer.courses_attached += ['Python', 'Git']
cool_lecturer.grades['Python'] = [10, 10, 8]
cool_lecturer.grades['Git'] = [6, 10]

best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Git', 8)
best_student.rate_lecturer(best_lecturer, 'Python', 9)
print(best_lecturer.grades)
print(best_lecturer.avg_grade())
print(best_lecturer)
print(best_lecturer > cool_lecturer)

some_reviewer = Reviewer('Jules', 'Winnfield')
cool_reviewer = Reviewer('Vito', 'Corleone')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(best_student, 'Python', 8)
print(best_student.grades)
print(some_reviewer)


def avg_grade_course_s(students_list, course):
    counter = 0
    sum_grades = 0
    for student in students_list:
        for grade in student.grades[course]:
            sum_grades += grade
            counter += 1
    return round(sum_grades / counter, 2)


student_list = [best_student, cool_student]
print(avg_grade_course_s(student_list, 'Python'))


def avg_grade_course_l(lecturer_list, course):
    counter = 0
    sum_grades = 0
    for lecturer in lecturer_list:
        for grade in lecturer.grades[course]:
            sum_grades += grade
            counter += 1
    return round(sum_grades / counter, 2)


lecturers_list = [best_lecturer, cool_lecturer]
print(avg_grade_course_l(lecturers_list, 'Git'))
