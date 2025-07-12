# Get the size of the pattern from the user
size = int(input("Enter the size of the pattern: "))

# Input validation (good practice to ensure 'size' is positive)
if size <= 0:
    print("Please enter a positive integer for the size.")
else:
    # Use a while loop for the rows
    row_count = 0
    while row_count < size:
        # Use a for loop for the columns within each row
        for col_count in range(size):
            # Print an asterisk without a newline, and no space after each asterisk
            # to ensure a compact square. If you want spaces between asterisks, use " *"
            print("*", end="")
        
        # After printing all asterisks for a row, move to the next line
        print()
        
        # Increment the row counter for the while loop
        row_count += 1