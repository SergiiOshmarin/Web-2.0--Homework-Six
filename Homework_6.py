from datetime import datetime
import faker
from random import randint, choice
import sqlite3

# Define the number of students, groups, subjects, and teachers
NUMBER_STUDENTS = 30
NUMBER_GROUPS = ["Group A", "Group B", "Group C"]
NUMBER_SUBJECTS = ["Math", "Physics", "Chemistry", "Biology", "Computer Science"]
NUMBER_TEACHERS = 5
fake_data = faker.Faker()

def generate_fake_data(number_students, number_groups, number_subjects, number_teachers) -> tuple():
    fake_students = []  # to store students
    fake_groups = []  # to store groups
    fake_subjects = []  # to store subjects
    fake_teachers = []  # to store teachers
    # generate number_students fake students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # generate number_groups fake groups
    for _ in number_groups:
        fake_groups.append(_)

    # generate number_subjects fake subjects
    for _ in number_subjects:
        fake_subjects.append(_)
    # generate number_teachers fake teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
    return fake_students, fake_groups, fake_subjects, fake_teachers


def prepare_data(students, groups, subjects, teachers) -> tuple():
    for_students = []  # to store student data
    for_groups = []  # to store group data
    for_subjects = []  # to store subject data
    for_teachers = []  # to store teacher data
    for_grades = []  # to store grade data
    assigned_subjects = {}  # dictionary to keep track of assigned subjects for each student
    assigned_teacher_subject = {}  # dictionary to keep track of assigned subject for each teacher
    for teacher in teachers:
        assigned_teacher_subject[teacher] = None  # initially no subject is assigned to teacher

    # prepare list of tuples for students table
    for student in students:
        for_students.append((student,))

    # prepare list of tuples for groups table
    for group in groups:
        for_groups.append((group,))

    # prepare list of tuples for subjects table
    for subject in subjects:
        for_subjects.append((subject,))

    # prepare list of tuples for teachers table
    for teacher in teachers:
        for_teachers.append((teacher,))

    # prepare list of tuples for grades table
    for i in range(30*5):
        student_id = randint(1, NUMBER_STUDENTS)
        group_id = randint(1, len(NUMBER_GROUPS))
        # pick a subject that has not been assigned to the student
        if student_id not in assigned_subjects:
            assigned_subjects[student_id] = set()
        subject_id = randint(1, len(NUMBER_SUBJECTS))
        while subject_id in assigned_subjects[student_id]:
            subject_id = randint(1, len(NUMBER_SUBJECTS))
            if len(assigned_subjects[student_id]) == len(NUMBER_SUBJECTS):
                break
        assigned_subjects[student_id].add(subject_id)
        teacher_id = randint(1, NUMBER_TEACHERS)
        teacher = teachers[teacher_id - 1]
        if not assigned_teacher_subject[teacher]:
            assigned_teacher_subject[teacher] = subject_id
        else:
            subject_id = assigned_teacher_subject[teacher]
        grade = randint(1, 5)
        date = fake_data.date()
        for_grades.append((student_id, group_id, subject_id, teacher_id, grade, date))

    return for_students, for_groups, for_subjects, for_teachers, for_grades

def insert_data(students, groups, subjects, teachers, grades):
    # Connect to a new database or create one if it doesn't exist
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()
    # Create tables
    cursor.execute("""CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS groups
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS grades
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, group_id INTEGER, 
                    subject_id INTEGER, teacher_id INTEGER, grade INTEGER, date DATETIME)
                """)

    # Insert data into students table
    cursor.executemany("INSERT INTO students (name) VALUES (?)", students)

    # Insert data into groups table
    cursor.executemany("INSERT INTO groups (name) VALUES (?)", groups)

    # Insert data into subjects table
    cursor.executemany("INSERT INTO subjects (name) VALUES (?)", subjects)

    # Insert data into teachers table
    cursor.executemany("INSERT INTO teachers (name) VALUES (?)", teachers)

    # Insert data into grades table
    cursor.executemany("INSERT INTO grades (student_id, group_id, subject_id, teacher_id, grade, date) VALUES (?,?,?,?,?,?)", grades)

    # commit the transaction
    conn.commit()
    cursor.execute("SELECT name from sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")
    # Close the connection
    conn.close()

if __name__ == '__main__':
    students, groups, subjects, teachers = generate_fake_data(
    NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS)
    data = prepare_data(students, groups, subjects, teachers)
    insert_data(*data)