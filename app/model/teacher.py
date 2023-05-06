class Teacher:
    """
    Teacher model class.
    
    Attributes:
        id: Teacher's id.
        firstname: Teacher's first name.
        lastname: Teacher's last name.
    """
    def __init__(self, id, firstname, lastname):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
        
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, value):
        self._firstname = value
        
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value):
        self._lastname = value
    
    def __str__(self):
        return f"{self.id}, {self.firstname}, {self.lastname}"

    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return False
        return (self.id == other.id and
                self.firstname == other.firstname and
                self.lastname == other.lastname)
    
    def __hash__(self):
        return hash((self.id, self.firstname, self.lastname))