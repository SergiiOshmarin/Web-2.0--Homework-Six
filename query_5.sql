SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN teachers ON grades.teacher_id = teachers.id
WHERE teachers.name = 'Katrina Gillespie';