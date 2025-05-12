import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='student_db'
    )

def insert_student(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, math_grade, science_grade, english_grade FROM students")
    result = cursor.fetchall()
    conn.close()
    return result


def update_student(student_id, name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s WHERE id=%s", (name, age, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()

def search_students(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, name, age, math_grade, science_grade, english_grade 
    FROM students 
    WHERE name LIKE %s
""", (f"%{name}%",))
    result = cursor.fetchall()
    conn.close()
    return result

def update_student_grade(student_id, subject, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"UPDATE students SET {subject}_grade = %s WHERE id = %s"
    cursor.execute(query, (grade, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def numeric_to_letter(grade):
    if grade >= 94:
        return "A"
    elif grade >= 90:
        return "A-"
    elif grade >= 86:
        return "B+"
    elif grade >= 82:
        return "B"
    elif grade >= 78:
        return "B-"
    elif grade >= 74:
        return "C+"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


