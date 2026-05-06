classroom = []

#  Function
def generate_status(grade):
    if grade >= 80:
        return "Distinction"
    elif grade >= 50:
        return "Pass"
    else:
        return "Redo"

# 3. Input Loop
while True:
    name = input("Enter student name (or 'exit'): ")
    
    if name.lower() == "exit":
        break
    
    score = int(input("Enter score: "))

    # 4. Storage (dictionary)
    student = {
        "name": name,
        "score": score,
        "status": generate_status(score)
    }

    classroom.append(student)

# 5. Final Report

for student in classroom:
    print(f"{student['name']} - {student['score']}: {student['status']}")