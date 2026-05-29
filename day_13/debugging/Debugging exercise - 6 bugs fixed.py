# Day 13 - Debugging Exercise: Student Grade Manager
# Find and fix all 6 bugs in this code

students = {
    "Alice": 92,
    "Bob": 85,
    "Carlos": 73,
    "Diana": 68,
    "Elena": 55,
    "Frank": 41,
}

def get_grade(score):
    """Return a letter grade based on score."""
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"


def print_report(student_dict):
    """Print each student's name, score, and grade."""
    print("=" * 40)
    print("STUDENT GRADE REPORT")
    print("=" * 40)

    passing_count = 0
    failing_count = 0

    for name in student_dict: #Where is student_dict
        score = student_dict[name]
        grade = get_grade(score)
        print(f"{name}: {score} points -> Grade {grade}") """FIX THIS FUNCTION FIRST This function get the student's name, score and grade."""

        if grade != "F":
            passing_count += 1
        else:
            failing_count += 1

    print("=" * 40)
    total = passing_count + failing_count
    pass_rate = passing_count / total * 100
    print(f"Passing: {passing_count}/{total} ({pass_rate}%)")
    print(f"Failing: {failing_count}/{total}")


def get_top_student(student_dict):
    """Return the name of the student with the highest score."""
    top_name = ""
    top_score = 0

    for name, score in student_dict:
        if score >= top_score:
            top_name = name
            top_score = score

    return top_name


def add_student(student_dict):
    """Prompt user to add a new student."""
    new_name = input("Enter student name: ")
    new_score = input("Enter student score: ")

    if new_score < 0 or new_score > 100:
        print("Invalid score. Must be between 0 and 100.")
    else:
        student_dict[new_name] = new_score
        print(f"{new_name} added with score {new_score}.")


print_report(students)

top = get_top_student(students)
print(f"\nTop student: {top}")

add_student(students)
print_report(students)
