# student data
students = [
    {"name": "Alice", "scores": [90, 88, 95]},
    {"name": "Brian", "scores": [70, 75, 68]},
    {"name": "Cynthia", "scores": [85, 80, 82]},
    {"name": "David", "scores": [50, 60, 55]},
    {"name": "Ella", "scores": [92, 95, 98]},
    {"name": "Chacha", "scores":[50, 50, 30,]},
]

# assign grades
for record in students:
    avg = sum(record["scores"]) / len(record["scores"])
    record["average"] = round(avg, 2)

    if avg >= 90:
        record["grade"] = "A"
    elif avg >= 75:
        record["grade"] = "B"
    elif avg >= 60:
        record["grade"] = "C"
    elif avg >= 45:
        record["grade"] = "D"
    else:
        record["grade"] = "F"

# Search by student name
while True:
    name = input("\nEnter student name:").strip()

    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print("Succesfull fetch student data")
            print(f"\nStudent: {s['name']}")
            print(f"Scores: {s['scores']}")
            print(f"Average: {s['average']}")
            print(f"Grade: {s['grade']}")
            found = True
            break

    if not found:
        print("Student not found. Please Try again with a valid name from students data.")
   
   