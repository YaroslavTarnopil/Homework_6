SELECT student_name, AVG(grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
GROUP BY students.student_id
ORDER BY avg_grade DESC
LIMIT 5;

SELECT student_name, AVG(grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE subject_id = 1 -- замініть 1 на потрібний subject_id
GROUP BY students.student_id
ORDER BY avg_grade DESC
LIMIT 1;

SELECT groups.group_name, AVG(grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN groups ON students.group_id = groups.group_id
WHERE subject_id = 1 -- замініть 1 на потрібний subject_id
GROUP BY groups.group_name;

SELECT AVG(grade) as avg_grade
FROM grades;

SELECT subjects.subject_name
FROM subjects
WHERE teacher_id = 1; -- замініть 1 на потрібний teacher_id

SELECT student_name
FROM students
WHERE group_id = 1; -- замініть 1 на потрібний group_id

SELECT student_name, grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE group_id = 1 AND subject_id = 1; -- замініть 1 на потрібний group_id та subject_id

SELECT AVG(grade) as avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE teacher_id = 1; -- замініть 1 на потрібний teacher_id

SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 1; -- замініть 1 на потрібний student_id

SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 1 AND subjects.teacher_id = 1; -- замініть 1 на потрібні student_id та teacher_id




