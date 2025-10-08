file_path = "tasks.txt"
taskerActive = True

with open("tasks.txt", "a") as file:
    pass

print("Welcome to the Tasker!")

def linecheck():
    with open("tasks.txt", "r") as f:
        num_lines = sum(1 for _ in f)
        return num_lines;

while taskerActive:
    print("\nWhat do you want do?")
    print("\n1: Add a new Task")
    print("2: List Tasks")
    print("3: Remove a Task")
    print("4: Exit")
    activity = input()
    
    if activity == "1":
        number = linecheck()
        print("\nWhat task do you want to add?\n")
        task = input() 
        with open (file_path, "a") as file:
            file.write(f"{number + 1}. {task}\n")
            print(f"\nThe Task got added!")
    elif activity == "2":
        with open("tasks.txt", "r") as file:
            content = file.read()
            print(f"\n{content}")
    elif activity == "3":
        print("\nWhich task do you wan to remove?")
        removeLine = int(input()) - 1
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        lines[removeLine] = ""
        with open("tasks.txt", "w") as file:
            file.writelines(lines)
        with open("tasks.txt", "r") as file:
            tasks = []                       # Eine leere Liste für die Aufgaben
            for line in file:                # Gehe jede Zeile durch
                parts = line.split('.', 1)   # Teile die Zeile am ersten Punkt
                if len(parts) > 1:           # Nur Zeilen, die einen Punkt haben
                    tasks.append(parts[1].strip())  # Den Text nach dem Punkt speichern
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                file.write(f"{i}. {task.strip()}\n")
        print(f"The task number {removeLine + 1} got removed ")
    elif activity == "4":
        taskerActive = False
    else:
        print("That is not a valid command! Use 1 / 2 / 3 / 4.")

print("See you next time")
