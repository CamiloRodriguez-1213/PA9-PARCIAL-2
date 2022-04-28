import string
import random
def newToken():
    length_of_string = 6
    token =(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    return token