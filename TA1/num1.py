def count_characters(input_string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_others = 0

    for char in input_string:
        if not char.isalpha() and not char.isspace():
            print("Error: Contains special characters or numbers.")
            return

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif char.isspace():
            num_spaces += 1
        else:
            num_others += 1

    print(f"Vowels: {num_vowels}")
    print(f"Consonants: {num_consonants}")
    print(f"Spaces: {num_spaces}")

input_string = input("Input any letter from the Alphabet: ")
count_characters(input_string)
