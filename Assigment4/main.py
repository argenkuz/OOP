from user import User
from userservice import UserService
from userutil import UserUtil

def main():
    user_id = UserUtil.generate_user_id()
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    email = UserUtil.generate_email(name, surname, "gmail.com")
    password = UserUtil.generate_password()
    birthday = input("Enter your birthday YYYY-MM-DD(like 2000-01-01): ")

    user = User(user_id, name, surname, email, password, birthday)
    UserService.add_user(user)
    print(f"User added successfully! \n{user.get_details()}")

    print(f"User age: {user.get_age()}")

    email_validation = UserUtil.validate_email(email)
    print(f"\nEmail validation: {email} is {email_validation}")

    password_strength = UserUtil.is_strong_password(password)
    print(f"Password strength: {password_strength} is strong")


if __name__ == "__main__":
    main()