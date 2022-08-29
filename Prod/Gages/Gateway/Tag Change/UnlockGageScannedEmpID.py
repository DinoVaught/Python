	
def CleanEmployeeID(empID):

# empID look like ='<u>2471<u>'
# empID might have CRs, LFs , Nulls and other white characters on the beginning or ends of them
# this function strips the empID down to its numeric string values like '2471'

	retVal = empID 
	empID = ''
	for c in retVal:
		if ord(c) >= 48 and ord(c) <= 57:
			empID = empID + chr(ord(c))
	
	return empID
	

def GetGageName(tagPath):
	tagPath = tagPath.replace("[default]", "")
	tagPath = tagPath.split("/")
	return tagPath[0].strip()

def CheckForMasterLock(gage, roles, msgPath):


#	Debug.LogMessage('ozarka', "dataSet.getRowCount() = "  , 'ss')
#	params = {'msgID':'ozarka', 'message':"message", 'msgSource':"msgSource"}
#	system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)


	import system  # (import system) has to be here (so (system.db...) will interpret correctly for some bug-like reason 
	dataSet = system.db.runNamedQuery("Gages", "GageLockingTable/CheckGageLockedMaintenance", {"Gage":gage})
	

	if dataSet.getRowCount() > 0:


		locked = (dataSet.getValueAt(0, "Locked").upper() == 'Y')
		rabbited = (dataSet.getValueAt(0, "Red_Rabbit_Activated").upper() == 'Y')

		if locked == False:  # Under this condition, there is no 'master' lock, so just return False and let the rest of the script run.
			return False
			
		if locked == True and rabbited == False:                                # neither lock can be removed 
			system.tag.writeBlocking([msgPath], ['Calibrations Required (Red Rabbit)'])  # remind user of the lock type
			quit()                                                              # neither lock (mes or table lock) can be removed:  quit

		if locked == True and rabbited == True:  # Under these conditions, there is a Table-Lock and the master is completed
			roles.append("Operator")  # add the 'Operator' role, allow (anyone) to remove the mes and table locks
			return True

	else:
#		params = {'msgID':'Eastwood3', 'message':gage + ', rabbited = ' , 'msgSource':'rabbited'}
#		import system  # (import system) has to be here (so (system.db...) will interpret correctly for some bug-like reason
#		system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)

		return False
	
def EvalUserRoles(ID, sprRoles):
	import system  # (import system) has to be here (so (system.db...) will interpret correctly for some bug-like reason
	users = system.user.getUsers("default")
	
	userRoles = []   # this is here for error ('userRoles' referenced before assignment)

	for user in users:
		if (str(user.get("username")) == ID):
			userRoles = user.getRoles()

			for i in range(len(userRoles)):          # loop each item in Role list
				userRoles[i] = userRoles[i].upper()  # convert each role to upper case

    		for role in sprRoles:                    # loop each of the (supervisor roles)/(approved roles)
    			if (role.upper() in userRoles):      # if an (approved role) is in (scanned Emp ID's roles)
					return True

	return False     # if flow arrives here the (scanned empID's roles) do not have any (approved roles)
 	

try:


	#	params = {'msgID':'ozarka', 'message':'str(len(ID))  = ' + str(len(ID)) , 'msgSource':ID}
	#	system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)
	
	debugging = ('**G08**' == GetGageName(str(event.getTagPath())))
	
	if (debugging == False):  #  all other Gages will be tested for  initial chnage
		if (initialChange == 1): quit()  # 1 means this script may have been 'saved' and that saving it generated the change event 
	
	
	empID = str(event.getValue().value)
	
	
	superRoles = ["Supervisor", "Leader", "Administrator"]
	# Scans of  Emp IDs and WIP IDs can arrive here.  We're only targeting the Emp ID scans in this script
	

 	
	if empID.find('<u>') > -1:   # '<u>' If the scan is an employee ID . . .

#		params = {'msgID':'ozarka', 'message':'bb = ' , 'msgSource':empID}
#		system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)

		empID = CleanEmployeeID(empID)
		
		gageID = GetGageName(str(event.getTagPath()))
		
		tagPath =  '[default]' + gageID + '/' + gageID + '/MES/MES Control Hold'
		mesMsgPath  =  '[default]' + gageID + '/' + gageID + '/MES/MES Message'


		removeMasteredLock = CheckForMasterLock(gageID, superRoles, mesMsgPath) # this quite()s if conditions are . .
		
		empID_IsSupervisor = EvalUserRoles(empID, superRoles)

		
		if (empID_IsSupervisor == False):
			quit()  # scanned ID cannot remove any type of mes lock		

		
		system.tag.writeBlocking([tagPath], [False])
		system.tag.writeBlocking([mesMsgPath], [''])  # blank-out the lock msg on the HMI screen
		

		if (removeMasteredLock == True):	 # if a maintenance lock is in place and it's OK to unlock it
				
			system.db.runNamedQuery("Gages", "GageLockingTable/Unlock_Gage", {"Gage":gageID, "EmpID":empID})
		
except Exception as e:

	eParams = {'msgID':'UnlockGageScannedEmpID error',
               'message':getattr(e, 'message', repr(e)),
               'msgSource':'GatewayScript UnlockGageScannedEmpID 3K7K85'}
           
	system.db.runNamedQuery("Gages", "Debug/LogMsg", eParams)
		