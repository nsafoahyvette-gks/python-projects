# ==========================================
# YVETTE MENSAH NSAFOAH
# GKS PORTFOLIO - GRADE CALCULATOR
# ==========================================

def get_score(subject):
    while True:
        try:
            score = float(input(f"Enter your score for {subject} (0-100): "))

            if 0 <= score <= 100:
                return score

            print("❌ Score must be between 0 and 100.")

        except ValueError:
            print("❌ Please enter a valid number.")


def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def get_remark(score):
    if score >= 80:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 50:
        return "Pass"
    elif score >= 40:
        return "Needs Improvement"
    else:
        return "Fail"


def calculate_average(scores):
    return sum(scores.values()) / len(scores)


def display_results(scores):
    average = calculate_average(scores)

    print("\n" + "=" * 60)
    print("              GRADE REPORT")
    print("=" * 60)

    print(f"{'Subject':<25}{'Score':<10}{'Grade':<10}{'Remark'}")
    print("-" * 60)

    for subject, score in scores.items():
        grade = get_grade(score)
        remark = get_remark(score)

        print(f"{subject:<25}{score:<10.1f}{grade:<10}{remark}")

    print("-" * 60)

    overall_grade = get_grade(average)
    overall_remark = get_remark(average)

    print(f"Average: {average:.2f}%")
    print(f"Overall Grade: {overall_grade}")
    print(f"Overall Performance: {overall_remark}")

    print("=" * 60)


def main():
    print("\n" + "=" * 60)
    print("           YVETTE'S GRADE CALCULATOR")
    print("=" * 60)

    print("\nEnter your scores for your subjects.")

    subjects = [
        "English",
        "Core Mathematics",
        "Elective Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Social Studies"
    ]

    scores = {}

    for subject in subjects:
        scores[subject] = get_score(subject)

    display_results(scores)

    print("\n📚 Keep working toward your goals!")
    print("🇬🇭 Ghana → 🇰🇷 Korea")


if __name__ == "__main__":
    main()