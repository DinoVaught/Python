def err_handler(msg_id, err_source, err):
	err_msg = getattr(err, 'message', repr(err))

	if err_msg.upper() == 'exit sub'.upper():
		print('exiting script')
	else:
		print(err_msg)


def hydro_id_is_valid(hydro_id):
	try:

		return hydro_id.upper() in ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25']

	except:
		return False


def get_hydromat_id(wip_id, skid_id):
	hydro_id = 'mGlobals.Utils.parseHydroFromWip(wip_id)'
	if 'mGlobals.Utils.hydro_id_is_valid(hydro_id)' == 'False':
		hydro_id = "system.db.runNamedQuery(Printing/getAsset, {skidID: skid_id})"
		if 'mGlobals.Utils.hydro_id_is_valid(hydro_id)' == 'False':
			hydro_id = 'NA'

	return hydro_id


def strRightDelim(value, delimiter):
	try:

		iLoc = value.index(delimiter)
		retVal = value[iLoc + + len(delimiter): len(value)]
		return retVal

	except ValueError:  # delimiter does not exist in search string
		return "delimiter error"
	except:
		return "Error"


def stop_start_agr_rec(gage_id):
	base_path = '[default]' + gage_id + '/' + gage_id


def strIsNumeric(val):
	for c in val:
		if not (48 <= ord(c) <= 57):  # if ord(c) is not between 48 and 57
			return False  # ord(c) is not numeric

	return True


class ScanParse:
	"""
	parses the parts of a scanned string, determines the type scanned string etc. (Hydromat / production side)

	8/10/2022: This class is instantiated in (see notes below)

	Project: CMM
	View: Page/Embedded/Cards/machine home card
		- See Tag Binding on: root-style-classes (bound to tag) = [default]{machine}/{machine}/MES/

	Tag-Script . . .
		- [default]_types_/Hydromat v15/Scanner/Scanner Message

	"""

	def __init__(self, scn_val):
		""" Initiates the class
			Args:
				scn_val: the 'cleaned/striped()' scanned value as it was received from the scanner
		"""
		self.error = True
		self.scanType = ''
		self.maintType = ''
		self.scanValue = ''
		self.scanIdentifier = ''

		scn_val = str(scn_val)
		scn_val = scn_val.upper()

		self.scanIdentifier = scn_val[0:3:1]
		self.scanValue = scn_val.replace(self.scanIdentifier, '')

		if self.scanIdentifier == '<U>':
			if self.scanValue == '0000':
				self.scanType = self.ScanTypes.Clear_scan
			else:
				self.scanType = self.ScanTypes.User_ID

			if self.scanValue in [self.MaintenanceCode.Maint_Present, self.MaintenanceCode.Electronic, self.MaintenanceCode.Electronic, self.MaintenanceCode.Hydraulic, self.MaintenanceCode.Mechanical, self.MaintenanceCode.Coolant, self.MaintenanceCode.General]:
				self.scanType = self.ScanTypes.Maintenance

				if self.scanValue == self.MaintenanceCode.Maint_Present:
					self.maintType = self.MaintenanceTypes.Maint_Present

				if self.scanValue == self.MaintenanceCode.Electronic:
					self.maintType = self.MaintenanceTypes.Electronic

				if self.scanValue == self.MaintenanceCode.Hydraulic:
					self.maintType = self.MaintenanceTypes.Hydraulic

				if self.scanValue == self.MaintenanceCode.Mechanical:
					self.maintType = self.MaintenanceTypes.Mechanical

				if self.scanValue == self.MaintenanceCode.Coolant:
					self.maintType = self.MaintenanceTypes.Coolant

				if self.scanValue == self.MaintenanceCode.General:
					self.maintType = self.MaintenanceTypes.General

		if self.scanIdentifier == '<H>':
			self.scanType = self.ScanTypes.Heat_num

		self.error = False

	class ScanTypes:
		def __init__(self):
			pass

		User_ID = 'User_ID'
		Heat_num = 'Heat_num'
		Maintenance = 'Maintenance'
		Clear_scan = 'clear_scan'  # = the '0000' barcode/badge

	class MaintenanceTypes:
		def __init__(self):
			pass
		Maint_Present = 'Maint_Present'
		Electronic = 'Electronic'
		Hydraulic = 'Hydraulic'
		Mechanical = 'Mechanical'
		Coolant = 'Coolant'
		General = 'General'
		NoMaint = ''

	class MaintenanceCode:
		def __init__(self):
			pass
		Maint_Present = '9994'
		Electronic = '9995'
		Hydraulic = '9996'
		Mechanical = '9997'
		Coolant = '9998'
		General = '9999'

	class StyleClasses:
		def __init__(self):
			pass
		Maint_Present = 'MaintColors/Maint_Present'
		Electronic = 'MaintColors/Electronic'
		Hydraulic = 'MaintColors/Hydraulic'
		Mechanical = 'MaintColors/Mechanical'
		Coolant = 'MaintColors/Coolant'
		General = 'MaintColors/General'
		NoStyle = ''


def test_proc():
	pass


try:

	scnVal = '<u>9994<u>'
	mt = ScanParse(scnVal)

	value = 'Maint_Present'
	if value == mt.MaintenanceTypes.Maint_Present:
		value = mt.StyleClasses.Maint_Present



	STN_1_Count = ''
	STN_2_Count = ''
	STN_3_Count = ''
	STN_4_Count = ''
	STN_5_Count = ''
	STN_6_Count = ''

#	tp = TagPathParse('[default]G01/G01/Gage/Count/AGR', '/Gage/Count/Batch Target', '/Gage/Count/Batch Target')

	initialChange = 1
	if initialChange == 1:  # 1 means this script may have been 'saved' and that saving it generated the change event
		quit()


except Exception as e:
	e_msg_id = 'Test script error'
	e_msg_source = 'Hydromat v15/Scanner/Scanner Message/valueChanged. . . H7NFUR'

	err_handler(e_msg_id, e_msg_source, e)
