from student_db import add_student_database,search_student_db
def add_student():
    name = input("Enter your name: ")
    enrollment = input("Enter your enrollment: ")
    add_student_database(name,enrollment)
    print("student_added_successfully")
if __name__ == '__main__':
    add_student()



