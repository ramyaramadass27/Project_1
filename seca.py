import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ramya27032***",      
        database="ed_tech"     
    )

@st.cache_data
def load_data(Final_Statement_Report):
    conn = connect_to_mysql()
    cursor = conn.cursor()


    cursor.execute(f"SELECT * FROM Final_Statement_Report")
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    df= pd.DataFrame(rows, columns=columns)

    
    
    cursor.close()
    conn.close()
    return df

df = load_data("Final_Statement_Report")


page = st.sidebar.selectbox("📄 Select Page", ["🏠Home", "🔍Filter"])


if page == "🏠Home":
    st.title("Student Placement Insight📊: ")
    st.subheader("Students Final Report 💼 ")
    st.dataframe(df, use_container_width=True)

elif page == "🔍Filter":
    st.title("🔍 Filter - Final Statement Report")
    filter_type = st.radio("Choose filter type:", ["🔽 Predefined Queries", "✍️ Custom Filter"])

    if filter_type == "🔽 Predefined Queries":
        query_options = {
            "Which Batch performed best in Placements in last 2 years📅?":"""
                SELECT Course_batch, Enrollment_year, COUNT(*) AS Placed_count
                FROM Final_Statement_Report
                WHERE Course_batch IN ('Nov', 'April')
                AND Enrollment_year IN (2022, 2023)
                AND Placement_status = 'Placed'
                GROUP BY Course_batch, Enrollment_year
                ORDER BY Enrollment_year, Course_batch;
            """,
            
            "🔝Top 25 Student in Soft skills":"""
                SELECT * ,
                ROUND((Communication+Teamwork+Presentation+Leadership+
                Problem_solving+Critical_thinking+Interpersonal_skills
                )/7,2) AS soft_skills_average
                FROM Final_Statement_Report
                ORDER BY Soft_Skills_Average DESC
                LIMIT 25;
            """,

            "🔝Top 10 in Monk Interview📊(Ready)": """
                SELECT *
                FROM Final_Statement_Report
                WHERE Placement_status = 'Ready'
                ORDER BY Mock_interview_score DESC
                LIMIT 10;

            """,

            "Who got selected more - Male or Female🥇?":"""
                SELECT Gender,count(*) as total_placed
                FROM Final_Statement_report
                WHERE Placement_status="Placed"
                GROUP BY Gender;
            """,
            "Distribution of Soft skills📈":"""

                SELECT
                AVG(Communication) AS avg_Communication,
                AVG(Teamwork) AS avg_Teamwork,
                AVG(Presentation) AS avg_Presentation,
                AVG(Leadership) AS avg_Leadership,
                AVG(Problem_solving) AS avg_Problem_solving,
                AVG(Critical_thinking) AS avg_Critical_thinking,
                AVG(Interpersonal_skills) AS avg_Interpersonal_skills
                FROM Final_Statement_Report;

            """,
            
            "🔝Top 10 Student Ready for Interview based on previous Technical round score":"""
                SELECT *
                FROM Final_Statement_Report
                WHERE Placement_status = 'Ready'
                ORDER by Technical_round_score DESC
                LIMIT 10;
            """,

            "Students who completed Masters🧑‍💻 ":"""
                SELECT * 
                FROM Final_Statement_Report
                WHERE Degree in ("M.tech","ME","MCA","M.sc");
                """,

            "🔝Top 10 in Python Problem Solving": """
                SELECT *
                FROM final_statement_report
                ORDER BY Problems_solved_python DESC
                LIMIT 10;
            """,

            "Student who completed Assessments✅ ": """
                SELECT *
                FROM Final_Statement_Report
                WHERE  Assessments_completed =10;
            
            """,
            "Distribution of Placement status🎯":"""
                
                SELECT Placement_status, count(*) as count
                FROM Final_Statement_Report
                GROUP BY Placement_status;
            """,

            "🔝Top 10 Student based on Leadership quality🧑‍💼":"""
                SELECT * 
                FROM Final_Statement_Report
                ORDER BY Leadership DESC
                LIMIT 10;
            """,

             "🔝Top Female Student ready for interviews":  """
        
                SELECT *
                FROM Final_Statement_Report
                WHERE Gender = 'Female'
                ORDER BY Technical_round_score DESC
                LIMIT 10;
            """,

            "🔝Top 10 Student in sql":""" 
                SELECT *
                FROM Final_Statement_Report
                ORDER BY Problems_solved_sql DESC
                LIMIT 10;

            """,
            "🔝Top Student who solved most problems python and sql":""" 
                SELECT *
                FROM Final_Statement_Report
                WHERE Problems_solved_python>=450 AND
                Problems_solved_sql>=450;

            """,

            "🔝Top 10 Student with the highest scores in the latest project":"""
                SELECT *
                FROM Final_Statement_Report
                WHERE Placement_status = 'Ready'
                ORDER BY Latest_project_score DESC
                LIMIT 10;

                       
             """
        }
        
        selected_query = st.selectbox("📌 Select a query", list(query_options.keys()))


        try:
            conn = connect_to_mysql()
            cursor = conn.cursor()
            cursor.execute(query_options[selected_query])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result_df = pd.DataFrame(rows, columns=columns)
            cursor.close()
            conn.close()

        
            st.dataframe(result_df, use_container_width=True)

            if selected_query=="Distribution of Placement status🎯":
                st.subheader("Distribution of Placement status")
                labels = ['Placed', 'Ready', 'Not-Ready']
                sizes = [168, 154, 178]  
                colors = ['limegreen', 'xkcd:pale yellow', 'xkcd:light red']


                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  


                st.pyplot(fig)

            if selected_query=="Distribution of Soft skills📈":
                st.subheader("Distribution of Soft skills📈")
                avg_ssc=[87.59,87.55,87.71,87.60,82.82,75.09,88.91]
                ssc_lab=["Communication", "Teamwork","Presentation","Leadership",
                         "Critical_thinking","Problem_solving",
                           "Interpersonal_skills"
                           
                        ]

                fig, ax = plt.subplots()
                ax.bar(ssc_lab, avg_ssc, color='skyblue')
                ax.set_ylabel('Average Score')
                ax.set_xlabel('Soft Skills')
                ax.set_title('Average Scores of Soft Skills')
                plt.xticks(rotation=45)
                st.pyplot(fig)


                
            if selected_query=="Who got selected more - Male or Female🥇?":
                st.subheader("Who are more Male or Female")
                labels = ['Male', 'Female']
                sizes = [75,93]  
                colors = ['xkcd:light red', 'limegreen']


                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  


                st.pyplot(fig)    

            if selected_query=="Which Batch performed best in Placements in last 2 years📅?":
                result = [('April', 2022, 18), ('Nov', 2022, 19), ('April', 2023, 12), ('Nov', 2023, 22)]
                df_chart = pd.DataFrame(result, columns=['Course Batch', 'Enrollment Year', 'Placed Count'])


                fig, ax = plt.subplots(figsize=(6, 4))
                for year in sorted(df_chart['Enrollment Year'].unique()):
                  sub_df = df_chart[df_chart['Enrollment Year'] == year]
                  ax.bar(sub_df['Course Batch'] + f" {year}", sub_df['Placed Count'], label=str(year))

                  ax.set_title("📊 Placements by Course Batch (2022 & 2023)")
                  ax.set_xlabel("Batch & Year")
                  ax.set_ylabel("Number of Placed Students")
                  ax.legend()
                  st.pyplot(fig)

        except Exception as e:
            st.error(f" Error running the query: {e}")


    elif filter_type == "✍️ Custom Filter":
        st.subheader("Enter your custom condition below✏️:")
        column = st.selectbox("Select Column", df.columns.tolist())
        condition = st.selectbox("Condition", [">", "<", ">=", "<=", "=", "!="])
        value = st.text_input("Value (example: 75)")

        if st.button("Apply Filter🪄"):
            try:
                query = f"SELECT * FROM Final_Statement_Report WHERE {column} {condition} {value};"
                conn = connect_to_mysql()
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                result_df = pd.DataFrame(rows, columns=columns)
                cursor.close()
                conn.close()

                if not result_df.empty:
                    st.dataframe(result_df, use_container_width=True)
                else:
                    st.warning("No matching records found.")
            except Exception as e:
                st.error(f"Error: {e}")