from cs50 import get_string

userInput = get_string("Text: ")


words = 1
sentences = 0
letters = 0

for i in userInput:
    if i == " ":
        words += 1
    elif i == "." or i == "?" or i == "!":
        sentences += 1
    elif i.isalpha():
        letters += 1

L = letters/words * 100
S = sentences/words * 100
calculate = round(0.0588 * L - 0.296 * S - 15.8)

if calculate >= 16:
    print("Grade 16+")
elif calculate < 1:
    print("Before Grade 1")
else:
    print(f"Grade {calculate}")
