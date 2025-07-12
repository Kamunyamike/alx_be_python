def perform_operation(num_1,num_2,operation):
    if operation == "+":
        print(num_1 + num_2)
    elif operation == "-":
        print(num_1 - num_2)
    elif operation == "*":
        print(num_1 * num_2)
    elif operation == "/":
        if num_2 == 0:
            print("Num_2 cannot have value zero! Put another value other than zero for the denominator.")
        else:
            print(num_1 / num_2)
    else: 
        print("Please insert a valid operation to see the outcomes!!!")

