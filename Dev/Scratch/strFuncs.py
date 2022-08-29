

# Returns the part of (value) that is on the right side of (delimiter)
def strRightDelim(value, delimiter):
    try:

        iLoc = value.index(delimiter)
        retVal = value[iLoc+ + len(delimiter) : len(value)]
        return retVal

    except ValueError: # delimiter does not exist is search string
        return "delimiter error"
    except:
        return "Error"

# Returns right number of chars (numChars) of (value)
def strRightNumChrs(value, numChars):
    try:
        return value[len(value) - numChars : len(value)]
    except:
        return "Error"




# partNumX = "G10-648"
partNum = "UN078284737100001408"
retVal= strRightNumChrs(partNum, 9)
print(retVal)

