
	def LockGageHeatChange(gageID):

		mesHoldPath = '[default]' + gageID + '/' + gageID + '/MES/MES Control Hold'
		mesMsgPath = '[default]' + gageID + '/' + gageID + '/MES/MES Message'

		system.tag.writeBlocking([mesHoldPath], [True])
		system.tag.writeBlocking([mesMsgPath], ['Heat Change Blocked'])		

# ==========================================================================================================
# ==========================================================================================================
	
	try:
#		params = {'msgID':'blue', 'message':"debug record 1" , 'msgSource':''} # -----------------------------
#		system.db.runNamedQuery('Gages', 'Debug/LogMsg', params) # ------------------------------------------------------

		if currentValue.value is None:  # Sometimes currentValue is None, like when the Gage is turned off or perhaps in some other offline-like state
			raise Exception('Exit Sub')

		Gage = tagPath.replace("[default]", "")
		Gage = Gage.split("/")
		Gage = Gage[0].strip().upper()
		
		scnVal = currentValue.value.replace('\r\n', '')

		if strFuncs.strHasNulls(scnVal) == True: # Sometimes the scanners will create a junk scan string with 12 Nulls (see EN-22 for details) 
			raise Exception('Exit Sub')

		if scnVal[0:3] == "<u>":
			userTagPath =  '[default]' + Gage + '/' + Gage + '/Scanner/User'

			if (str(scnVal[3:7]) != '0000'):
				system.tag.writeBlocking([userTagPath], [scnVal[3:7]])

			raise Exception('Exit Sub') # user ID processed, exit script

		
		

		if scnVal[0:3].upper() == 'RRR'.upper():  # RRR = Reject ReRun, scanned values look like 'RRR123456'

			rrScnVal = strFuncs.strRightDelim(scnVal.upper(), 'RRR'.upper())
			
			if strFuncs.isInteger(rrScnVal) == False:
				raise Exception('Scanned string is not numeric, rrScnVal = ' + rrScnVal + ', scnVal = ' + scnVal + ', Gage = ' + Gage)
			
			rrScnVal = int(rrScnVal)
			system.db.runNamedQuery('Gages', 'AGR_Counts/Flag_AGR_Record_As_Rerun', {'indexVal':rrScnVal})			
			raise Exception('Exit Sub')



		if scnVal[0:4].upper() == 'TOTE':  # Tote Tag Rerun: scanned values = 'TOTE184416' 184416 = (ndx) field in table mes.skid_parts (black Tote/good parts) 

			tote_id = scnVal.upper().replace('TOTE', '')
			if strFuncs.strIsNumeric(tote_id) == False:             # strFuncs.strIsNumeric(tote_id)
				raise Exception(Gage + ' - scanned value is not numeric (' + tote_id + ')')

			system.db.runNamedQuery('Gages', 'AGR_Counts/flag_good_parts_as_rerun', {'tote_id':tote_id})

			Debug.LogMessage(Gage, '333', str(tote_id))

			raise Exception('Exit Sub') # Rerun scan processed complete


			
		if len(scnVal) == 12:  # if a WIP Tag was scanned
			
			gageLock = system.tag.readBlocking(['[.]../MES/MES Control Hold'])
			gageLock = str(gageLock[0].value)

			if gageLock.upper() == 'True'.upper():
				raise Exception('Exit Sub') # Block or quit() the scanning of a WIP Tag when the Gage is locked		
		
			# Select (heat) associated with the recently scanned WIP ID
			sql = 'SELECT heat '
			sql = sql + 'FROM mes.lot_table_' + mGlobals.Utils.parseHydroFromWip(scnVal) + ' '
			sql = sql + "WHERE wip_id = '" + scnVal  + "'"
			
			if sql.upper().find('Error'.upper()) > -1:
				raise Exception('Error in parseHydro(wip), Gage = '+ Gage)		
			
			
			pyData = system.db.runQuery(sql)
			
			if int(pyData.getRowCount()) == 0:
				LockGageHeatChange(Gage)
				quit()
			
			scanned_heat = pyData[0]['heat']
			currentHeat = system.tag.readBlocking(['[default]' + Gage + '/' + Gage + '/Database/WIP Details/Heat'])[0].value


			if (currentHeat != scanned_heat):
			
				allowChange = system.db.runScalarQuery("SELECT heat_change FROM mes.gage_states WHERE Gage_ID = '" + Gage + "'")
				
				if (allowChange.upper == 'N'.upper): # if (allow heat change) flag = No 'N' (Blocking Change)
				
					LockGageHeatChange(Gage)
					quit()  #  (block heat change) flag is set to No
					
				else: # (allow heat change) flag is set to Yes (Allowing Change)
				
					# set the (allow heat change) flag to No 'N'
					system.db.runNamedQuery('Gages', "Gage_States/set_heat_change_state", {'Gage':Gage, 'state_yn':'N' }) 
			
			system.tag.write("[.]Active Wip",scnVal)
			
# =========== end ==============================================			

	# select * from debug
	# where source like '%XTA9ZQ'
	# order by created desc;

	except Exception as e:
		e_msg_id = 'UDT Tag error'
		e_msg_source = 'Gage/Scanner/Scan String/valueChanged. . . XTA9ZQ'
		
		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)		