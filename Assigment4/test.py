import unittest
from user import User
from userservice import UserService
from userutil import UserUtil

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(user_id=230121012, name="Argen", surname="Kulzhanov", email="argen.kulzhanov@gmail.com", password="password123", birthday="2005-12-07")

    def test_get_details(self):
        details = self.user.get_details()
        print(f"\nUser Details: {details}")
        self.assertEqual(details, ":ID:230121012, Name: Argen, Surname: Kulzhanov, Email: argen.kulzhanov@gmail.com, Password: password123, Birthday: 2005-12-07")

    def test_get_age(self):
        age = self.user.get_age()
        print(f"\nUser Age: {self.user.name} {age}")
        self.assertEqual(age, 19)


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user1 = User(230121012, "Argen", "Kulzhanov", "argen.kulzhanov@gmail.com", "password123", "2005-12-07")
        self.user2 = User(230121008, "Kirill", "Donetskov", "kirill.donetskov@gmil.com", "password456","2005-06-12")

        UserService().add_user(self.user1)
        UserService().add_user(self.user2)

    def test_find_users(self):
        user = UserService.find_user(230121012)
        self.assertEqual(user.user_id, self.user1.user_id)
        self.assertEqual(user.name, self.user1.name)
        self.assertEqual(user.surname, self.user1.surname)
        self.assertEqual(user.email, self.user1.email)
        self.assertEqual(user.password, self.user1.password)
        self.assertEqual(user.birthday, self.user1.birthday)

    def test_add_user(self):
        new_user = User(230121024, "Meder", "Rahatbekov", "meder.rahatbekov@gmail.com", "password789", "2003-03-15")
        UserService().add_user(new_user)
        self.assertEqual(len(UserService().users), 3)
        print("\nAdded Users:")
        for user in UserService.users:
            print(user.get_details())

    def test_delete_user(self):
        user = UserService().delete_user(230121012)

        self.assertEqual(user, None)
        print(f"\n5)User: {user}")

    def test_update_user(self):
        print(f"Before Update: {self.user2.get_details()}")
        updated_user = UserService.update_user(230121008, "Beks",  "beks.kulzhanov@gmail.com")
        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.name, "Beks")
        self.assertEqual(updated_user.email, "beks.kulzhanov@gmail.com")
        print(f"\n6)Updated User: {updated_user.get_details()}")

class TestUseUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(isinstance(user_id, str) and len(str(user_id)) == 9)
        print(f"\n7)Generated User ID: {user_id}")

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(len(password) >= 8)
        print(f"\n8)Generated Password: {password}")

    def test_is_strong_password(self):
        print(f"\n9)Generated password is strong: {UserUtil.is_strong_password(UserUtil.generate_password())}")
        print(f"    Password is strong: {UserUtil.is_strong_password('Password123!')}")
        print(f"    Password is weak: {UserUtil.is_strong_password('password123')}")

    def test_generate_email(self):
        email = UserUtil.generate_email("Maga", "Magomedow", "gmail.com")
        self.assertEqual(email, "maga.magomedow@gmail.com")
        print(f"\n10)Generated Email: {email}")

    def test_validate_email(self):
        email = UserUtil.generate_email("Maga", "Magomedow", "gmail.com")
        invalid_email = UserUtil.validate_email("test@.com")
        validation_result = UserUtil.validate_email(email)
        self.assertEqual(validation_result, "Valid email")
        self.assertEqual(invalid_email, "Not valid email")

        print(f"\n11)Generated email: {email} is {validation_result}")
        print(f"   Invalid email: {email} is {invalid_email}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
