correctAnswers = 0

print("Welcome to the space quiz\n\n")

print("1. What is the smallest planet?")
answer = input()

if answer == "mercury":
    print(answer + " is correct\n")
    correctAnswers += 1
else:
    print(answer + " is incorrect\n")


print("2. What is the hottest planet?")
answer = input()

if answer == "venus":
    print(answer + " is correct\n")
    correctAnswers += 1
else:
    print(answer + " is incorrect\n")

print(f"Total correct answers: {correctAnswers}")