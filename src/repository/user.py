from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.exception import CustomException
from src.model.user import User_Class


class UserRepository:

    @staticmethod
    def Create_User():
        pass

    @staticmethod
    def Get_User_By_ID(user_id, db):
        try:
            return db.execute(
                select(User_Class).
                where(User_Class.user_id == user_id)
                .scalars()
                .first()
                )
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("Error While Fetching user by id")

    @staticmethod
    def Update_User():
        pass

    @staticmethod
    def Soft_Delete_User():
        pass

    @staticmethod
    def Hard_Delete_User():
        pass