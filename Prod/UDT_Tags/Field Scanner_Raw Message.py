	try:
		
		import mGlobals.Utils
		val = currentValue.value
		
#		Logging.log.log_debug('**** 1 len() ', str(len(val)), val)
#		
#		for c in val:
#			Logging.log.log_debug('**** 11 - ' + val, c,  str(ord(c)))	
#		raise Exception('Exit Sub')
 
#		val = mGlobals.Utils.clean_scan_str(val)
#		
#		Logging.log.log_debug('**** 2 len()', str(len(val)), val)
#		
#		for c in val:
#			Logging.log.log_debug('**** 22 - ' + val, c,  str(ord(c)))
		
		
		pre = val[0:3]
		cut1 = val.find('>')
		cut2 = val.rfind('<')
		message = val[cut1 + 1:cut2]
		

		if pre == "<u>":
			system.tag.write("[.]User",message)
		elif pre == '<h>':
			system.tag.write("[.]Heat.value",message)
		elif pre == '<p>':
			system.tag.write("[.]Part.value",message)
		elif pre == '<r>':
			system.tag.write("[.]MRB.value",message)
#		elif len(val) == 14:
#			system.tag.write("[.]WIP.value",message)

		if len(val) == 12:
			system.tag.write("[.]WIP.value",val)
#			Logging.log.log_debug('**** 33 - writing ', val,  '')
#		else:
#			Logging.log.log_debug('**** 33 - NOT writing ', val,  '')

		
		# raise Exception('Exit Sub')
#		for c in val:
#			Logging.log.log_debug('**** 2xz', str(len(val)) + ' = ' + val, c + ' = ' + str(ord(c)))	
	
	except Exception as e:
		e_msg_id = 'valueChanged err'
		e_msg_source = 'TEM2/TEM2 Scanner/Raw Message. . . EI4SO5'
		
		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)