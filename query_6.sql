SELECT students.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON grades.group_id = groups.id
WHERE groups.name = 'Group A';