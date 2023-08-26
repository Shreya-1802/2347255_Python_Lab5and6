import re
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()-_=+{}\[\]:;",.<>?\\|]', password):
        return False    
    return True

password = "Christ@123"
if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is not strong.")
