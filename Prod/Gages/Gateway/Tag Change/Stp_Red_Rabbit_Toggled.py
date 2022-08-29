def logDebugMsg(msgID, message, msgSource):
		
	params = {'msgID':msgID,
			  'message':message,
			  'msgSource':msgSource}
	import system
	system.db.runNamedQuery('Gages', 'Debug/LogMsg', params)

def GetGageName(tagPath):
		tagPath = tagPath.replace("[default]", "")
		tagPath = tagPath.split("/")
		return tagPath[0].strip()


try:


	if (initialChange == 1): quit()  # 1 means this script may have been 'saved' and that saving it generated the change event
	
	gageID = GetGageName(str(event.getTagPath()))
	
#	logDebugMsg('ozMech 1', str(event.getValue().value), gageID)
	
#	if (event.getValue().value == True): # change to True
	system.db.runNamedQuery("Gages", "GageMaintenance/GageMasteredResetCount", {"Gage":gageID})
	
		
except Exception as e:

	eParams = {'msgID':'Gateway Script error',
			   'message':getattr(e, 'message', repr(e)),
			   'msgSource':'StopGageTuneupNeeded 8YEF19'}
		   
	system.db.runNamedQuery("Gages", "Debug/LogMsg", eParams)