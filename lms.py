import sys

def calculate_average_score(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def performance_status(avg_score):
    if avg_score >= 85:
        return "Excellent Performance"
    elif avg_score >= 70:
        return "Good Performance"
    elif avg_score >= 50:
        return "Average Performance"
    else:
        return "Needs Improvement"

if __name__ == "__main__":
    script_name = sys.argv[0]

    if len(sys.argv) >= 4:
        student_name = sys.argv[1]
        course_name = sys.argv[2]
        scores = list(map(int, sys.argv[3:]))
        print("User provided LMS details:")
    else:
        student_name = "Sneha"
        course_name = "Python Programming"
        scores = [78, 85, 90, 80]
        print("No input given - using default values:")

    avg_score = calculate_average_score(scores)
    status = performance_status(avg_score)

    print("\n========== Learning Management System Report ==========")
    print("Script Name:", script_name)
    print("Student Name:", student_name)
    print("Course Name:", course_name)
    print("Scores:", scores)
    print("Average Score:", round(avg_score, 2))
    print("Performance Status:", status)