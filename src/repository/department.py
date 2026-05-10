from sqlalchemy.exc import SQLAlchemyError

from src.exception import CustomException


class DepartmentRepository:

    @staticmethod
    def Create_Department():
        pass
    
    @staticmethod
    def Hard_Delete_Department(department, db):
        try:
            db.delete(department)
            db.commit()
            return {
                'message' : 'Department Deleted!!!'
            }
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(e) from e