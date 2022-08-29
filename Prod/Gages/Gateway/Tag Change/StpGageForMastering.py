def logDebugMsg(msgID, message, msgSource):
		
	params = {'msgID':msgID,
			  'message':message,
			  'msgSource':msgSource}
	import system
	system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)


try:

	if (initialChange == 1):  # 1 means this script may have been 'saved' and that saving it generated the change event 
		quit()


	pth = str(event.tagPath).replace('[default]', '')
	pathAry = pth.split('/')
	GageID = pathAry[0]
	pathGageID = '[default]' + GageID + '/' + GageID
	pathTotPart = pathGageID + '/Gage/Total Parts'  # [default]G16/G16/Gage/Total Parts
	
	CurrentTick = int(event.getValue().value)
	divRemain = divmod(CurrentTick, 10) # each 10th part
	
	if (divRemain[1] != 0):  # each 10th part
		quit()

	resultSet = system.db.runNamedQuery("Gages", "GageMaintenance/Get_Last_Tuneup_Tick", {"Gage":GageID})
	
	LastMasterCount = int(resultSet.getValueAt(0, 0))
	
#	Debug.LogMessage('ozarka', 'LastMasterCount = ' + str(LastMasterCount), 'CurrentTick = ' + str(CurrentTick))  # ???
			
	if (LastMasterCount == 0): # if this is the first time the Gage is reading this data  #  Initialize the table with CurrentTick (total part count)
		system.db.runNamedQuery("Gages", "GageMaintenance/Set_Last_Tuneup_Tick", {"Gage":GageID, "TotalParts":CurrentTick})
		quit() # this was the first time the Gage read this data

	MaxPartsBetween = int(resultSet.getValueAt(0, 1))  #  The number of parts allowed between masterings / (originally this number was 4000)
	system.db.runNamedQuery("Gages", "GageMaintenance/Set_Current_Tick", {"Gage":GageID, "TotalPartCount":CurrentTick})
	partsUntilLock = MaxPartsBetween - (CurrentTick - LastMasterCount)
	CalibrationStatePath = '[default]' + GageID + '/' + GageID + '/MES/Calibration State'
	
	if (partsUntilLock > 300):
#		Debug.LogMessage('Cain', GageID, '0 = ' + CalibrationStatePath)
		system.tag.writeBlocking([CalibrationStatePath], [0])

		
	if (partsUntilLock <= 300):
		system.tag.writeBlocking([CalibrationStatePath], [1])
#		Debug.LogMessage('Cain', GageID, '1 = ' + CalibrationStatePath)

	if (partsUntilLock <= 100):
		system.tag.writeBlocking([CalibrationStatePath], [2])
#		Debug.LogMessage('Cain', GageID, '2 = ' + CalibrationStatePath)		

	
	if (CurrentTick - LastMasterCount >= MaxPartsBetween):
		mesLockPath = '[default]' + GageID + '/' + GageID + '/MES/MES Control Hold'
		mesMsgPath = '[default]' + GageID + '/' + GageID + '/MES/MES Message'
		system.tag.writeBlocking([mesLockPath], [True])
		system.tag.writeBlocking([mesMsgPath], ['Calibrations Required'])
#		logDebugMsg('choca', GageID, 'MES Control Hold = True')
		#  write locking record to Gage_Locking
		system.db.runNamedQuery("Gages", "GageLockingTable/Lock_Gage", {"Gage":GageID, "Lock_Type":Globals.lock_type_operator}) # update the lock details table		
		system.db.runNamedQuery("Gages", "GageMaintenance/Set_Last_Tuneup_Tick", {"Gage":GageID, "TotalParts":CurrentTick}) # update the counting logic / table	
	else:
		pass
#		system.db.runNamedQuery("Gages", "GageMaintenance/Set_Current_Tick", {"Gage":GageID, "TotalPartCount":CurrentTick})	

		
		
except Exception as e:
	e_msg_id = 'Gateway Script error'
	e_msg_source = 'StpGageForMastering 3R9LAO'
	
	ErrorHandling.err_handler(e_msg_id, e_msg_source, e)