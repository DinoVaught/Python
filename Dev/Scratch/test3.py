import time
import datetime


class Gages:
	def __init__(self):
		pass

	class MesLocking:  # copy this part of the class (this line and below)
		def __init__(self):
			pass

		class PartMissedSensor:
			def __init__(self):
				pass
			hmi_msg = 'Exit Chute Bad Part Did Not Hit Sensor'
			pop_up_id = 'I458YWRL1E06N64F'     # id View = (Gages: Page/Embedded/Pops/MesUnlockPartMissed)
			date_format = '%Y-%m-%d %H:%M:%S'  # used for MesUnlockPartMissed's onStartUp https://forum.inductiveautomation.com/t/way-to-prevent-script-from-running-when-popup-view-loads/61322


def err_handler(msg_id, err_source, err):
	err_msg = getattr(err, 'message', repr(err))

	if err_msg.upper() == 'exit sub'.upper():
		print('exiting script')
	else:
		print(err_msg)


def view_loaded():
	ml = Gages.MesLocking


try:

	PartNumber = '456123 081'



	# dateFormat = '%Y-%m-%d %H:%M:%S'
	viewLoaded = str(datetime.datetime.now().strftime(ml.PartMissedSensor.date_format))
	time.sleep(1)
	time_now = datetime.datetime.now().strftime(ml.PartMissedSensor.date_format)

	time_now = datetime.datetime.strptime(time_now, ml.PartMissedSensor.date_format)
	viewLoaded = datetime.datetime.strptime(viewLoaded, ml.PartMissedSensor.date_format)

	print('seconds ' + str((time_now - viewLoaded).total_seconds()))


except Exception as e:
	e_msg_id = 'Test script error'
	e_msg_source = 'Hydromat v15/Scanner/Scanner Message/valueChanged. . . H7NFUR'

	err_handler(e_msg_id, e_msg_source, e)