# ==========================================
# YVETTE MENSAH NSAFOAH
# GKS PORTFOLIO - QUIZ GAME
# ==========================================

import random


QUESTIONS = [
    {
        "question": "What is the capital city of Ghana?",
        "options": ["A. Kumasi", "B. Accra", "C. Tamale", "D. Cape Coast"],
        "answer": "B",
    },
    {
        "question": "Which language is mainly used to create the structure of a webpage?",
        "options": ["A. HTML", "B. Python", "C. SQL", "D. Java"],
        "answer": "A",
    },
    {
        "question": "What is 15 × 4?",
        "options": ["A. 45", "B. 50", "C. 60", "D. 75"],
        "answer": "C",
    },
    {
        "question": "Which organelle is known as the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Ribosome", "C. Cell wall", "D. Mitochondrion"],
        "answer": "D",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing Utility",
        ],
        "answer": "A",
    },
    {
        "question": "Which gas do humans need for respiration?",
        "options": ["A. Carbon dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B",
    },
    {
        "question": "What is the chemical symbol for oxygen?",
        "options": ["A. Ox", "B. O", "C. C", "D. H"],
        "answer": "B",
    },
    {
        "question": "What is the value of 25% of 200?",
        "options": ["A. 25", "B. 40", "C. 50", "D. 75"],
        "answer": "C",
    },
    {
        "question": "Which keyword is commonly used to define a function in Python?",
        "options": ["A. function", "B. define", "C. func", "D. def"],
        "answer": "D",
    },
    {
        "question": "Which Korean writing system is used to write the Korean language?",
        "options": ["A. Kanji", "B. Hangul", "C. Hiragana", "D. Hanzi"],
        "answer": "B",
    },
]


def show_question(question_data, number, total):
    print("\n" + "=" * 60)
    print(f"Question {number} of {total}")
    print("=" * 60)

    print(question_data["question"])

    for option in question_data["options"]:
        print(option)


def get_answer():
    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("❌ Please enter A, B, C, or D.")


def calculate_percentage(score, total):
    return (score / total) * 100


def get_result_message(percentage):
    if percentage >= 80:
        return "Excellent! 🔥"
    elif percentage >= 70:
        return "Very good! 👏🏾"
    elif percentage >= 60:
        return "Good job! 👍🏾"
    elif percentage >= 50:
        return "You passed, but keep practicing. 📚"
    else:
        return "Keep studying and try again! 💪🏾"


def run_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    score = 0
    total = len(questions)

    print("\n" + "=" * 60)
    print("             YVETTE'S QUIZ GAME")
    print("=" * 60)
    print("Test your knowledge!")
    print(f"You will answer {total} questions.")

    for number, question in enumerate(questions, start=1):
        show_question(question, number, total)

        answer = get_answer()

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {question['answer']}.")

    percentage = calculate_percentage(score, total)

    print("\n" + "=" * 60)
    print("                  RESULTS")
    print("=" * 60)

    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")
    print(get_result_message(percentage))

    print("=" * 60)


def main():
    while True:
        run_quiz()

        again = input("\nWould you like to play again? (Y/N): ").strip().upper()

        if again != "Y":
            print("\n👋 Thanks for playing!")
            print("Keep learning and building! 🇬🇭 → 🇰🇷")
            break


if __name__ == "__main__":
    main()