
try:


	
	partMissed  = event.getValue().value  # Reject/Bad Part Did Not Trigger Chute Sensor

	ml = Gages.mes_locks.MesLocking
	
	tpp = mGlobals.Utils.TagPathParse(str(event.getTagPath()), '/MES/MES Control Hold', '/MES/MES Message')
	#  tpp.WritePath_a resolves to = '.../MES/MES Control Hold'
	#  tpp.WritePath_b resolves to = '.../MES/MES Message'
	
	
	if (initialChange == 1):  # 1 means this script may have been 'saved' and that saving it generated the change event 
		raise Exception('Exit Sub')
	
	if partMissed == False:
		raise Exception('Exit Sub')

	if partMissed == True:
		system.tag.writeBlocking([tpp.WritePath_a], [True])
		system.tag.writeBlocking([tpp.WritePath_b], [ml.PartMissedSensor.hmi_msg]) # ml.PartMissedSensor.hmi_msg = 'Exit Chute Bad Part Did Not Hit Sensor'
		
		Logging.prod_data.log_prod_data('Gages: Bad Part No Exit Chute Sensor', tpp.MachineName, 'Locked', '', '')
		

except Exception as e:
	e_msg_id = 'Gateway Script error' + ', ' + tpp.MachineName
	e_msg_source = 'StopGage_exit_diverter_not_trigger Q2WPH5'
	
	ErrorHandling.err_handler(e_msg_id, e_msg_source, e)