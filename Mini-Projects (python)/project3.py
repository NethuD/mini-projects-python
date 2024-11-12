#Operations

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 17
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
correct = 0
incorrect_questions = []
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True: 
        guess = input(f"Problem #{i + 1}: {expr} = ")
        
        # Input validation
        if guess.isdigit() or (guess[0] == '-' and guess[1:].isdigit()):  # Handling negative answers
            guess = int(guess)
            if guess == answer:
                correct += 1
                print("Correct! Good job.")
                break  # Exit the loop to move to the next problem
            else:
                wrong += 1
                print(f"Wrong! The correct answer is {answer}.")
                incorrect_questions.append((expr, answer))  # Store the incorrect question and its answer
                break  # Exit the loop to move to the next problem
        else:
            print("Please enter a valid number.")

end_time = time.time()
total_time = round(end_time - start_time, 2) 

# Summary
print("---------------------")
print(f"Nice Work! You finished in {total_time} seconds!")
print(f"You got {correct} out of {TOTAL_PROBLEMS} correct.")
print(f"You answered {wrong} questions incorrectly.")

# Display incorrect questions and answers
if wrong > 0:
    print("Here are the questions you answered incorrectly:")
    for expr, answer in incorrect_questions:
        print(f"{expr} = {answer}")

# Impression message
if correct == TOTAL_PROBLEMS:
    print("Excellent work! You got all the answers right!")
elif correct > wrong:
    print("Great job! You answered more questions correctly than incorrectly.")
else:
    print("Keep practicing! You'll get better with more practice.")
