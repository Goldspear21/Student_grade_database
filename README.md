<h1 align="center" id="title">Student Grade Database</h1>

<p align="center">
  <img src="https://socialify.git.ci/Goldspear21/Student_grade_database/image?language=1&name=1&owner=1&stargazers=1&theme=Dark" alt="project-banner">
</p>

<p align="center" id="description">
  Student Record Manager built with Python (Miniconda 3), Tkinter GUI, and MySQL; supports CRUD operations, subject-wise grade management, and real-time letter grade calculation.
</p>

---

## 📸 Project Screenshots

<p align="center">
  <img src="https://res.cloudinary.com/dfio7wdjh/image/upload/v1747045984/Screenshot_2025-05-12_143121_ypsmrt.png" width="400"/>
  <img src="https://res.cloudinary.com/dfio7wdjh/image/upload/v1747045985/Screenshot_2025-05-12_143149_wybdna.png" width="400"/>
  <img src="https://res.cloudinary.com/dfio7wdjh/image/upload/v1747045984/Screenshot_2025-05-12_143201_hf6nu9.png" width="400"/>
  <img src="https://res.cloudinary.com/dfio7wdjh/image/upload/v1747045984/Screenshot_2025-05-12_143231_rntfbi.png" width="400"/>
</p>

---

## ✨ Features

- 🖥️ Tkinter-based graphical user interface
- 🗂️ Full CRUD operations (Create, Read, Update, Delete)
- 🔍 Search students by name
- 📊 Manage grades for Math, Science, and English
- 🅰️ Auto-convert numeric grades to letter grades (A–F scale)
- 🖱️ Double-click any student to update subject grades interactively
- 💾 Data stored in a persistent MySQL database
- 📐 Modular file structure following best practices
- ⚠️ Input validation and real-time feedback

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (Miniconda 3)
- MySQL Server
- `mysql-connector-python` (Install via pip)

### Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/Goldspear21/Student_grade_database.git
   cd Student_grade_database
2.Install dependencies:
```bash
pip install mysql-connector-python

3.Set up the MySQL database:


```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  math_grade INT DEFAULT NULL,
  science_grade INT DEFAULT NULL,
  english_grade INT DEFAULT NULL
);
