student_records = {}
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {
        "age": age,
        "grades": set(),
        "courses": set(courses)
    }
    print(f"Student '{name}' added successfully.")

def add_grade(name,grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["grades"].add(grade)
    print(f"Grade {grade} added for student '{name}'.")    

def is_enrolled(name,course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    grade_set=student_records[name]["grades"]
    if not grade_set:
        return 0.0
    return float(sum(grade_set)/len(grade_set))
def list_student_by_course(name,course):
    if course in courses:
        return list_students_by_course

def list_students_by_course(course):
    enrolled_students = []
    
    
    for name, info in student_records.items():
        
        if course in info["courses"]:
            enrolled_students.append(name)
            
    return enrolled_students
 
    
        


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list