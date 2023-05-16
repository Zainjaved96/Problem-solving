from functools import  wraps

def make_secure(func):
    @wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


# use this without @ 
# get_admin_password = make_secure(get_admin_password)
user = {"username": "jose", "access_level": "admin"}
print(get_admin_password.__name__)
