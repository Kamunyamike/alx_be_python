task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input ("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task. Aim to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that may need attention soon.")
        else:
            print(f"{task} is a medium priority task. Work on it when your high-priority tasks are done.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task. Consider completing it when you have free time or during downtime.")
        else: 
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
            
            
