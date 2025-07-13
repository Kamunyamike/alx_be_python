#Create a custom exception class called ValueTooHighError that inherits from the Exception class.
#Write a program that takes a number as input and raises a ValueTooHighError 
#exception if the number is greater than 100.
class ValueTooHighError(Exception):
    def __init__(self, value, message = "Value too high. Try a number below 100."):
        self.value = value
        self.message = message
        super(). __init__(self.message)
    
def process_number(number):
    if number > 100:
        raise ValueTooHighError(f"{number} is higher than 100.")
    else:
        return (f"The number {number} is less or equal to 100.")
if __name__ == "__main__":
    while True:
        try: 
            user_input = input("Enter your preffered number: ")
            if user_input.lower() == "quit":
                print("Exiting program")
                break
            else: 
                number = int(user_input)
                result = process_number(number)
                print(result)

        except ValueError:
            print("Invalid input. Please put a valid number.")
        except ValueTooHighError as e:
            print(f"Error: {e.message} You entered {e.value}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
