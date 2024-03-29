import view


# students
{1: {'Имя': 'Иван', 'Фамилия': 'Иванов', 'День рождения': '2000-01-01'}}
# class
{'1А': [], '1Б': []}

student_id_counter = 0
students = {}
classes = {}



def AddNewStudent():
    new_student = dict()
    new_student['Id'] = GetNewId()
    new_student['Имя'] = view.GetNewStudentInfo('Имя студента')
    new_student['Фамилия'] = view.GetNewStudentInfo('Фамилия студента')
    new_student['День рождения'] = view.GetNewStudentInfo('День рождения студента')
    AddStudentsInClass(new_student['Id'])
    return new_student


def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def SaveStudents(student):
    with open('students.csv', 'a') as file:
        file.write(f"{student['Id']};{student['Имя']};{student['Фамилия']};{student['День рождения']}\n")


def AddStudentsInClass(student_id):
    global classes
    student_class = view.GetNewStudentInfo('students class')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]

def GetLastStudentId():
    global student_id_counter
    with open('last_student_id.txt', 'r', encoding='utf=8') as file:
        student_id_counter = int(file.read())

def SaveLastStudentId():
    global student_id_counter
    with open('last_student_id.txt', 'w', encoding='utf=8') as file:
        file.write(str(student_id_counter))

def SaveClasses():
    with open('classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')

def GetClasses():
    with open('classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            q = element.split(' - ')
        for i in range(0, len(temp), 2):
            classes[temp[i]]