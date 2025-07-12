def perform_operation(num_1,num_2,operation):
    if operation == "add":
        return num_1 + num_2
    elif operation == "subtract":
        return num_1 - num_2
    elif operation == "multiply":
        return num_1 * num_2
    elif operation == "divide":
        if num_2 == 0:
            return "Num_2 cannot have value zero! Put another value other than zero for the denominator."
        else:
            return num_1 / num_2
    else: 
        return "Error: Invalid operator. Please use '+', '-', '*', or '/'."

