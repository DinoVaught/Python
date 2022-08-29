pathRight = '/Scanner/Wip Date'

for i in range(1, 28, 1):
	tagID = 'G' + str(i).zfill(2)
	targetTag = '[default]' + tagID + '/' + tagID + pathRight
	config = system.tag.getConfiguration(targetTag, False)

	if ('value' in config[0]):
		print tagID + ': ' + pathRight + ' Value = ' + str(config[0]['value'])
	else:
		print tagID + ': ' + pathRight + ' Value = Bad_Stale'
        
        
        
====================================================================================

pathRight = '/Wip Part Type'

for i in range(1, 28, 1):
	tagID = 'G' + str(i).zfill(2)
	targetTag = '[default]' + tagID + '/' + tagID + pathRight
	config = system.tag.readBlocking([targetTag])[0].value

#	print str(tagID) + ': ' + str(config)

	if (config == None):
		print str(tagID) + ', ' + pathRight + ' = None'
#	else:
#		print tagID + ': ' + pathRight + ' Value = Bad_Stale'      
        