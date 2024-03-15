tasks = input("Enter your tasks for today separated by a comma: ").split(", ")
done = []
ongoing = []

for task in tasks:
    print(f"\n{task}\n")
    response = input(f"Did you finish the {task} already?\n").capitalize()
    if response == 'Yes':
        print("Nice Job\n----------\n")
        done.append(task)
    elif response == 'No':
        print("Try not to put it off\n----------\n")
        ongoing.append(task)
    else:
        print('Please write Yes or No')

progress = input("Do you want to see your today's progress?(yes, no)\n").capitalize()
if progress == "Yes":
    print("""
            ******** Done Tasks ****
""")
    print(done)
    print("""
            ****** Ongoing Tasks *****
""")
    print(ongoing)
else:
    input("Please hit Enter to exit")
