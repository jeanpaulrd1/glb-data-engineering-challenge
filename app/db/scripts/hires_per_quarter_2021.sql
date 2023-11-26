SELECT
	d.department
	,j.job 
	,SUM(CASE WHEN QUARTER(he.hired_date) = 1 THEN 1 ELSE 0 END) AS 'Q1'
	,SUM(CASE WHEN QUARTER(he.hired_date) = 2 THEN 1 ELSE 0 END) AS 'Q2'
	,SUM(CASE WHEN QUARTER(he.hired_date) = 3 THEN 1 ELSE 0 END) AS 'Q3'
	,SUM(CASE WHEN QUARTER(he.hired_date) = 4 THEN 1 ELSE 0 END) AS 'Q4'
FROM hired_employees he 
JOIN departments d ON he.department_id = d.id 
JOIN jobs j ON he.job_id  = j.id 
WHERE YEAR(he.hired_date) = 2021
GROUP BY d.department , j.job 
ORDER BY d.department , j.job;