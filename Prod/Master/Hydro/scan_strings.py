class ScanParse:
	""" parses the parts of a scanned string, determines the type scanned string etc. (Hydromat / production side) """

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


			if self.scanValue in [self.MaintenanceCode.Electronic, self.MaintenanceCode.Electronic, self.MaintenanceCode.Hydraulic, self.MaintenanceCode.Mechanical, self.MaintenanceCode.Coolant, self.MaintenanceCode.General]:
				self.scanType = self.ScanTypes.Maintenance

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
		Electronic = 'Electronic'
		Hydraulic = 'Hydraulic'
		Mechanical = 'Mechanical'
		Coolant = 'Coolant'
		General = 'General'
		NoMaint = ''

	class MaintenanceCode:
		def __init__(self):
			pass
		Electronic = '9995'
		Hydraulic = '9996'
		Mechanical = '9997'
		Coolant = '9998'
		General = '9999'

	class StyleClasses:
		def __init__(self):
			pass
		Electronic = 'MaintColors/Electronic'
		Hydraulic = 'MaintColors/Hydraulic'
		Mechanical = 'MaintColors/Mechanical'
		Coolant = 'MaintColors/Coolant'
		General = 'MaintColors/General'
		NoStyle = ''


def scan_is_valid(scanned_val):

	try:

		if scanned_val is None:
			return False

		scanned_val = str(scanned_val)

		if len(scanned_val) <= 3:
			return False

		if scanned_val[0:1:1] != '<':
			return False

		if scanned_val[-1] != '>':
			return False

		if scanned_val.count('<') != 2:
			return False

		if scanned_val.count('>') != 2:
			return False

		return True

	except:
		return False