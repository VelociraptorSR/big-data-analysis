import json

students = []

id_counter = len(students)

def save_to_json():
    global students
    with open("students.json", mode = "w") as file:
        json.dump(students, file, indent = 4)
    print("Data saved successfully. ")

def load_from_json():
    global students
    try:
        with open("students.json", mode = "r") as file:
            students = json.load(file)
        print("Data load successfully. ")
    except FileNotFoundError:
        print("File not found. ")

def enroll_student():
    global id_counter
    try:
        print("--------Adding Student--------")
        name = input("Enter the name of student: ").strip()
        if name == "":
            print("Please retry name cannot be empty. ")
            return
        course = input("Enter the enrolled course of student: ").strip()
        if course == "":
            print("Please retry course cannot be empty. ")
            return
        marks = float(input("Enter the obtained marks of student: "))
        if 0>marks or marks>100:
            print("Please retry. Enter marks between 0 to 100 ")
            return
        
        grade = grade_assign(marks)
        
        students.append({'id': id_counter+1, 'name': name, 'course': course, 'marks': marks, 'grade': grade})
        id_counter += 1
        print("Student record added successfully. ")
    except ValueError:
        print("Please try with correct value: ")
        
def grade_assign(marks):
    if marks>=85:
        return "A"
    if 85>marks>=70:
        return "B"
    if 70>marks>=50:
        return "C"
    if marks<50:
        return "F"
        
def cohort_directory():
    if len(students) == 0:
        print("No records in the file. ")
    else:
        display(students)
    
def query_record():
    try:
        print('1. Search by id')
        print('2. Search by course name')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            search_by_id()
        elif choice == 2:
            search_by_course()
        else:
            print("Invalid choice. Please retry. ")
    except:
        print("Please try again with integer input. ")

def search_by_id():
    try:
        pid = int(input("Enter the id of student: "))
        result = [p for p in students if p['id'] == pid]
        if not result:
            print(f"No record foound for Id = {pid} ")
            return None
        display(result)
    except:
        print("Please try again with integer input. ")

def search_by_course():
    course = input("Enter the course: ")
    result = [p for p in students if p['course'] == course]
    if not result:
        print(f"No record foound for Course = {course} ")
        return None
    display(result)

def revise_evaluation():
    try:
        pid = int(input("Enter the id of student: "))
        result = [p for p in students if p['id'] == pid]
        if not result:
            print(f"No record foound for Id = {pid} ")
            return None
        name = input("Enter the name of student: ").strip()
        if name != "":
            result[0]['name'] = name
        course = input("Enter the enrolled course of student: ").strip()
        if course != "":
            result[0]['course'] =course
        marks = float(input("Enter the obtained marks of student: "))
        if 0>marks or marks>100:
            print("Please retry. Enter marks between 0 to 100 ")
            return
        result[0]['marks'] = marks
        grade = grade_assign(marks)
        result[0]['grade'] = grade
        print("Student record updated successfully. ")
        
    except ValueError:
        print("Please try with correct value: ")

def display(result):
    print("----------Students Data----------")
    print("-"*70)
    print(f"{'Id':^5}{'Name':<20}{'Course':<20}{'Marks':>10}{'Grade':>10}")
    print("-"*70)
    for p in result:
        pid, name, course, marks, grade = p.values()
        print(f"{pid:^5}{name:<20}{course:<20}{marks:>10}{grade:>10}")   
    print("-"*70)
    return
    
def purge_record():
    try:
        pid = int(input("Enter the id of student: "))
        result = [p for p in students if p['id'] == pid]
        if len(result) == 0:
            print(f"No record foound for Id = {pid} ")
            return
        pid, name, course, marks, grade = result[0].values()
        print(f"Id     : {pid}")
        print(f"Name   : {name}")
        print(f"Course : {course}")
        print(f"Mark   : {marks}")
        print(f"Grade  : {grade}")
        del_do = input("Do you want to delete this record (y/n): ")
        if del_do.lower() == "y":
            students.remove(result[0])
            print("Record deleted successfully. ")    
    except:
        print("Please try again with integer input. ")

def menu():
    menu_text = '''         1. Enroll Student
         2. Cohort Directory
         3. Query Records
         4. Revise Evaluation
         5. Purge Record
         6. Save to JSON
         7. Load From JSON
         8. Terminate'''
    print("----------Continuos Evaluation & Transcrit Persistence System----------")
    print(menu_text)
    try:
        choice = int(input("Enter choice: "))
    except:
        choice = -1
    return choice

def main():
    load_from_json()
    while True:
        choice = menu()
        
        match choice:
            case 1:
                enroll_student()
            case 2:
                cohort_directory()            
            case 3:
                query_record()
            case 4:
                revise_evaluation()
            case 5:
                purge_record()
            case 6:
                save_to_json()
            case 7:
                load_from_json()
            case 8:
                break
            case _:
                print("Invalid Choice. Please retry. ")
            
                
if __name__ == "__main__":
    main()
    
    