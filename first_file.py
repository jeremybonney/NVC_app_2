feelings = ['angry', 'sad', 'happy', 'content']

def feelings_check():
	
	feelings =[]

	print("What are you feeling right now? ('n' for nothing or you don't want to share)")
	
	first_feeling = input()

	if first_feeling != 'n':
		feelings.append(first_feeling)
		print("Ok, you're feeling " + first_feeling + ". And what else? ('n' for nothing or you don't want to share)")
		checking_feelings = True
		feeling = input()

		if feeling != 'n':
			checking_feelings = True
			while checking_feelings:
				feeling = input()
				feelings.append(feeling)
				print("Ok, you're feeling " + feeling + ". And what else? ('n' for nothing)")
				more_feelings = input()
				if more_feelings == 'n':
					checking_feelings = False
				else:
					feeling = input()

	print("Great. This is everything that you're feeling right now:\n")
	for feeling in feelings:
		print("• " + feeling)
	print("\nLet's continue."))



	else:
		feelings.append(feeling)
		print("Great. You've said you're feeling " + first_feeling + ".")

	checking_feelings = True
	while checking_feelings:
		feeling = input()
		feelings.append(feeling)
		print("Ok, you're feeling " + feeling + ". And what else? ('n' for nothing)")
		more_feelings = input()
		if more_feelings == 'n':
			checking_feelings = False
		else:
			feeling = input()

	print("Great. This is everything that you're feeling right now:\n")
	for feeling in feelings:
		print("• " + feeling)
	print("\nLet's continue.")

feelings_check()