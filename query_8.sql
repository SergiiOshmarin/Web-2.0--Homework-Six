SELECT AVG(grades.grade) as avg_grade
FROM grades
JOIN teachers ON grades.teacher_id = teachers.id
WHERE teachers.name = 'Jessica Nielsen';