feelings = ['angry', 'sad', 'happy', 'content']

def feelings_check():
	print("What are you feeling right now?")
	print("""
		a = angry
		b = sad
		c = happy
		d = content""")

	choice = input()
	print("Ok, you're feeling " + choice + ".")

feelings_check()