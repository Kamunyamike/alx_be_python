current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

if current_weather.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather.lower() == "cold": 
    print("Make sure to wear a warm coat and a scarf.")
else: 
    print("Sorry, I don't have recommendations for this weather.")