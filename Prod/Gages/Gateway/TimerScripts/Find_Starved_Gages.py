def LightCurtainIsBlocked(gage):
	
	import system
	pathMax = '[default]' + gage + '/' + gage + '/Specials/TrackMax'
	pathMin = '[default]' + gage + '/' + gage + '/Specials/TrackMin'
	
	pathMaxVal = system.tag.readBlocking([pathMax])[0].value
	pathMinVal = system.tag.readBlocking([pathMin])[0].value
	
#	print(str(pathMaxVal == True or pathMinVal == True) + ', pathMaxVal = ' + str(pathMaxVal) + ', pathMinVal = ' +str(pathMinVal) )

	return pathMaxVal == True or pathMinVal == True

try:
	import system
	dsGageStates = system.dataset.toPyDataSet(system.db.runNamedQuery('Gage_States/starved_get'))
	
	for row in dsGageStates:
		
		gage_ID = str(row['Gage_ID']) 
		seconds = int(row['secs'])
		
##
		ga = Maintenance.GageAttention(gage_ID)
	
		if ga.GageIsInMaintenance() == False: # skip over Gages that are in maintenance
		
			if seconds >= 30:
				if LightCurtainIsBlocked(gage_ID) == False:
					# LightCurtainIsBlocked = False (gage is starved)
					ga.SetCardBackColor(ga.GageStates.Starved)
				else:
					ga.SetCardBackColor(ga.GageStates.Running)
	
except Exception as e:

		e_msg_id = 'Gateway script, Find_Starved_Gages error'
		e_msg_source = '...SQSX4W'
		
		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)
