
import uuid
from datetime import datetime

class BaseModel:
     """
    This is a base model class for our program.
    defines all common attributes/methods for other classes.
    """
    def __init__(self):
         """
        Constructor method for BaseModel.
        Initializes a new instance of BaseModel with the given name.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for each instance
        self.created_at = datetime.now()  # Assign current datetime when instance is created
        self.updated_at = datetime.now()  # Assign current datetime when instance is created

