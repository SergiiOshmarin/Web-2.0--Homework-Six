SELECT students.name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = 'Math'
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 1;