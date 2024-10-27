from faker import Faker
class Urls:

    URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN = f"{URL}login"
    FORGOT_PASSWORD = f"{URL}forgot-password"
    ORDER_FEED = f"{URL}feed"
    RESTORE_PASS = f"{URL}reset-password"
    CREATE_USER = f"{URL}api/auth/register"
    DELETE_USER = f"{URL}api/auth/user"
    PERSONAL_ACCOUNT = f"{URL}account/profile"
    ORDER_LIST = f"{URL}account/order-history"


class UserData:
    @staticmethod
    def generate_user():
        fake = Faker()
        user_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return user_data


