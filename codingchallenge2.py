# YOUTUBE LIVE CODING SESSION VID: https://youtu.be/D7w6_i5QwRY

class Student:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.scores = []

    def get_ave(self):
        return sum(self.scores) / test_amt

def translate_grade(numeric_grade):
    if numeric_grade >= 90:
        return "A"
    elif numeric_grade >= 80:
        return "B"
    elif numeric_grade >= 70:
        return "C"
    elif numeric_grade >= 60:
        return "D"
    else:
        return "F"

students_list = []

student_amt = int(input("Enter number of students: "))
test_amt = int(input("Enter number of tests: "))

for i in range(student_amt):
    student = Student()
    student.last_name = input("Enter student {}'s last name: ".format(i + 1))
    student.first_name = input("Enter student {}'s first name: ".format(i + 1))

    for i in range(test_amt):
        student.scores.append(int(input("Enter {} test {} score: ".format(
                            student.first_name + " " + student.last_name,
                            i + 1))))

    students_list.append(student)

for student in students_list:
    ave = student.get_ave()

    print("{first} {last}: {average:.2f} - {letter}".format(
                                        first = student.first_name,
                                        last = student.last_name,
                                        average = ave,
                                        letter = translate_grade(ave)
    ))
