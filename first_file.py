feelings = ['angry', 'sad', 'happy', 'content']

def feelings_check():
	
	feelings =[]

	print("What are you feeling right now?")
	feeling = input()
	checking_feelings = True
	while checking_feelings:
		feelings.append(feeling)
		print("""
			Ok, you're feeling """ + feeling + ". Anything else? (y/n)")
		yes_or_no = input()
		if yes_or_no == 'y':
			print("What else are you feeling?")
			feeling = input()
		else:
			checking_feelings = False
	print("Great. This is everything that you're feeling right now:\n")
	for feeling_x in feelings:
		print(feeling_x)
	print("\nLet's continue.")

feelings_check()