def illuminati(height):
    for x in range(height):
        if x == (height-1):
            print("/", (height - 1) * 2 * "_", "\\", sep="")
        else:
            print(" " * (height - x - 1), "/", (x * 2) * " ", "\\", sep="")

illuminati(3)