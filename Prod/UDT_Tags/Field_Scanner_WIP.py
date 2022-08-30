	
	try:
	
		ass =  system.tag.read('[.]Asset.value')

		use =  system.tag.read('[.]User.value')
		wip =  currentValue
		
		Logging.log.log_debug('**** wip ', '1', wip.value)
		
		machine = wip.value[2:5]
		
		Logging.log.log_debug('**** wip ', '2', '2')
		
		when = currentValue.timestamp
		
		Logging.log.log_debug('**** wip ', '3', wip.value.strip())
		
		q = system.tag.read('[.]Query to run.value')
		x = system.db.runQuery("SELECT tbl,lotter FROM mes.tbl_strings where `machine` = \'%s\'" %(machine))
		tbl = x[0]['lotter']
		params = {'tbl':tbl,'asset':ass.value,'whom':use.value,'doctime':when,'wip':wip.value.strip()}
		print params
		print q.value
		l = system.db.runNamedQuery("CMM", q.value, params)
		print l
	
		Logging.log.log_debug('**** wip ', '4', q.value + ' l = ' + str(l))
	
	except Exception as e:
		e_msg_id = 'valueChanged err'
		e_msg_source = 'UDT Field Scanner/WIP. . . 5MDNSY'
		
		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)