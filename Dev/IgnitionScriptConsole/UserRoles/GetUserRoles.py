users = system.user.getUsers("")
for user in users:
    print  str(user.get('username')) + " * "  + str(user.get('firstname'))  + " * " + str(user.get('lastname'))  + " " + str(user.getRoles())

********************************
users = system.user.getUsers("")
for user in users:
	empID = str(user.get('username'))
	empName = str(user.get('firstname')) + " " + str(user.get('lastname'))
	empRoles = str(user.getRoles())
	if 'Supervisor'.upper() in empRoles.upper():
		print  empID + ', ' + empName