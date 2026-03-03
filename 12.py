students=["chandan","darshan","narendra"]
marks=[85,75,90]
student_marks={}
print(student_marks)
for index , students in enumerate(students):
    student_marks[students]=marks[index]
print(student_marks)