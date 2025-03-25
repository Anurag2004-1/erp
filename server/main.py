from student_db import add_student_database,search_student_db
from flask import Flask, request, jsonify
import psycopg2
# def add_student():
#     name = input("Enter your name: ")
#     enrollment = input("Enter your enrollment: ")
#     add_student_database(name,enrollment)
#     print("student_added_successfully")

def add_student():
    try:
        data = request.get_json()
        name = data.get('name')
        enrollment = data.get('enrollment')

        if not name or not enrollment:
            return jsonify({"error": "Missing required fields"}), 400

        response = add_student_database(name, enrollment)
        return jsonify(response), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
def search_student():
    enrollment = input("Enter your enrollment: ")
    student = search_student_db(enrollment)
    # data = {"name": sudent[0], "enrollment": sudent[1]}
    print(student._asdict())
def interface():
    user_choice = input("1. to add student \n2. search student\n input your choice")
    while user_choice != "X":
        user_choice = input("1. to add student \n2. search student\n input your choice")
        if user_choice == "1":
            add_student()
            print("student_added_successfully")

        elif user_choice == "2":
            search_student()
            print("here is your student")

        elif user_choice == "X":
            break


if __name__ == '__main__':
    interface()




