import json
import random
import getpass

user = []



def createAccount():
	print("\nCREATE ACCOUNT")
	username = input("Enter your USERNAME: ")
	password = getpass.getpass(prompt= 'Enter your PASSWORD: ')
	with open('support/enrolled_students.json', 'r+') as enrolled_students:
		users = json.load(enrolled_students)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password]
			enrolled_students.seek(0)
			json.dump(users, enrolled_students)
			enrolled_students.truncate()
			print("Account created successfully!")

def loginAccount():
	print('\nLOGIN PANEL')
	username = input("USERNAME: ")
	password = getpass.getpass(prompt= 'PASSWORD: ')
	with open('support/enrolled_students.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("An account of that name doesn't exist.\nPlease create an account first.")
	elif username in users.keys():
		if users[username][0] != password:
			print("Your password is incorrect.\nPlease enter the correct password and try again.")
		elif users[username][0] == password:
			print("You have successfully logged in.\n")
			user.append(username)

def play():
    print("\nQUIZ START")
    score = 0
    global user
    with open("support/questions.json", 'r+') as f:
        j = json.load(f)
        for i in range(5):
            no_of_questions = len(j)
            ch = random.randint(0, no_of_questions-1)
            print(f'\nQ{i+1} {j[ch]["question"]}\n')
            for option in j[ch]["options"]:
                print(option)
            answer = input("\nEnter your answer: ")
            if j[ch]["answer"][0] == answer[0].upper():
                print("\nYou are correct")
                score+=1
            else:
                print("\nYou are incorrect")
            del j[ch]
        print(f'\nFINAL SCORE: {score}')
        if len(user) == 0:
            print("You are logged out. Can't be added")
        else:
            
		      
            with open('support/enrolled_students.json', 'r+') as enrolled_students:	
                users = json.load(enrolled_students)
            if user[0] in users.keys():
                
                users[user[0]].append(["previous attempt:",score])
                
                
                
			    
			
                
                print("Attempt added successfully!")
def logout():
	global user
	if len(user) == 0:
		print("You are already logged out.")
	else:
		user = []
		print("You have been logged out successfully.")

def rules():
	print('''\nRULES
- You can create an account from ACCOUNT CREATION panel.
- You can login using created account credentials and then logout too after taking the quiz.
- Each round consists of 5 random questions from the json file. Marking: +1/no negative.
- Your final score will be given at the end.
	''')
def show():
    global user
    if len(user)==0:
        print('You are not logged in')
    else:
        with open('support/enrolled_students.json', 'r+') as enrolled_students:	
            users = json.load(enrolled_students)
        if user[0] in users.keys():
                    
            print(users[user[0]][1:])

if __name__ == "__main__":
	choice = 1
	while choice != 6:
		print('\nSELECT AN OPTION 1-6')
		print('\n')
		print('1. PLAY QUIZ')
		print('2. INSTRUCTIONS')
		print('3. CREATE AN ACCOUNT')
		print('4. LOGIN PANEL')
		print('5. LOGOUT PANEL')
		print('6. SHOW PREVIOUS ATTEMPTS')
        
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			rules()
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			logout()			
		elif choice == 6:
			show()
        
		else:
			print('Invalid Input. ENTER 1-6')
