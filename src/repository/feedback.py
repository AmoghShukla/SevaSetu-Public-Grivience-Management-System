from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.exception import CustomException
from src.model.user import User_Class


class FeedbackRepository:

    @staticmethod
    def Create_Feedback():
        pass

    @staticmethod
    def Get_Feedback_By_ID(user_id, db):
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
    def Update_Feedback():
        pass

    @staticmethod
    def Soft_Delete_Feedback():
        pass

    @staticmethod
    def Hard_Delete_Feedback(user, db):
        try:
            db.delete(user)
            db.commit()
            return {
                'message' : 'User Deleted!!!'
            }
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(e) from e