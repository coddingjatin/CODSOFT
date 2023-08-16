from graphics import GraphWin, Entry, Text, Point, Rectangle
import random

# Quiz Questions and Answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "London", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Saturn", "Jupiter"],
        "answer": "Jupiter"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    }
]

def display_welcome_message(win):
    win.setBackground("skyblue")
    title_text = Text(Point(200, 50), "Welcome to the Quiz Game!")
    title_text.setSize(15)
    title_text.setStyle("bold")
    title_text.draw(win)
    rule_text = "You will be presented with "
    rule_text += "\nmultiple-choice questions."
    rule_text += "\nChoose the correct answer for each question."
    rule_text += "\n\nClick anywhere to start the quiz."
    rules = Text(Point(200, 120), rule_text)
    rules.setSize(14)
    rules.draw(win)

    win.getMouse()

    title_text.undraw()
    rules.undraw()

def clear_window(win):
    for item in win.items[:]:
        item.undraw()
def evaluate_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()
def display_feedback(win, is_correct, correct_answer):
    feedback_text = Text(Point(200, 150), "Correct!" if is_correct else f"Incorrect. \nCorrect answer is: {correct_answer}")
    feedback_text.setStyle("bold")
    feedback_text.setSize(16)
    feedback_text.setTextColor("green" if is_correct else "red")
    feedback_text.draw(win)

    win.getMouse()
    feedback_text.undraw()
def calculate_final_score(score, total_questions):
    return score / total_questions * 100

def display_final_results(win, score, total_questions):
    results_text = Text(Point(200, 150), f"Quiz Completed!\nYou answered {score} out of {total_questions} \nquestions correctly.")
    results_text.setSize(18)
    results_text.setStyle("bold")
    results_text.draw(win)

    win.getMouse()
    results_text.undraw()    
def play_again(win):
    again_text = Text(Point(200, 150), "Do you want to play again? (yes/no)")
    again_text.setSize(16)
    again_text.setStyle("bold")
    again_text.draw(win)

    entry = Entry(Point(200, 180), 10)
    entry.setSize(16)
    entry.draw(win)

    win.getMouse()
    choice = entry.getText().strip().lower()

    again_text.undraw()
    entry.undraw()

    return choice == "yes"    
def ask_question(win, question, options):
    question_text = Text(Point(200, 50), question)
    question_text.setSize(16)
    question_text.draw(win)

    y_offset = 90
    user_answer = None

    for i, option in enumerate(options):
        option_text = Text(Point(200, y_offset), f"{i + 1}. {option}")
        option_text.setSize(14)
        option_text.draw(win)
        y_offset += 30

    entry = Entry(Point(200, y_offset + 20), 30)
    entry.setSize(14)
    entry.draw(win)

    submit_text = Text(Point(200, y_offset + 60), "Submit")
    submit_text.setStyle("bold")
    submit_text.setSize(14)
    submit_text.draw(win)

    win.getMouse()
    user_answer = entry.getText().strip()

    entry.undraw()
    submit_text.undraw()

    for option_text in win.items[:]:  # Remove options from the window
        option_text.undraw()

    return user_answer


# ... (rest of the functions remain the same)

def main():
    win = GraphWin("Quiz Game", 400, 300)

    while True:
        display_welcome_message(win)

        random.shuffle(quiz_data)
        total_questions = len(quiz_data)
        score = 0

        for question_data in quiz_data:
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["answer"]

            clear_window(win)

            user_answer = ask_question(win, question, options)
            is_correct = evaluate_answer(user_answer, correct_answer)
            display_feedback(win, is_correct, correct_answer)

            if is_correct:
                score += 1

        display_final_results(win, score, total_questions)

        if not play_again(win):
            break

    win.close()

if __name__ == "__main__":
    main()
