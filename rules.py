print("SELECT YOUR ISSUE")
print("'stomach-ache', 'sore-hands', 'headache', 'tired-feet'")
issue_list = []
issue = input("What is your issue? Select from the options above: ")
issue_list.append(issue)

for _ in range(10):
    print("Would you like to add more issues? Enter 1 for 'Yes' or 0 for 'No'")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        issue = input("What else is your issue? Select from the options above: ")
        issue_list.append(issue)
    else:
        break        

problems = {
    "start": issue_list,
    "finish": ["not-healthy"],
    "rules":[
        {
            "issue": "stomach-ache",
            "solution":"Have a light meal and drink plenty of water."
        },
        {
            "issue": "sore-hands",
            "solution":"Stretch and massage your hands regularly."
        },
        {
            "issue": "headache",
            "solution":"Take a break, relax, and stay hydrated."
        },
        {
            "issue": "tired-feet",
            "solution":"Rest your feet and consider elevating them for a while."
        },
    ]
}

start = problems['start']
finish = problems['finish']
rules = problems['rules']

for rule in rules:
    if start[0] == rule['issue']:
        print("Solution:", rule['solution'])
