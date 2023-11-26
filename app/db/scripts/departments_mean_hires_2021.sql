SELECT 
	he.department_id
	,d.department
	,COUNT(1) as 'hires_count'
FROM hired_employees he 
JOIN departments d ON he.department_id = d.id 
WHERE YEAR(he.hired_date) = 2021
GROUP BY he.department_id
HAVING COUNT(1) > 
	(SELECT
		COUNT(1) / (SELECT COUNT(1) FROM departments)
	 FROM hired_employees he2
	 WHERE YEAR(he2.hired_date) = 2021)
ORDER BY COUNT(1) DESC;