dsGageStates = system.dataset.toPyDataSet(system.db.runNamedQuery('Gage_States/starved_get'))
	
for row in dsGageStates:
	gage_ID = str(row['Gage_ID']) 
	seconds = int(row['secs'])
	
	ga = Maintenance.GageAttention(gage_ID)

	pathMax = '[default]' + gage_ID + '/' + gage_ID + '/Specials/TrackMax'
	pathMin = '[default]' + gage_ID + '/' + gage_ID + '/Specials/TrackMin'

	curMax = system.tag.readBlocking([pathMax])[0].value
	curMin = system.tag.readBlocking([pathMin])[0].value

	maint = ga.GageIsInMaintenance()
	
	print(ga.Gage + ', curMax = ' + str(curMax) + ', curMin = ' + str(curMin) )