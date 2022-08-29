# This script runs 1 time per minute / at intervals of 60,000 milliseconds.  Be careful not to edit the interval of 60,000 ms as this assures the (by minute) accuracy this( AGR collection) process requires 
# This script runs 1,440 times per day
# This script terminates early, quite()s, and does absolutely nothing 99.79% of the time
# The other 0.21% of the time, it will collect AGR data for each of the 27 gages (by shift)

import datetime


try:

	hour = int(datetime.datetime.now().strftime("%H"))
	minute = int(datetime.datetime.now().strftime("%M"))
	second = int(datetime.datetime.now().strftime("%S"))
	
	
	# ==============================================================================================================================
	# The hours below (23, 15, 7) are the hours this script will run in its entirety                                               = 
	# This script will not quit() on the 0 minute of the (23, 15, 7) hours                                                         =
	# ==============================================================================================================================
	
	if hour != 23 and hour != 15 and hour != 7:  #  (23 = 11 PM)  (15 = 3 PM) (7 = 7 AM)                                           =
		quit()                                                                                                                   # =
																																 # =                           
	if minute != 0: quit()                                                                                                       # =
	
	# ==============================================================================================================================
	
	Gage = ""
	for x in range(1, 28):
	
		try:
	
			Gage = "G" + str(x).zfill(2)
			pathGageID = '[default]' + Gage + '/' + Gage
		
#			if Gage == 'G15':
#				i = 1 / 0		
		
			Total = system.tag.readBlocking([pathGageID + '/Station Data/ST1/ST 1 Total Bad Parts'])[0].value
			STN_1_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST1/ST 1 Total Rejects'])[0].value
			STN_2_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST2/ST 2 Total Bad Parts'])[0].value
			STN_3_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST3/ST 3 Total Bad Parts'])[0].value
			STN_4_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST4/ST 4 Total Bad Parts'])[0].value
			STN_5_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST5/ST 5 Total Bad Parts'])[0].value
			STN_6_Count = system.tag.readBlocking([pathGageID + '/Station Data/ST6/ST 6 Total Bad Parts'])[0].value
			
			
			if (Total is None): Total = '0'
			if (STN_1_Count is None): STN_1_Count = '0'
			if (STN_2_Count is None): STN_2_Count = '0'			
			if (STN_3_Count is None): STN_3_Count = '0'
			if (STN_4_Count is None): STN_4_Count = '0'
			if (STN_5_Count is None): STN_5_Count = '0'
			if (STN_6_Count is None): STN_6_Count = '0'	
		
			SkidNum = system.tag.readBlocking([pathGageID + '/Skid/skid id'])[0].value
			hydroMachine = system.db.runNamedQuery("Gages", "Printing/getAsset", {'skidID':SkidNum})
			heatNum = system.tag.readBlocking([pathGageID + '/Skid/Skid Heat'])[0].value
			wipID = system.tag.readBlocking([pathGageID + '/Scanner/Active Wip'])[0].value
			PartNumber = system.tag.readBlocking([pathGageID + '/Gage/Running Part Number'])[0].value
			PartNumber = strFuncs.strRightDelim(PartNumber, '-')
			empID = system.tag.readBlocking([pathGageID + '/Scanner/User'])[0].value
		
			stopParams = {
				'MachTotalStop':Total,
				'GageID':Gage,
				'StopSTN_1':STN_1_Count,
				'StopSTN_2':STN_2_Count,
				'StopSTN_3':STN_3_Count,
				'StopSTN_4':STN_4_Count,
				'StopSTN_5':STN_5_Count,
				'StopSTN_6':STN_6_Count
				}
			system.db.runNamedQuery("Gages", "AGR_Counts/stop_AGR_shift_count", stopParams)
		
		
			startParams = {
				'Mach_Total_Start':Total,
				'GageID':Gage,
				'Start_STN_1':STN_1_Count,
				'Start_STN_2':STN_2_Count,
				'Start_STN_3':STN_3_Count,
				'Start_STN_4':STN_4_Count,
				'Start_STN_5':STN_5_Count,
				'Start_STN_6':STN_6_Count,
				'Hydro':hydroMachine,
				'WIP_Num':wipID,
				'HeatNum':heatNum,
				'PartNum':PartNumber,
				'Skid_ID':SkidNum,
				'EmpID':empID
				}	
		
			system.db.runNamedQuery("Gages", "AGR_Counts/stop_AGR_shift_count", stopParams)
			system.db.runNamedQuery("Gages", "AGR_Counts/start_AGR_shift_count", startParams)
			
		except Exception as inErr:
			e_in_msg_id = 'AGR_By_Shift nest err in (for x), ' + Gage
			e_in_msg_source = 'Gateway script AGR_By_Shift . . . 2GDUZ7'

			ErrorHandling.err_handler(e_in_msg_id, e_in_msg_source, inErr)		

# Debug.LogMessage('Magdalene', system.tag.readBlocking(["[default]G01/G01/Station Data/ST1/ST 1 Total Bad Parts"])[0].value , str(hour) + " : " + str(minute) + " : " + str(second))
except Exception as e:
	e_msg_id = 'AGR_By_Shift err'
	e_msg_source = 'Gateway script AGR_By_Shift . . . EVO965'
	
	ErrorHandling.err_handler(e_msg_id, e_msg_source, e)