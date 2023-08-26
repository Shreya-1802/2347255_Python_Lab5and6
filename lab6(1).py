import re
def find_phone_number(input_string):
    phone_pattern = re.compile(r'(\(\d{3}\)-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})')
    match = phone_pattern.search(input_string)
    if match:
        return match.group()
    else:
        return None

input_text = "Please contact me at (123)-456-7890 or 987-654-3210."
phone_number = find_phone_number(input_text)
if phone_number:
    print("Valid phone number found:", phone_number)
else:
    print("No valid phone number found.")
