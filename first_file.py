feelings = ['angry', 'sad', 'happy', 'content']

def feelings_check():
	print("What are you feeling right now?")
	print("""
		a = angry
		b = sad
		c = happy
		d = content""")

	feeling = input()
	checking_feelings = True
	while checking_feelings:
		print("""
			Ok, you're feeling """ + feeling + ". Anything else? (y/n)")
		yes_or_no = input()
		if yes_or_no == 'y':
			print("What else are you feeling?")
			feeling = input()
		else:
			checking_feelings = False
	print("Great. Let's continue.")


feelings_check()