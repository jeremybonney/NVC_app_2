def feelings_check():
	
	feelings =[]

	print("What are you feeling right now? ('n' for nothing or you don't want to share)")
	
	# checking_feelings = True
	feeling = input()

	if feeling == 'n':
		print("No worries. I hope you figure out what you need to. I'll be here if you need me.")

	else:
		# while checking_feelings:
		feelings.append(feeling)

		print("Great. You've said you're feeling " + feeling + ". And what else? ('n' for nothing)")

		checking_feelings = True
		while checking_feelings:
			additional_feeling = input()

		if additional_feeling == 'n':
			print("Great. So you're just feeling " + feeling + " or there's nothing more you want to share right now. I'll be here if you need me again.")

		else:
			print("Ok, so you're also feeling " + additional_feeling + ". And what else? ('n' for nothing)")

		feeling = input()

		if feeling 

		checking_feelings = True
		while checking_feelings:
			feeling = input()
			feelings.append(feeling)
		# 	print("Ok, you're feeling " + feeling + ". And what else? ('n' for nothing)")
		# 	more_feelings = input()
		# 	if more_feelings == 'n':
		# 		checking_feelings = False
		# 	else:
		# 		feeling = input()
	
		# for feeling in feelings:
		# 	print("• " + feeling)
		# print("\nLet's continue."))

feelings_check()