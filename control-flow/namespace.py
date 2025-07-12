def counting_function():
    print("Counts for count!")
    count = 0
    print("Entry point.")
    count += 1
    print(f"This is count {count}.")
    count += 5
    print (f"This is count {count}.")
    
def logging_function():
    print("Logging in!!!")
    count = 1
    print(f"This is log entry {count}.")
    count = 2
    print(f"This is log entry {count}")

Global = 100

#Calling the functions
counting_function()
logging_function()

print(f"This is Global function {Global}")
