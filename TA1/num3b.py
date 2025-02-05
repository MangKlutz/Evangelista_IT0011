def pattern_b():
    i = 1
    while i <= 5:
        # Print leading spaces
        j = 1
        while j <= 5 - i:
            print(" ", end="")
            j += 1
        # Print numbers
        k = 1
        while k <= (2 * i - 1):
            print(i, end="")
            k += 1
        i += 1
        print()

pattern_b()
