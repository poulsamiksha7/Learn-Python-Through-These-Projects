import random
import json
import time


def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)["questions"]


def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    return random.sample(questions, num_questions)


def ask_question(question):
    print()
    print(question["question"])

    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    try:
        number = int(input("Select the correct number: "))
    except ValueError:
        print("Invalid input, counted as wrong.")
        return False

    if number <= 0 or number > len(question["options"]):
        print("Invalid choice, counted as wrong.")
        return False

    return question["options"][number-1] == question["answer"]


questions = load_questions()


while True:
    total_questions = int(input("Enter number of questions: "))

    if total_questions <= 0:
        print("Please enter at least 1 question.")
    else:
        break


random_questions = get_random_questions(
    questions,
    total_questions
)

correct = 0
start_time = time.time()

for question in random_questions:

    is_correct = ask_question(question)

    if is_correct:
        print("Correct ✅")
        correct += 1
    else:
        print("Wrong ❌")

    print("---------------------")


completed_time = time.time() - start_time

score = round((correct / total_questions) * 100, 2)


with open("score_card.txt", "a") as f:
    f.write(
        f"Score: {score}% | "
        f"Correct: {correct}/{total_questions} | "
        f"Time: {round(completed_time,2)} seconds\n"
    )


print("\nSummary")
print("Total Questions:", total_questions)
print("Correct Answers:", correct)
print("Score:", f"{score}%")
print("Time:", round(completed_time,2), "seconds")