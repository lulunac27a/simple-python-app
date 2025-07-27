# a simple Python app
print("This is a simple Python app.")  # print simple text
input_text = input("Enter text: ")  # prompt text for input
print(input_text)  # print variable to entered text input
print("Length: ", len(input_text))  # print length of entered text
print("Uppercase output: ", input_text.upper())  # print text in uppercase
print("Lowercase output: ", input_text.lower())  # print text in lowercase
print("Titlecase output: ", input_text.title())  # print text in titlecase
print(
    "Capitalized output: ", input_text.capitalize()
)  # print text in capitalized (first letter only)
print("Reversed output: ", input_text[::-1])  # print text in reverse
