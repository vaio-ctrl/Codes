def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "x"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter the phrase: ")))