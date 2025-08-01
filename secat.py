import mysql.connector
import random
from faker import Faker
fake=Faker()

class StudentDB:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="ramya27032***",
            database="ed_tech"
        )
        self.cursor=self.conn.cursor()
        self.fake=Faker("en_IN")

    def insert_Student_Table(self, n=500):
        values=[]
        work_experience_std = random.sample(range(1, n+1),20)
        for i in range(n):
            Student_id = i+1
            Gender=random.choice(["Male","Female"])
            if Gender=="Male":
                Student_name=self.fake.name_male()
            else:
                Student_name=self.fake.name_female()
            Age = random.randint(18, 25)
            Enrollment_year = random.randint(2019, 2023)
            City = self.fake.city()
            if Student_id in   work_experience_std:
                Work_experience = random.choice(["Relationship Manager","Graophic Designer","Financial Analyist","Sales executive",
                                                 "Accountant","HR executive","Marketing Coordinator","Teacher","Business Analyst","Data enty"])
            else:
                Work_experience = "None"
            Degree = random.choice(["BCA","B.sc","B.Tech","BBA","BE","MCA","M.sc","ME"])
            Email = Student_name.lower().replace("","") + "@gmail.com"
            Course_batch = random.choice(["April", "Nov"])
            Attendance = random.randint(65, 100)
            Phone_number = self.fake.phone_number()
            
            Graduation_year = Enrollment_year - 3

            values.append((
                Student_id, Student_name, Gender, Age, Enrollment_year, Work_experience,
                City, Degree, Email, Course_batch, Attendance,
                Phone_number, Graduation_year
            ))
        query = """
        INSERT INTO Student_Table (
            Student_id, Student_name, Gender, Age, Enrollment_year, Work_experience, City,
            Degree, Email, Course_batch, Attendance, Phone_number, Graduation_year
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        """

        self.cursor.executemany(query, values)
        self.conn.commit()
        print(f" Successfully inserted {n} student records.")  

    def insert_Programming_Table(self, n=500):
        values=[]
        for i in range(n):
            Programming_id = i+1
            Student_id = i+1
            Language_Known = random.choice(["python, sql","python, java, sql","python, pandas, sql"])
            Problems_solved_python = random.randint(150,500)
            Problems_solved_sql = random.randint(150,500)
            Assessments_completed = random.randint(4,10)
            Mini_projects = random.randint(2,5)
            Certifications_earned = random.randint(2,10)
            Latest_project_score = round(random.uniform(51.0, 98.0), 2)
            
            values.append((
                Programming_id,Student_id,Language_Known,Problems_solved_python,Problems_solved_sql,Assessments_completed,Mini_projects,
                           Certifications_earned,Latest_project_score
            ))
        query = """
         INSERT INTO Programming_Table (
              Programming_id,Student_id,Language_Known,Problems_solved_python,Problems_solved_sql,Assessments_completed,Mini_projects,
              Certifications_earned,Latest_project_score
              )VALUES (%s, %s, %s, %s, %s, %s, %s ,%s ,%s)
        """
        self.cursor.executemany(query, values)
        self.conn.commit()
        print(f" Successfully inserted {n} student records.")  

    def insert_Soft_Skills_Table(self, n=500):
        values=[]
        for i in range(n):
            Soft_skill_id = i+1
            Student_id = i+1
            Communication = random.randint(75,100)
            Teamwork = random.randint(75,100)
            Presentation = random.randint(80,95)
            Leadership = random.randint(75,100)
            Problem_solving = random.randint(60,90)
            Critical_thinking = random.randint(70,95)
            Interpersonal_skills = random.randint(80,98)

            values.append((Soft_skill_id, Student_id, Communication, Teamwork, Presentation, Leadership, Problem_solving,
                           Critical_thinking, Interpersonal_skills
                          ))    
        query="""
        INSERT INTO Soft_Skills_Table(
            Soft_skill_id,Student_id,Communication,Teamwork,Presentation,Leadership,Problem_solving,Critical_thinking,Interpersonal_skills
            )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.executemany(query,values)
        self.conn.commit()
        print(f" Succesfully inserted {n} student records.")


    def insert_Placements_Table(self,n=500):
        values=[]
        date_list=["2024-06-05","2025-05-21","2024-09-06","2025-03-27","2025-04-28"]
        

        for i in range(n):
            Placement_id = i+1
            Student_id = i+1
            Placement_status = random.choice(["Placed","Ready","Not-Ready"])
            
            if Placement_status == "Placed":
                Technical_round_score = random.randint(75,100)
                Mock_interview_score = random.randint(85,98)
                Internships_completed = random.randint(4,5)
                Company_name = random.choice(["HCL","TCS","Wipro","infosys","infosys","IBM","Tech Mahindra","Amazon","Cognizant","Zoho"])
                Job_role = random.choice(["Software Developer","Full Stack Developer","AI/ML Engineer","Mobile App Developer",
                                          "DevOps Engineer","Web Developer(Frontend)","Data Analyst"])
                Placement_package=random.choice(["2.2 Lakhs","3.5 Lakhs","6.5 Lakhs","5.4 Lakhs","3.8 Lakhs"])
                Interview_rounds_cleared =5
                Placement_date=random.choice(date_list)
            else:
                Technical_round_score =random.randint(40,60)
                Mock_interview_score=random.randint(40,79)
                Internships_completed = random.randint(1,3)
                Company_name="-"
                Job_role="-"
                Placement_package="-"
                Interview_rounds_cleared = random.randint(1,4)
                Placement_date=None
                
              
            values.append((Placement_id, Student_id,Technical_round_score, Mock_interview_score, Internships_completed, Placement_status, 
                           Company_name, Job_role,Placement_package, Interview_rounds_cleared, Placement_date))
        query="""
        INSERT INTO Placements_Table(
             Placement_id, Student_id, Technical_round_score,Mock_interview_score, Internships_completed, Placement_status, Company_name, job_role,
             placement_package, Interview_rounds_cleared, Placement_date)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        
        self.cursor.executemany(query,values)
        self.conn.commit()
        print(f" Succesfully inserted {n} student records.")
    def close_connection(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = StudentDB()
    db.insert_Student_Table(500)
    db.insert_Programming_Table(500)
    db.insert_Soft_Skills_Table(500)
    db.insert_Placements_Table(500)
    db.close_connection()           



