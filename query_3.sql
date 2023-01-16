SELECT groups.name, AVG(grades.grade) as avg_grade
FROM groups
JOIN grades ON groups.id = grades.group_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = 'Math'
GROUP BY groups.id;