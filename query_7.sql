SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON grades.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE groups.name = 'Group A' AND subjects.name = 'Biology';