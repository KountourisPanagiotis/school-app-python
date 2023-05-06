class TeacherNotFound(Exception):
    """
    Teacher not found exception class.
    """
    def __init__(self, teacher_id):
        
        # constructor of super class Exception
        super().__init__(f"Teacher id: [{teacher_id}] was not found")
 
class TeacherAlreadyExists(Exception):
    """
    Teacher already exists exception class.
    """
    def __init__(self, teacher_id):
        
        # constructor of super class Exception
        super().__init__(f"Teacher id: [{teacher_id}] already exists")
