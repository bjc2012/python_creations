 # This multiple choice quiz contains 3 NBA related questions that test your history of the game
 # To pass the quiz, you must answer all three questions correctly

from quiz import Question

question_prompts = [
    "What year was the game of basketball invented?\n(a) 1891\n(b) 1908\n(c) 1999",
    "Which player has scored the most points in NBA History?\n(a) Michael Jordan\n(b) LeBron James\n(c) Kareem Abdul-Jabbar\n(d) Kobe Bryant",
    "Which team has the most NBA championships?\n(a) Lakers\n(b) Celtics\n(c) Bulls\n(d) Lakers and Celtics are both tied for 17 championships"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            
    print("You answered " + str(score) + "/" + str(len(questions)) + " correctly")


run_test(questions)   