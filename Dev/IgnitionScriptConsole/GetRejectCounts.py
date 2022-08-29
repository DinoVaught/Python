
# Gets the same reject counts (as displayed on the gages cards) for the (trash can) print button

dsGageStates = system.dataset.toPyDataSet(system.db.runNamedQuery('Gage_States/starved_get'))
	
for row in dsGageStates:
	gage = str(row['Gage_ID']) 

	path = '[default]' + gage + '/' + gage + '/Gage/Count/AGR'
	maxPath = '[default]' + gage + '/' + gage + '/Gage/Count/Batch Target'

	crntRjcts = system.tag.readBlocking([path])[0].value
	batchMax = system.tag.readBlocking([maxPath])[0].value
	batchMax = int(batchMax * .5)

	prcnt = crntRjcts / float(batchMax)

	print(gage + ' = ' + str(crntRjcts) + '/' + str(batchMax) + ' (' + "{:.2f}".format(prcnt))