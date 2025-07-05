num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+" :
        result = num_1 + num_2
        print("The result is: ", result)
    case "-":
        result = num_1 - num2
        print("The result is: ", result)
    case "*":
        result = num_1 * num_2
        print("The result is: ", result)
    case "/":
        if num_2 == 0:
            print("Cannot divide by zero.")   
        else:
            result = num_1/num_2
            print("The result is: ",result)    

        