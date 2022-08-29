def log_prod_data(rec_type, val_1, val_2, val_3, val_4):

	params = {'msgID':rec_type,
              'msg1':val_1,
              'msg2':val_2,
              'msg3':val_3,
              'msg4':val_4}

	system.db.runNamedQuery("Logging/LogKeyData", params)