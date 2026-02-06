import random
import string
from datetime import datetime
import re
class UserUtil:
    @staticmethod
    def generate_user_id():
        current_year = str(datetime.now().year)[-2:]
        random_digits = ''.join(random.choices('0123456789', k=7))
        new_user_id = current_year + random_digits
        return new_user_id

    @staticmethod
    def generate_password():
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        chars = string.punctuation

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(chars)
        ]

        all_chars = lowercase + uppercase + digits +chars
        password+= random.choices(all_chars, k=4)
        random.shuffle(password)
        return ''.join(password)

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return password

        if not any(c.islower() for c in password):
            return password

        if not any(c.isupper() for c in password):
            return password

        if not any(c.isdigit() for c in password):
            return password

        if not any(c in string.punctuation for c in password):
            return password

        return password

    @staticmethod
    def generate_email(name, surname, domain):
        email = name + "." + surname + "@" + domain
        return email.lower()

    @staticmethod
    def validate_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return "Valid email" if re.match(regex, email) else "Not valid email"