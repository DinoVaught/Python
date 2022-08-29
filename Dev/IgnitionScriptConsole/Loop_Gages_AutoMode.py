for i in range(1, 28, 1):
    gage = 'G' + str(i).zfill(2)

    path = '[default]' + gage + '/' + gage + '/Gage/Auto Mode'

    am = system.tag.readBlocking([path])[0].value
    if am == False:
        print(gage + ' Auto Mode = ' + str(am))