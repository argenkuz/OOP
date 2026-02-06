class UserService:
    users = []

    @classmethod
    def add_user(cls, user):
        cls.users.append(user)

    @classmethod
    def find_user(cls,user_id):
        for user in cls.users:
            if user.user_id == user_id:
                return user
        return "User not found!"

    @classmethod
    def delete_user(cls,user_id):
        for user in cls.users:
            if user.user_id == user_id:
                cls.users.remove(user)
                break

    @classmethod
    def update_user(cls, user_id, name, email):
        user = cls.find_user(user_id)
        if user != "User not found!":
            user.name = name
            user.email = email
            return user

    @classmethod
    def get_number(cls):
        return len(cls.users)


