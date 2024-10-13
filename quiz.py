# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final results when quiz is completed

quiz = {
    "Question 1": {
        "Question": "What is the capital of France?",
        "Answer": "Paris"
    },
    "Question 2": {
        "Question": "What is the capital of Germany?",
        "Answer": "Berlin"
    },
    "Question 3": {
        "Question": "What is the capital of Italy?",
        "Answer": "Rome"
    },
    "Question 4": {
        "Question": "What is the capital of Spain?",
        "Answer": "Madrid"
    },
    "Question 5": {
        "Question": "What is the capital of Portugal?",
        "Answer": "Lisbon"
    },
    "Question 6": {
        "Question": "What is the capital of Switzerland?",
        "Answer": "Bern"
    },
    "Question 7": {
        "Question": "What is the capital of Austria?",
        "Answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['Question'])
    answer = input("Answer")

    if answer.lower() == value['Answer'].lower():
        print('Correct')
        score += 1
        print("Your score is: " + str(score))

    else:
        print("Wrong")
        print("The answer is : " + value['Answer'])
        print("Your score is: " + str(score))


print("You got " + str(score) + " out of 7 Questions correctly")
print("Your percentage is " + str(int(score/7*100)) + "%")

