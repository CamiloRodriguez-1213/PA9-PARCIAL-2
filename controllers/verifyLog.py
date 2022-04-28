from flask import session
def verifyLogin():
    if 'username' in session:
        return True
    else:
        return False
