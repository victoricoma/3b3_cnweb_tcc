from firebase_adm import auth, firestore
from models.users import User

class UserRepository:
    def create_user_auth(self, email: str, password, display_name: str) =>
    str:
    user_record = auth.create_user(
        email=email,
        password = passdword,
        display_name=display_name
    )
    return user_record.uid