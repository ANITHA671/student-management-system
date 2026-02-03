# Student Management System

A web-based application to manage student records using **Streamlit**, **Python**, and **MySQL**.  

It allows you to **add, view, update, and delete students**, calculate statistics like **average marks, pass percentage, top scorer**, and visualize data with **bar charts and pie charts**.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** MySQL  
- **Libraries:** pandas, mysql-connector-python, matplotlib  

---

## 📂 Database Table Example

**Table Name:** `students`  

| Column  | Type          | Notes                        |
|---------|---------------|-------------------------------|
| id      | INT           | Primary Key, Auto Increment   |
| name    | VARCHAR(50)   | Student Name                  |
| age     | INT           | Age of Student                |
| subject | VARCHAR(50)   | Subject Name                  |
| marks   | INT           | Marks obtained                |

**SQL to create table:**

```sql
CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    subject VARCHAR(50),
    marks INT
);
