
class InvalidUsername(Exception):
    pass

try:
    
    
    # username = input('username: ')

    raise InvalidUsername('test')


    if len(username) > 6:
        raise InvalidUsername('Username is too long')
    if '!' in username:
        raise InvalidUsername('Invalid character in username')

except InvalidUsername as e:
    print(repr(e))
    raise


