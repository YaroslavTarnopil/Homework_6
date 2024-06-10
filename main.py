from faker import Faker
import random
import psycopg2

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="061488",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Видалення таблиць перед повторним створенням
cursor.execute("""
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS groups;
""")
conn.commit()

# Створення таблиць
cursor.execute("""
CREATE TABLE IF NOT EXISTS groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id INT REFERENCES groups(group_id)
);

CREATE TABLE IF NOT EXISTS subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id)
);

CREATE TABLE IF NOT EXISTS grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    subject_id INT REFERENCES subjects(subject_id),
    grade FLOAT,
    date_received DATE
);
""")
conn.commit()

# Наповнення таблиць даними
fake = Faker()

# Наповнення таблиці груп
groups = ["Group A", "Group B", "Group C"]
for group in groups:
    cursor.execute("INSERT INTO groups (group_name) VALUES (%s) ON CONFLICT (group_name) DO NOTHING;", (group,))
conn.commit()

# Наповнення таблиці викладачів
for _ in range(5):
    cursor.execute("INSERT INTO teachers (teacher_name) VALUES (%s);", (fake.name(),))
conn.commit()

# Наповнення таблиці студентів
for _ in range(50):
    cursor.execute("INSERT INTO students (student_name, group_id) VALUES (%s, %s);", (fake.name(), random.randint(1, 3)))
conn.commit()

# Наповнення таблиці предметів
subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Literature", "Computer Science"]
for subject in subjects:
    cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s);", (subject, random.randint(1, 5)))
conn.commit()

# Наповнення таблиці оцінок
for student_id in range(1, 51):
    for subject_id in range(1, 8):
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s);",
                       (student_id, subject_id, round(random.uniform(60, 100), 2), fake.date_between(start_date='-1y', end_date='today')))
conn.commit()

cursor.close()
conn.close()
