from sqlalchemy.exc import SQLAlchemyError


class UserRepository:

    @staticmethod
    def Create_User():
        pass

    @staticmethod
    def Get_User_By_ID():
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