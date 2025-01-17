from passlib.context import CryptContext

from model.user import User
from repository.user import UserRepository
from schema import RegisterInput, LoginInput, LoginType
from middleware.JWTManager import JWTManager


class AuthenticationService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    async def login(login_data: LoginInput):
        # check existing user
        existing_user = await UserRepository.get_by_email(login_data.email)

        if not existing_user:
            raise ValueError("email not found!")

        if not AuthenticationService.pwd_context.verify(
            login_data.password, existing_user.password
        ):
            raise ValueError("Wrong Password!")

        token = JWTManager.generate_token({"sub": login_data.email})
        return LoginType(email=login_data.email, token=token)

    @staticmethod
    async def register(user_data: RegisterInput):
        existing_user = await UserRepository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("Email is registered!")

        user = User()
        user.email = user_data.email
        user.name = user_data.name
        user.password = AuthenticationService.pwd_context.hash(user_data.password)
        await UserRepository.create(user)

        return f"successfully registered data!"
