# Write your code here     

n_input = input()
if n_input.strip():
	n = int(n_input)
	phonebook = {}

	for _ in range(n):
		line = input().split()
		if not line:
			continue

		command = line[0]

		if command == "ADD":
			name, number = line[1], line[2]
			phonebook[name] = number   # add or update

		elif command == "REMOVE":
			name = line[1]
			if name in phonebook:
				del phonebook[name]    # remove if exists

		elif command == "DISPLAY":
			if not phonebook:
				print("No contacts")
			else:
				for name in sorted(phonebook.keys()):
					print(f"{name}: {phonebook[name]}")
