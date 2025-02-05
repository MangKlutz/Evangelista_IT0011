def pattern_a():
    for i in range(1, 6):
        # Print leading spaces
        for j in range(5 - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end="")
        print()

pattern_a()
