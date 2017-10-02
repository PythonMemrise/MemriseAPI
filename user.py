#MemriseAPI
import urllib
import mem_exceptions
from course import get_pagetext

__all__ = ['courses_learning', 'courses_learning_number', 'courses_teaching', 'courses_teaching_number', 'dailygoal',  'mems', 'number_of_followers', 'number_of_following', 'points', 'promember', 'top50learncompetition',
           'words', 'usertest']

actuality = coerce(1.2, 10.2017) #version: 1.2 last, last update: October 2017



def usertest(user):
    try:
        url = "https://www.memrise.com/user/" + user
        global pagetext
        pagetext = urllib.urlopen(url).read()
        if "<h2>The page you are trying to get to doesn't exist.</h2>" in pagetext:
            global exist
            exist = False
        else:
            exist = True
    except IOError:
        raise mem_exceptions.NoConnection()
    
def linenumber(url, text): #gets the number of a line
    myData = urllib.urlopen(url)   
    for num, line in enumerate(myData, 1):
        if text in line:
            return int(num)


def promember(user):
    """True, if user is pro member and False, if user isn't pro member!"""
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
            try:
                url = "http://memrise.com/user/" + user
                if 'data-original-title="Pro' in urllib.urlopen(url).read():
                    return True
                else:
                    return False
            except IOError:
                raise mem_exceptions.NoConnection()
    

def top50learncompetition(user):
    """True, if the user is in the top 50 of the September Back-to-School learning Competition"""    
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "http://memrise.com/user/" + user
            if 'data-original-title="TOP' in urllib.urlopen(url).read():
                return True
            else:
                return False
        except IOError:
            raise mem_exceptions.NoConnection()

   
def dailygoal(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
            try:
                url = "https://www.memrise.com/user/" + user + "/mems/created/"
                mems_line = linenumber(url, 'streak')
                lines = list(pagetext.split("\n"))
                line =  str(lines[mems_line+9])
                repl = line.replace("</b>", "").replace("<b>", "") #kill HTML                
                return repl
            except TypeError:
                pass
            except IOError:
                raise mem_exceptions.NoConnection()

     
def mems(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "https://www.memrise.com/user/" + user + "/mems/created/"
            mems_line = linenumber(url, 'Created')
            lines = pagetext.split("\n")
            return lines[mems_line-1]
        except TypeError:
            return 0
        except IOError:
            raise mem_exceptions.NoConnection()
        
def points(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "https://www.memrise.com/user/" + user
            points_line = linenumber(url, 'Points')
            lines = pagetext.split("\n")
            return lines[points_line-4]
        except TypeError:
                return 0
        except IOError:
                raise mem_exceptions.NoConnection()
def words(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "https://www.memrise.com/user/" + user
            words_line = linenumber(url, 'Words')
            lines = pagetext.split("\n")
            return lines[words_line-5]
        except TypeError:
                return 0
        except IOError:
                raise mem_exceptions.NoConnection()

def number_of_followers(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "https://www.memrise.com/user/" + user
            followers_line = linenumber(url, 'Follower')
            lines = pagetext.split("\n")
            return lines[followers_line-6]
        except TypeError:
            return 0
        except IOError:
                raise mem_exceptions.NoConnection()

def number_of_following(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "https://www.memrise.com/user/" + user
            following_line = linenumber(url, 'Following')
            lines = pagetext.split("\n")
            return lines[following_line-5]
        except TypeError:
                return 0
        except IOError:
                raise mem_exceptions.NoConnection()

def courses_learning_number(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
           try:
                      url = "http://memrise.com/user/" + user + "/courses/teaching"
                      text = get_pagetext(url)
                      matched_lines = [line for line in text.split('\n') if "" in line]
                      return matched_lines[35]
           except IOError:
                      raise mem_exceptions.NoConnection()
       
def courses_teaching_number(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "http://memrise.com/user/" + user + "/courses/teaching"
            text = get_pagetext(url)
            matched_lines = [line for line in text.split('\n') if "" in line]
            return matched_lines[36]
        except IOError:
            raise mem_exceptions.NoConnection()
        
def courses_learning(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "http://memrise.com/user/" + user + "/courses/learning"
            text = get_pagetext(url)
            matched_lines = [line for line in text.split('\n') if "" in line]
            for el in range(39, len(matched_lines)-43):
                    print matched_lines[el]
        except IOError:
            raise mem_exceptions.NoConnection()
                
def courses_teaching(user):
    usertest(user)
    if exist == False:
        raise mem_exceptions.UserError()
    if exist == True:
        try:
            url = "http://memrise.com/user/" + user + "/courses/teaching"
            text = get_pagetext(url)
            matched_lines = [line for line in text.split('\n') if "" in line]
            for el in range(39, len(matched_lines)-42):
                    print matched_lines[el]
        except IOError:
            raise mem_exceptions.NoConnection()
    
         
   
