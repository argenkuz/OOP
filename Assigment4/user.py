from datetime import datetime ,date

class User:
    def __init__(self, user_id:int, name:str, surname:str ,email:str, password:str, birthday:str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.surname = surname
        self.password = password
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()


    def get_details(self):
        return f"ID:{self.user_id} \nName: {self.name} \nSurname: {self.surname} \nEmail: {self.email} \nPassword: {self.password} \nBirthday: {self.birthday}"

    def get_age(self):
        today = date.today()
        birthdate = self.birthday
        age = today.year - birthdate.year

        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        return age
