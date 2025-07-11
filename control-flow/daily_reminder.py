task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound = input ("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a {priority} priority task. Aim to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that may need attention soon.")
        else:
            print(f"Note: {task} is a {priority} priority task. Work on it when your high-priority tasks are done.")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time or during downtime.")
        else: 
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
            
            
