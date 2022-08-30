	ass =  system.tag.read('[.]Asset.value')
	use =  system.tag.read('[.]User.value')
	wip =  currentValue
	machine = wip.value[2:5]
	when = currentValue.timestamp
	q = system.tag.read('[.]Query to run.value')
	x = system.db.runQuery("SELECT tbl,lotter FROM mes.tbl_strings where `machine` = \'%s\'" %(machine))
	tbl = x[0]['lotter']
	params = {'tbl':tbl,'asset':ass.value,'whom':use.value,'doctime':when,'wip':wip.value.strip()}
	print params
	print q.value
	l = system.db.runNamedQuery("CMM",q.value,params)
	print l	