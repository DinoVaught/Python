	
	try:
		if (initialChange == 1):  # 1 means this script may have been 'saved' and that saving it generated the change event 
			raise Exception('Exit Sub')
			
		if currentValue.value is None:  # Sometimes currentValue is None, like when the Gage is turned off or perhaps in some other offline-like state
			raise Exception('Exit Sub')

		if currentValue.quality.isGood() == False:
			raise Exception('Exit Sub')

	
		Gage = tagPath.replace("[default]", "")
		Gage = Gage.split("/")
		Gage = Gage[0].strip().upper()
		
		system.db.runNamedQuery('Gages', 'Gage_States/starved_set', {'gage_ID':Gage})

		ga = Maintenance.GageAttention(Gage)

		if currentValue.value == True:  # True  = (the gage is not starved)(the light curtain is blocked) (there is a part in the sensor)
			if ga.GageIsInMaintenance() == False:
				ga.SetCardBackColor(ga.GageStates.Running)

	except Exception as e:
	
		e_msg_id = 'valueChanged err'
		e_msg_source = 'UDT_Tag/TrackMax. . . 44Z6KG'
		
		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)
