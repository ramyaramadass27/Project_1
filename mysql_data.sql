use ed_tech;

CREATE TABLE Student_Table(
     Student_id INT AUTO_INCREMENT PRIMARY KEY ,
     Student_name VARCHAR(100),
     Age INT,
     Gender VARCHAR(10),
     Degree varchar(10),
     Work_experience varchar(100),
     City VARCHAR(100),
     Email VARCHAR(100),
     Phone_number VARCHAR(15),
     Attendance int,       
     Enrollment_year INT,
     Course_batch VARCHAR(100),
     Graduation_year INT
     );
     
select * from Student_Table;

CREATE TABLE Programming_Table(
     Programming_id INT PRIMARY KEY,
     Student_id INT,
     Language_Known VARCHAR(100),
     Problems_solved_python INT,
     problems_solved_sql INT,
     Assessments_completed INT,
     Mini_projects INT,
     Certifications_earned INT,
     Latest_project_score FLOAT,
     FOREIGN KEY (Student_id) REFERENCES Student_Table(Student_id)
     );
     

     
SELECT * FROM Programming_Table;


CREATE TABLE Soft_Skills_Table(
     Soft_skill_id INT PRIMARY KEY,
     Student_id INT,
     Communication INT,
     Teamwork INT,
     Presentation INT,
     Leadership INT,
     Problem_solving int,
     Critical_thinking INT,
     Interpersonal_skills INT,
     FOREIGN KEY (Student_id) REFERENCES Student_Table (Student_id)
     );

     
SELECT * FROM Soft_Skills_Table;  

CREATE TABLE Placements_Table(
     Placement_id INT PRIMARY KEY,
     Student_id INT,
     Technical_round_score INT,
     Mock_interview_score INT,
     Internships_completed INT,
     Placement_status VARCHAR(100),
     Company_name VARCHAR(200),
     Job_role VARCHAR(200),
     Placement_package VARCHAR(100),
     Interview_rounds_cleared INT,
     Placement_date DATE,
     FOREIGN KEY (Student_id) REFERENCES Student_Table(Student_id)
     );
     
SELECT * FROM Placements_Table;

Create table Final_Statement_Report 
as select 
Student_Table.Student_id,
Student_Table.Student_name,
Student_Table.Age,
Student_Table.Gender, 
Student_Table.Attendance,
Student_Table.Email,
Student_Table.Degree,
Student_Table.City,
Student_Table.Phone_number, 
Student_Table.Work_experience,
Student_Table.Enrollment_year ,
Student_Table.Course_batch,
Student_Table.Graduation_year,
Programming_Table.Language_Known,
Programming_Table.Problems_solved_python,
Programming_Table.Problems_solved_sql,
Programming_Table.Assessments_completed,
Programming_Table.Mini_projects,
Programming_Table.Certifications_earned, 
Programming_Table.Latest_project_score,
Soft_Skills_Table.Communication, 
Soft_Skills_Table.Teamwork, 
Soft_Skills_Table.Presentation, 
Soft_Skills_Table.Leadership, 
Soft_Skills_Table.Problem_solving,
Soft_Skills_Table.Critical_thinking, 
Soft_Skills_Table.Interpersonal_skills,
Placements_Table.Technical_round_score,
Placements_Table.Mock_interview_score,
Placements_Table.Internships_completed,
Placements_Table.Placement_status,
Placements_Table.Company_name,
Placements_Table.Placement_package,
Placements_Table.Job_role,
Placements_Table.Interview_rounds_cleared,
Placements_Table.Placement_date
from Student_Table
 join
 Programming_Table
 on Student_Table.Student_id=Programming_Table.Student_id
 join 
 Soft_Skills_Table
on  Student_Table.Student_id= Soft_Skills_Table.Student_id
join
 Placements_Table
 on  Student_Table.Student_id= Placements_Table.Student_id;

select * from Final_Statement_Report;

SELECT * ,
ROUND((Communication+Teamwork+Presentation+Leadership+
Problem_solving+Critical_thinking+Interpersonal_skills
)/7,2) AS soft_skills_average
from Final_Statement_Report
order by Soft_Skills_Average desc
limit 25;

select *
from Final_Statement_Report
where Placement_status = 'Ready'
order by Mock_interview_score desc
limit 10;

SELECT *
FROM Final_Statement_Report
WHERE Placement_status = 'Ready'
ORDER BY Latest_project_score DESC
LIMIT 10;

select *
from Final_Statement_Report
where Gender = 'Female'
order by Technical_round_score desc
limit 10;

select *
from Final_Statement_Report
order by Problems_solved_python desc
limit 10;

select  *
from Final_Statement_Report
order by Problems_solved_sql desc
limit 10;

select * 
from Final_Statement_Report
order by Certifications_earned desc 
limit 50;


select * 
from Final_Statement_Report
order by Critical_thinking desc 
limit 50;

select *
from Final_Statement_Report
where Problems_solved_python>=450 and
Problems_solved_sql>=450;

select Placement_status, count(*) as count
from Final_Statement_Report
group by Placement_status;

select Gender, count(*)as count
from Final_Statement_Report
group by Gender;

select * 
from Final_Statement_Report
order by  Assessments_completed desc
limit 10;

select Student_name,
	(Problems_solved_python + Problems_solved_sql + Mock_interview_score) / 3 as avg_score
from Final_Statement_Report;


select Gender,count(*) as total_placed
from Final_Statement_report
where Placement_status="Placed"
group by Gender;

SELECT Course_batch, Enrollment_year, COUNT(*) AS placed_count
FROM Final_Statement_Report
WHERE Course_batch IN ('Nov', 'April')
  AND Enrollment_year IN (2022, 2023)
  AND Placement_status = 'Placed'
group by Course_batch, Enrollment_year
ORDER BY Enrollment_year, Course_batch;


select * 
from Final_Statement_Report
where Degree in ("M.tech","ME","MCA","M.sc");

select *
from  Final_Statement_Report
where Assessments_completed= 10;

SELECT
AVG(Communication) AS avg_Communication,
AVG(Teamwork) AS avg_Teamwork,
AVG(Presentation) AS avg_Presentation,
AVG(Leadership) AS avg_Leadership,
AVG(Problem_solving) AS avg_Problem_solving,
AVG(Critical_thinking) AS avg_Critical_thinking,
AVG(Interpersonal_skills) AS avg_Interpersonal_skills
FROM Final_Statement_Report;
