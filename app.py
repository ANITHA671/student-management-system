import pandas as pd
import streamlit as st
import sqlite3

conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    subject TEXT,
    marks INTEGER
)
""")
conn.commit()

st.title("🎓 Student Management System")

st.header("Add Student")
name = st.text_input("Name")
age = st.number_input("Age", 1, 100)
subject = st.text_input("Subject")
marks = st.number_input("Marks", 0, 100)

if st.button("Add"):
    cursor.execute(
        "INSERT INTO students (name, age, subject, marks) VALUES (?,?,?,?)",
        (name, age, subject, marks)
    )
    conn.commit()
    st.success("Student added successfully!")

st.header("All Students")
df = pd.read_sql("SELECT * FROM students", conn)
st.dataframe(df)

st.header("Pass Percentage")
pass_percent = pd.read_sql(
    "SELECT SUM(marks>=40)*100.0/COUNT(*) AS pass_percentage FROM students",
    conn
)
st.write(pass_percent)

st.header("Average Marks per Subject")
avg_df = pd.read_sql(
    "SELECT subject, AVG(marks) AS avg_marks FROM students GROUP BY subject",
    conn
)
st.dataframe(avg_df)
