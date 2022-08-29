# Returns the part of (value) that is on the right side of (delimiter)
def strRightDelim(value, delimiter):
    try:

        iLoc = value.index(delimiter)
        retVal = value[iLoc+ + len(delimiter) : len(value)]
        return retVal

    except ValueError: # delimiter does not exist in search string
        return "delimiter error"
    except:
        return "Error"

# Returns right number of chars (numChars) of (value)
def strRightNumChrs(value, numChars):
    try:
        return value[len(value) - numChars : len(value)]
    except:
        return "Error"
        
def strIsNumeric(val):
	for c in val:
		if not (48 <= ord(c) <= 57):  # if ord(c) is not between 48 and 57
			return False              # ord(c) is not numeric

	return True


def isInteger(val):
	try:
		num = int(val)
		return True
	except Exception as e:
		return False
		
def strHasNulls(strVal):

	for c in strVal:
		if ord(c) == 0:
			return True

	return False
