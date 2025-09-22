task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        msg = f"'{task}' is a high priority task"
    case "medium":
        msg = f"'{task}' is a medium priority task"
    case "low":
        msg = f"'{task}' is a low priority task"
    case _:
        msg = f"'{task}' has an unspecified priority"

if time_bound == "yes":
    msg += " that requires immediate attention today!"

print("Reminder:", msg)
