import pandas as pd
import streamlit as st
import mysql.connector

# ---------------- MySQL Connection ----------------
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="studentuser",
    password="student123",
    database="studentdb",
    auth_plugin="caching_sha2_password"
)

print("✅ Connected Successfully")

cursor = conn.cursor()

# ---------------- Streamlit UI ----------------
st.title("🎓 Student Management System")

# Add Student Section
st.header("Add Student")
name = st.text_input("Name")
age = st.number_input("Age", 1, 100)
subject = st.text_input("Subject")
marks = st.number_input("Marks", 0, 100)

if st.button("Add"):
    cursor.execute(
        'INSERT INTO students (name, age, subject, marks) VALUES (%s,%s,%s,%s)',
        (name, age, subject, marks)
    )
    conn.commit()
    st.success("Student added successfully!")

# View All Students
st.header("All Students")
df = pd.read_sql("SELECT * FROM students", conn)
st.dataframe(df)
st.header("Pass Percentage")
pass_percent = pd.read_sql(
    "SELECT SUM(marks>=40)*100/COUNT(*) AS pass_percentage FROM students",
    conn
)
st.write(pass_percent)

# ---------------- AVERAGE MARKS PER SUBJECT ----------------
st.header("Average Marks per Subject")
avg_df = pd.read_sql(
    "SELECT subject, AVG(marks) AS avg_marks FROM students GROUP BY subject",
    conn
)
st.dataframe(avg_df)

