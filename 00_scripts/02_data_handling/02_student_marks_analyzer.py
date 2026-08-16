import csv

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to exit: ").strip()

        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
           marks = float(input(f"Enter marks for {name}: "))
           students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")

    return students

def display_report(students={}):
    if not students:
        print("No student data")
        return

    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    avarage = sum(marks) / len(students)

    topper = [name for name, score in students.items() if score == max_score]
    bottomer = [name for name, score in students.items() if score == min_score]

    print("\n Students marks report")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"Average marks for students: {avarage:.2f}")
    print(f"Highest marks : {max_score} by {', '.join(topper)}")
    print(f"Lowest marks : {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks")

    for name, score in students.items():
        print(f" - {name}: {score}")

students = collect_student_data()
display_report(students)