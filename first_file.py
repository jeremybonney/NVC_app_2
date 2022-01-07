def feelings_check():
	
	feelings =[]

	print("What are you feeling right now? ('n' for nothing or you don't want to share)")
	
	feeling = input()

	if feeling == 'n':
		print("No worries. I hope you figure out what you need to. I'll be here if you need me.")

	else:
		feelings.append(feeling)

		print("Great. You've said you're feeling " + feeling + ". And what else? ('n' for nothing)")

		checking_feelings = True
		while checking_feelings:
			additional_feeling = input()

			if additional_feeling == 'n':
				print("Great. So this is everything you're feeling right now: ")
				for feeling in feelings:
					print("• " + feeling)
				checking_feelings = False

			else:
				print("Ok, so you're also feeling " + additional_feeling + ". And what else? ('n' for nothing)")

feelings_check()