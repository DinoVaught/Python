
class ExitSub(Exception):
    pass


try:
    testVal = 'ZZhelloZZ'
    output = {}  # Dictionary

    raise ExitSub('')

    raise Exception('hello error')

    for x in testVal:
        if x not in output.keys():
            output[x] = testVal.count(x)

    print (str(output))


except ExitSub:
    pass


except Exception as e:
    err = getattr(e, 'message', repr(e))
    print(err)
