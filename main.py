import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ask_question(number, question, options, correct_option, explanation):
    print(f"\nQuestion {number}: {question}")
    for key, value in options.items():
        print(f"  {key}) {value}")

    user_choice = input("Your answer (A, B, C, or D): ").strip().upper()
    while user_choice not in options:
        user_choice = input("Please enter A, B, C, or D only: ").strip().upper()

    if user_choice == correct_option:
        print("✅ Correct!", explanation)
        return 5
    else:
        print(f"❌ Incorrect. The correct answer was {correct_option}) {options[correct_option]}.")
        print("ℹ️", explanation)
        return 0

def show_intro():
    print("=" * 50)
    slow_print("🏏 Welcome to the Ultimate Cricket Quiz! 🧠", 0.04)
    print("=" * 50)
    slow_print("Test your cricket knowledge across formats and legends!", 0.02)
    print()

def final_feedback(score):
    print("\n🎉 Quiz Complete! 🎉")
    print(f"Your final score: {score}/25\n")

    if score == 25:
        print("🏆 Incredible! You're a cricket legend!")
    elif score >= 15:
        print("👏 Great effort! You really know your cricket.")
    elif score >= 5:
        print("👍 Not bad. Keep watching and learning!")
    else:
        print("📚 Time to brush up on your cricket knowledge!")

def play_quiz():
    questions = [
        {
            "question": "Who scored the fastest T20 century?",
            "options": {
                "A": "Chris Gayle",
                "B": "AB de Villiers",
                "C": "Sahil Chauhan",
                "D": "Rohit Sharma"
            },
            "answer": "C",
            "explanation": "Sahil Chauhan scored a century in just 27 balls for Estonia in 2024."
        },
        {
            "question": "Who has taken the most wickets in Test cricket?",
            "options": {
                "A": "James Anderson",
                "B": "Shane Warne",
                "C": "Anil Kumble",
                "D": "Muttiah Muralitharan"
            },
            "answer": "D",
            "explanation": "Muralitharan holds the record with 800 Test wickets."
        },
        {
            "question": "Who won the 2023 Cricket World Cup?",
            "options": {
                "A": "India",
                "B": "England",
                "C": "Australia",
                "D": "Pakistan"
            },
            "answer": "C",
            "explanation": "Australia defeated India in the final to win the 2023 World Cup."
        },
        {
            "question": "What is the New Zealand Men’s cricket team known as?",
            "options": {
                "A": "All Blacks",
                "B": "Blackcaps",
                "C": "Kiwi Smashers",
                "D": "Southern Blasters"
            },
            "answer": "B",
            "explanation": "‘Blackcaps’ is the official nickname for NZ's men's team."
        },
        {
            "question": "Who holds the highest individual score in Test cricket?",
            "options": {
                "A": "Virender Sehwag",
                "B": "Brian Lara",
                "C": "Don Bradman",
                "D": "David Warner"
            },
            "answer": "B",
            "explanation": "Brian Lara scored 400 not out vs England in 2004."
        }
    ]

    score = 0
    for idx, q in enumerate(questions, 1):
        score += ask_question(idx, q["question"], q["options"], q["answer"], q["explanation"])
        time.sleep(1)

    final_feedback(score)

def main():
    show_intro()
    while True:
        play_quiz()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for playing the Cricket Quiz! 🏏 See you next time!")
            break

if __name__ == "__main__":
    main()
