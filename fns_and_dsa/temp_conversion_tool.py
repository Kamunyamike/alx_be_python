FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = input("Enter the temperature to convert: ")
state =  input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if state == "F":
    fahrenheit = int(temperature)
    #Function to convert fahrenheit to celcius
    def convert_to_celsius(fahrenheit):
        global FAHRENHEIT_TO_CELSIUS_FACTOR
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return(celsius)
    print(f"{temperature} F is {convert_to_celsius(fahrenheit)} C")
elif state == "C":
        celsius = int(temperature)
        #Function to convert celcius to fahrenheit
        def convert_to_fahrenheit(celsius):
            global CELSIUS_TO_FAHRENHEIT_FACTOR
            fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
            return(fahrenheit)
        print(f"{temperature} C is {convert_to_fahrenheit(celsius)} F")
else:
    print("Invalid temperature. Please enter a numeric value.")

 #   