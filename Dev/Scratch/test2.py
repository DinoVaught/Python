import types


def err_handler(msg_id, err_source, err):
	err_msg = getattr(err, 'message', repr(err))

	if err_msg.upper() == 'exit sub'.upper():
		print('exiting script')
	else:
		print(err_msg)


class UserInfo:
	def __init__(self, user_id):

		self.userID = ''
		self.user_name = ''

	def has_role(self, val_1):
		if val_1.upper in self.user_name:
			return True
		return False

def user_has_role(user_id, role):
	return False


class AgrStationCounts:
	def __init__(self, gage_id):
		base_path = '[default]' + gage_id + '/' + gage_id
		self.ST_1 = 12
		self.ST_2 = 456
		self.ST_3 = 20
		self.ST_4 = 45
		self.ST_5 = 50
		self.ST_6 = 87
		self.agr_batch_max = 5000

		self.agr_total = self.ST_1 + self.ST_2 + self.ST_3 + self.ST_4 + self.ST_5 + self.ST_6
		self.db_total = 500


def get_query(gage, agr_dat):
	sql_qry = 'UPDATE gage_states_red_tote SET '
	sql_qry = sql_qry + ' st_1 = ' + str(agr_dat.ST_1) + ', '
	sql_qry = sql_qry + ' st_2 = ' + str(agr_dat.ST_2) + ', '
	sql_qry = sql_qry + ' st_3 = ' + str(agr_dat.ST_3) + ', '
	sql_qry = sql_qry + ' st_4 = ' + str(agr_dat.ST_4) + ', '
	sql_qry = sql_qry + ' st_5 = ' + str(agr_dat.ST_5) + ', '
	sql_qry = sql_qry + ' st_6 = ' + str(agr_dat.ST_6) + ', '
	sql_qry = sql_qry + ' last_update = Sysdate() '
	sql_qry = sql_qry + " WHERE  gage_id = '" + gage + "'"

	return sql_qry

try:

	gage_id = '22D21235C005'

	for c in gage_id:
		print(c + ' = ' + str(ord(c)))

	agr_vals = AgrStationCounts(gage_id)

	sql = get_query(gage_id, agr_vals)

	maint_changed = 'Hydromat Maint State Color Changed'

	rls = (1, 2, 3, 4, 5, 6, 7)

	for x in rls:
		print(x)

	rl = '*'.join(rls).upper()

	i = None
	i = int(i)
	print(int(i))


except Exception as e:
	e_msg_id = 'Test script error'
	e_msg_source = 'Hydromat v15/Scanner/Scanner Message/valueChanged. . . H7NFUR'

	err_handler(e_msg_id, e_msg_source, e)