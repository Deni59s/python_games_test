import prompt

def welcome_user():
	return prompt.string("Welcome to the Brain Games!\nMay I have your name?\n")
welcome = welcome_user()
print('Hello, '+welcome+'!')

welcome_user()