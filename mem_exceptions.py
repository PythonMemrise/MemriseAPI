

class NoConnection(Exception):
    def __init__(self):
        self.msg = "There is no connection!"
    def __str__(self):
        return self.msg
   
class UserError(Warning):
    def __init__(self):
        self.msg = "This user doesn't exist!"
    def __str__(self):
        return self.msg
   
class CourseError(Exception):
    pass


