from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.exception import CustomException
from src.model.feedback import Feedback_Class


class FeedbackRepository:

    @staticmethod
    def Create_Feedback():
        pass

    @staticmethod
    def Get_Feedback_By_ID(feedback_id, db):
        try:
            return db.execute(
                select(Feedback_Class).
                where(Feedback_Class.feedback_id == feedback_id)
                .scalars()
                .first()
                )
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("Error While Fetching Feedback by id")

    @staticmethod
    def Update_Feedback():
        pass

    @staticmethod
    def Soft_Delete_Feedback():
        pass

    @staticmethod
    def Hard_Delete_Feedback(feedback, db):
        try:
            db.delete(feedback)
            db.commit()
            return {
                'message' : 'Feedback Deleted!!!'
            }
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(e) from e