# first import demo yayy

import getpass

username = "AizarGaming1290"
password = "Namzuged0921"

usr = input("Please enter thy username --->")
pw = getpass.getpass("Password? --->")

if usr == username and pw == password :
	print("You're in!")
else:
	print("Sorry. Access Denied.")

# so basically the getpass.getpass() let's us type our input but we cannot see it for ourselves.