SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON grades.teacher_id = teachers.id
WHERE students.name = 'Gary Jones' AND teachers.name = 'Katrina Gillespie';