def uppercase(str):
    for char in str:
        # Check if character is lowercase using ASCII range
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        # Use string format with end="" to print characters on the same line
        print("{}".format(char), end="")
    # Final print for the new line
    print("")

