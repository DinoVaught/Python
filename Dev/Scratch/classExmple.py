
class ReprintFields():
    part = 0 # id part (3 digit number) represents the "part"
    barCode = 1 # concatenation of (base) and (skid_ndx) from table mes.skid_id
    dateTime = 2 
    wip_ID = 3
    heat = 4
    skid_ID = 5
    asset = 6 # machine name (D21) for example
    gageName = 7 # Gage name (G21) for example

# The values stored in AGR_LowNums are the subtrahends (the number that will be subtracted) 
# used to calculate how many parts were rejected in a tote
class AGR_LowNums():
    STN_1 = 0
    STN_2 = 0
    STN_3 = 0
    STN_4 = 0
    STN_5 = 0
    STN_6 = 0

# This class is a model of the field names (columns) returned from query AGR_Counts/get_active_rec_black_tote
# Allowing the use of human-readable words where column numbers are used
class AGR_ActiveRecord():
    fld_STN_1 = 2
    fld_STN_2 = 3
    fld_STN_3 = 4
    fld_STN_4 = 5
    fld_STN_5 = 6
    fld_STN_6 = 7


LowVals = AGR_LowNums

LowVals.STN_1 = 9358475
LowVals.STN_2 = 9876543210

print(LowVals.STN_1)
print(LowVals.STN_2)
