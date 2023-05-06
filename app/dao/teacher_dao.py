from abc import ABC, abstractmethod
import mysql.connector
from model.teacher import Teacher
from exceptions.dao_exceptions import TeacherNotFound, TeacherAlreadyExists
from database.db_connection import conn as conn

class ABCTeacherDAO(ABC):
    """
    Defines the Teacher DAO API
    """
    @abstractmethod
    def insert(self,  teacher_to_insert):
        """
        Inserts a new teacher record into the database
        """
        pass

    @abstractmethod
    def update(self, teacher_to_update):
        """
        Updates an existing teacher record in the database
        """
        pass

    @abstractmethod
    def delete(self, teacher_to_delete):
        """
        Deletes an existing teacher record from the database
        """
        pass

    @abstractmethod
    def getOne(self, teacher_id):
        """
        Retrieves a single teacher record from the database by ID
        """
        pass

    @abstractmethod
    def getAll(self):
        """
        Retrieves all teacher records from the database
        """
        pass


class TeacherDAOImpl(ABCTeacherDAO):
    """
    Implements the methods of the teacher DAO interface
    """
    def __init__(self, conn):
        self.conn = conn

    def insert(self, teacher_to_insert):
        """
        Inserts a new teacher record into the database
        """
        cursor = self.conn.cursor()
        query = "INSERT INTO teachers (id, firstname, lastname) VALUES (%s, %s, %s)"
        values = (teacher_to_insert.id, teacher_to_insert.firstname, teacher_to_insert.lastname)
        try:
            cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.IntegrityError:
            raise TeacherAlreadyExists(teacher_to_insert.id)
        finally:
            cursor.close()

    def update(self, teacher_to_update):
        """
        Updates an existing teacher record in the database
        """
        cursor = self.conn.cursor()
        query = "UPDATE teachers SET firstname = %s, lastname = %s WHERE id = %s"
        values = (teacher_to_update.firstname, teacher_to_update.lastname, teacher_to_update.id)
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            raise TeacherNotFound(teacher_to_update.id)
        self.conn.commit()
        cursor.close()

    def delete(self, teacher_to_delete):
        """
        Deletes an existing teacher record from the database
        """
        cursor = self.conn.cursor()
        query = "DELETE FROM teachers WHERE id = %s"
        values = (teacher_to_delete.id,)
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            raise TeacherNotFound(teacher_to_delete.id)
        self.conn.commit()
        cursor.close()

    def getOne(self, teacher: Teacher):
        """
        Retrieves a single teacher record from the database by ID
        """
        cursor = self.conn.cursor()
        query = "SELECT id, firstname, lastname FROM teachers WHERE id = %s"
        values = (teacher.id,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            raise TeacherNotFound(teacher.id)
        return Teacher(*row)

    def getAll(self):
        """
        Retrieves all teacher records from the database
        """
        cursor = self.conn.cursor()
        query = "SELECT id, firstname, lastname FROM teachers"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        teachers = []
        for row in rows:
            teachers.append(Teacher(*row))
        return teachers
