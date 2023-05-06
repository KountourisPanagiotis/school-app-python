from abc import ABC, abstractmethod
from model.teacher import Teacher
from dao.teacher_dao import ABCTeacherDAO
from exceptions.dao_exceptions import TeacherNotFound, TeacherAlreadyExists
from typing import List

class ABCTeacherService(ABC):
    """
    Defines the Teacher Service API
    """
    @abstractmethod
    def add_teacher(self, teacher: Teacher):
        """
        Inserts a new teacher record into the database
        """
        pass

    @abstractmethod
    def update_teacher(self, teacher: Teacher):
        """
        Updates an existing teacher record in the database
        """
        pass

    @abstractmethod
    def delete_teacher(self, teacher_id: int):
        """
        Deletes an existing teacher record from the database
        """
        pass

    @abstractmethod
    def get_teacher(self, teacher_id: int) -> Teacher:
        """
        Retrieves a single teacher record from the database by ID
        """
        pass

    @abstractmethod
    def get_all_teachers(self) -> List[Teacher]:
        """
        Retrieves all teacher records from the database
        """
        pass

class TeacherServiceImpl(ABCTeacherService):
    """
    Implements the methods of the teacher Service interface
    """
    def __init__(self, dao: ABCTeacherDAO):
        self.dao = dao

    def add_teacher(self, teacher: Teacher):
        try:
            self.dao.insert(teacher)
        except TeacherAlreadyExists as e:
            raise e
        except Exception as e:
            raise e

    def update_teacher(self, teacher: Teacher):
        try:
            self.dao.update(teacher)
        except TeacherNotFound as e:
            raise e
        except Exception as e:
            raise e

    def delete_teacher(self, teacher_id: int):
        try:
            teacher = Teacher(id=teacher_id,  firstname=None, lastname=None)
            print(teacher , "<----------------------------------") 
            teacher = self.dao.getOne(teacher)
            self.dao.delete(teacher)
        except TeacherNotFound as e:
            raise e
        except Exception as e:
            raise e

    def get_teacher(self, teacher_id: int):
        try:
            teacher = Teacher(id=teacher_id,  firstname=None, lastname=None)
            return self.dao.getOne(teacher)
        except TeacherNotFound as e:
            raise e
        except Exception as e:
            raise e

    def get_all_teachers(self) -> List[Teacher]:
        try:
            return self.dao.getAll()
        except Exception as e:
            raise e