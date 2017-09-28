#MemriseAPI
import urllib
import sys
from datetime import datetime as dt
import requests
import mem_exceptions

__all__ = ['actuality', 'allcourses', 'courseinfo', 'coursenumber', 'coursetest']

actuality = coerce(1.0, 9.2017) #version: 1.0 last, last update: September 2017


def linenumber(url, text): #gets the number of a line
    myData = urllib.urlopen(url)   
    for num, line in enumerate(myData, 1):
        if text in line:
            return int(num)


def coursetest(id):
    try:
        url = "http://www.memrise.com/course/" + str(id)
        if "<h2>The page you are trying to get to doesn't exist.</h2>" in urllib.urlopen(url).read():
            global exist
            exist = False
            return exist
        else:
            exist = True
            return exist
    except IOError:
        raise mem_exceptions.NoConnection()

#wie viele kurse werden taeglich gemacht? Daraus mit datetime errechnen den start fuer newestcourse()

def coursenumber():
    try:
        start = 1580000
        for i in range(1, 20000, 1000):
            nstart = start + i
            print nstart
            url = "http://www.memrise.com/course/" + str(nstart)
            if "<h2>The page you are trying to get to doesn't exist.</h2>" in urllib.urlopen(url).read():
                return "Current course: " + nstart
                break
    except IOError:
        raise mem_exceptions.NoConnection()



def get_pagetext(url):
    from bs4 import BeautifulSoup
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
        # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)
    return text


def courseinfo(id):
    if id <= 0 or len(str(id)) >= 10:
        raise mem_exceptions.CourseError("This course can't exist!")
    try:
        coursetest(id) #does the course exist?
        if exist == False:
            raise mem_exceptions.CourseError("This course doesn't exist!")
        text = get_pagetext("http://memrise.com/course/" + str(id))
        matched_lines = [line for line in text.split('\n') if "" in line]
        url = ("http://memrise.com/course/" + str(id) + "/" + str(matched_lines[25]) + "/leaderboard").replace(" ", "-").lower()    
        author = get_pagetext(url)
        author_line = [line for line in author.split('\n') if "" in line]
    
        if matched_lines[26] != u"Welcome to Memrise!":
            line26 = "\n" + matched_lines[26]
        else:
            line26 = ""
        try:
            return str(matched_lines[22:25]) + "\n" + matched_lines[25] + line26 + "\n" + author_line[22]
        except IndexError:
            pass
    except UnicodeEncodeError:
        if matched_lines[26] != u"Welcome to Memrise!":
            line26 = "\n" + matched_lines[26]
        else:
            line26 = ""
        return str(matched_lines[22:25]) + "\n" + matched_lines[25] + line26
    except IOError:
        raise mem_exceptions.NoConnection()


def allcourses(course_info=False):
    """print a list of all available courses"""
    if course_info == False:
        for i in range(1600000):
            if coursetest(i) == True:
                    print i
    if course_info == True:
        for i in range(1600000):
            try:
                if coursetest(i) == True:
                        print str(i), courseinfo(i)
            except KeyboardInterrupt:
                break
            except IOError:
                raise mem_exceptions.NoConnection()
    if course_info == Ellipsis:
        raise SyntaxError
    else:
        raise mem_exceptions.CourseError("course_info can't be like this. Only true or false.")

