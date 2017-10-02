#MemriseAPI
actuality = coerce(1.2, 9.2017) #version: 1.2 last, last update: October 2017

__all__ = ['actuality', 'CourseError', 'NoConnection', 'UserError']

class NoConnection(Exception):
    def __init__(self):
        self.msg = "Can't connect to memrise.com!"
    def __str__(self):
        return self.msg
   
class UserError(Warning):
    def __init__(self):
        self.msg = "This user doesn't exist!"
    def __str__(self):
        return self.msg
   
class CourseError(Exception):
    pass


