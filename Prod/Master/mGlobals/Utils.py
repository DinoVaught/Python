# ====================================================================
# parseHydroFromWip(wip):
# returns the hydromat machine (D25) from a WIP (21D25294C007)       =
# returns (D25) from (21D25294C007)                                  =
def parseHydroFromWip(wip):
	
	try:

		debugDat = ''
		wip = wip.upper()
		targetLoc = wip.find('D')

		if targetLoc == -1:
			for c in wip:
				debugDat += str(ord(c)) + ', '
			raise Exception('the parse character does not exist exist')

		if wip.count('D') != 1:
			debugDat = wip
			raise Exception('multiple occurrences of the parse character exists')

		retVal = wip[targetLoc: targetLoc + 3: 1]

		return retVal.upper()

	except Exception as e:

		e_msg_id = 'parseHydro(wip) err, debugDat = ' + ' (' + debugDat + ') wip = (' + wip + ')'
		e_msg_source = 'mGlobals.Utils.parseHydroFromWip(wip). . . Y4HACX'

		ErrorHandling.err_handler(e_msg_id, e_msg_source, e)
		return 'Error'


def gage_id_is_valid(gage_id):

	try:
		gage_id = gage_id.upper()
		if gage_id in ['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09', 'G10', 'G11', 'G12', 'G13', 'G14',
					   'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28']:
			return True
		else:
			return False
	except:
		return False


class TagPathParse:
	def __init__(self, tag_path, write_path_a, write_path_b=''):
		"""
		
		:type write_path_b: str
		"""
		self.MachineName = tag_path.split("/")[1].upper().strip()
		self.SourcePath = tag_path
		self.WritePath_a = '[default]' + self.MachineName + '/' + self.MachineName + write_path_a
		if write_path_b != '':
			self.WritePath_b = '[default]' + self.MachineName + '/' + self.MachineName + write_path_b
		else:
			self.WritePath_b = ''


def clean_scan_str(scan_str):
	ret_val = scan_str
	ret_val = ret_val.replace('\r', '')  # remove any (carriage return) characters
	ret_val = ret_val.replace('\n', '')  # remove any (new line) characters
	ret_val = ret_val.strip()  # remove any spaces from left and right ends
	return ret_val