import sqlite3

def connect_db():
    return sqlite3.connect("student.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      grade TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_student(name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

def retrieve_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(student_id, name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    insert_student("Alice", 20, "A")
    insert_student("Bob", 22, "B")
    print("Initial Data:", retrieve_students())
    update_student(1, "Alice Smith", 21, "A+")
    print("After Update:", retrieve_students())
    delete_student(2)
    print("After Deletion:", retrieve_students())

if __name__ == "__main__":
    main()