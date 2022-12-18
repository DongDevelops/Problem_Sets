from cs50 import get_string

userInput = get_string("Text: ")

A = len(userInput)
userInput[A]

L = 0
S = 0


L += 1

S += 1

calculate = 0.0588 * L - 0.296 * S - 15.8

if calculate >= 16:
    print("Grade 16+")

if calculate < 1:
    print("Before Grade 1")


print(f"Grade {}")
