def log_in(uName, pwd):
	if uName == "xxsx" and pwd == "1231":
		print(uName)
	else:
		print("Wrong")
		entry()

def entry():
	username = input("Enter NAME")
	password = input("Enter PWD")
	log_in(username, password)

print(" LOGIN .....")
#username = input("ENTER NAME")
#password = input("ENTER PWD")
entry()

