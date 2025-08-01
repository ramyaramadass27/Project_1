 ```
markdown
# 🎓 Placement Eligibility App

The **Placement Eligibility App** is a streamlit tool designed to help institutions and recruiters assess student eligibility
for campus placements. It connects to a **MySQL database**,uses **Pandas** for analyzes student data, provides both
predefined and custom filtering options to identify qualified candidates and displays results interactively using **Streamlit**.

---

## 🧱 Project Workflow

This project follows these main steps:

###   🔶 1. Database  Table Creation (MySQL)
- Created 4 empty tables in MySQL:
  - `Student_table`
  - `Programming_table`
  - `Soft_Skills_table`
  - `Placement_table`

> No data was inserted manually in MySQL.

---

### 🔶 2. Data Population via Python
- Used Python (with Faker module) to generate fake student data and using random library to generate random values to tables 
- Inserted the data into the empty MySQL tables using Python OOP for database interactions

---

### 🔶 3. Table Join in MySQL
- Joined all 4 tables using `INNER JOIN` in MySQL to create:
  - `Final_Report_Statement` (for predefined queries and custom filters)
- create 10+ queries for predefined function
  

---

### 🔶 4. Import to Python (Pandas)
- Loaded `Final_Report_Statement` into Python using Pandas and MySQL connector
- Cleaned and formatted data

---

### 🔶 5. Streamlit App Creation
- Created a Streamlit app with two filter systems:
  - **Predefined Query Filters** (via selectbox)
  - **Custom Condition Filters** (e.g., "mock interview score > 75")

- Added:
  - Top 10 students in leadership
  - Distribution of Soft skills - bar chart
  


## 🚀 Features

- 📋 **Student Table Integration** – Connects to a MySQL database containing student records.
- 🔍 **10+ Predefined Queries** – Quickly access common eligibility filters (e.g., Distribution of Soft skills, Top 10 students in mocnk interview score).
- 🧠 **Custom Filter Builder** – Create dynamic filters based on multiple criteria like techinical round score>75, problems solved>450, etc.
- 📊 **Interactive Dashboard** – Built with Streamlit for a clean and responsive UI.
- 📁 **Data Analysis** – Uses Pandas for efficient data manipulation and display.

---

## 🛠️ Technologies Used

- **Frontend**: Streeamlit
- **Backend**: Python(pandas, matplotlib)
- **Database**: Mysql
- **Libraries**:
     - mysql-connector-python
     - pandas
     - faker
     - random

---
## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/placement-eligibility-app.git
   cd placement-eligibility-app

```
2.Install all required packages:

```
bash
pip install -r requirements.txt

```
3. Set up MySQL database
- Create the 4 tables (student_table, Programming_table, Soft_Skills_table, Placement_table)

4. Run your python scrip to populate the tables:

```
pyhton insert_data.py

```

▶️ Usage
1.Run the Streamlit app

```
streamlit run app.py

```
2. Explore the dashboard
- Select from predefined queries
- Apply custom filters
- View eligible students


📁 File Structure

```
placement-eligibility-app/
│
├── 📁 database/
│   ├── create_tables.sql           # SQL script to create 4 empty tables
│   ├── insert_mock_data.py         # Python script using Faker & random to populate tables
│   ├── join_queries.sql            # SQL JOIN queries to combine student data
│   └── db_config.py                # MySQL connection settings

├── 📁 app/
│   ├── app.py                      # Main Streamlit app
│   ├── predefined_queries.py       # Python functions for 10+ predefined queries
│   ├── custom_filter.py            # Logic for dynamic filtering
│   └── utils.py                    # Helper functions (e.g., formatting, data loading)

├── 📁 data/
│   └── sample_output.csv           # Optional: exported results for testing/demo

├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation

```
👨‍💻 Author
Ramya

