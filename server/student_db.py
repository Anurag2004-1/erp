import psycopg2
from server.datatype import Student
def get_db_connection_postgres():
    conn = psycopg2.connect(
        host="localhost",
        database="student",
        user="postgres",
        password="palash",
        port="5432"
    )
    conn.autocommit = True
    create_db_and_tables(conn)
    return conn

def create_db_and_tables(conn):
    cursor = conn.cursor()
    # Fixed SQL Syntax
    ddl = """ 
    CREATE TABLE IF NOT EXISTS erp_student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        enrolment_id VARCHAR(100) NOT NULL UNIQUE
    )
    """
    cursor.execute(ddl)
    conn.commit()
    cursor.close()

def add_student_database(name: str, enrollment: str):
    ddl = "INSERT INTO erp_student (name, enrolment_id) VALUES (%s, %s)"
    with get_db_connection_postgres() as connection:
        with connection.cursor() as cursor:
            cursor.execute(ddl, (name, enrollment))


def search_student_db(enrollment: str):

    ddl = "SELECT name, enrolment_id FROM erp_student WHERE enrolment_id = %s"
    with get_db_connection_postgres() as connection:
        with connection.cursor() as cursor:
            cursor.execute(ddl, (enrollment,))
            student = cursor.fetchone()  # Fetch result
            if student:
                print("Student Found:", student)
            else:
                print(" No student found with that enrollment ID.")
            return Student(name=student[0], enrollment=student[1])
print(search_student_db(enrollment="test"))