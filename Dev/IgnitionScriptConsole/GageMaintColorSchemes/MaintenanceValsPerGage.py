def LightCurtainIsBlocked(gage):
	
	pathMax = '[default]' + gage + '/' + gage + '/Specials/TrackMax'
	pathMin = '[default]' + gage + '/' + gage + '/Specials/TrackMin'
	
	pathMaxVal = system.tag.readBlocking([pathMax])[0].value
	pathMinVal = system.tag.readBlocking([pathMin])[0].value
	
	if gage == 'G08':
#	print(gage + ', ' + str(pathMaxVal == True or pathMinVal == True) + ', pathMaxVal = ' + str(pathMaxVal) + ', pathMinVal = ' +str(pathMinVal))
		# print(gage + ', ' + ' pathMaxVal = ' + str(pathMaxVal) + ', pathMinVal = ' +str(pathMinVal))

		return pathMaxVal == True or pathMinVal == True

try:
	dsGageStates = system.dataset.toPyDataSet(system.db.runNamedQuery('Gage_States/starved_get'))
	
	for row in dsGageStates:
		
		gage_ID = str(row['Gage_ID']) 
		seconds = int(row['secs'])
		
#		if gage_ID == 'G05':
		
#		print(ga.Gage + '= ' + ga.GageStates.Starved)

		ga = Maintenance.GageAttention(gage_ID)
		if gage_ID == 'G11':
			pass
#			ga = Maintenance.GageAttention(gage_ID)
#			ga.SetCardBackColor('zz')
#			ga.SetCardBackColor(ga.GetGageMaintState()) 
#			print(ga.Gage + ', ' + ga.GetGageMaintState())

		print(ga.Gage + ', ' + ga.GetGageMaintState() + ', ' + str(ga.GageIsInMaintenance()))
	
	
	
		if ga.GageIsInMaintenance() == False: # skip over Gages that are in maintenance
		
			if seconds >= 30:
				if LightCurtainIsBlocked(gage_ID) == False:
					pass
					# LightCurtainIsBlocked = False (gage is starved)
#					print(ga.Gage + '= starved')
				else:
					pass
#					print(ga.Gage + '= not starved')
	
except Exception as e:
	
		print gage_ID + (getattr(e, 'message', repr(e)))
		
# G08, pathMaxVal = None 