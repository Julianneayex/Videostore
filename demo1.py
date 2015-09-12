from sys import argv
import datetime
from datetime import date, datetime,time,timedelta
    
class Customer(object):
    def __init__(self,name,idNo,bag=[]):
        self.name = name
        self.idNo = idNo
        self.bag =  bag

# print information about the Customer    
    def printinfo(self):
        print "\n*******************CUSTOMER INFORMATION**********************"
        print ('%-20s %-20s' % ("Name", "Id Number",))
        print ('%-20s %-20s' % (self.name, self.idNo,))

class Movie(object):
    movies = 4
    def __init__(self)
        self.moviename = moviename
        self.cost = cost
        self.category =category
        self.store = store

    def lend_movie(self,name,moviename,store=[]):
        self.store.remove(movie)
        c.bag.append(movie)
        

#print movie info
        def printinfo(self):
               print "\n********MOVIE INFO********"
               print ('%-20s %-200s ' % (self.moviename, self.cost))
          

class Charge(object):
    def __init__ (self,discount):
        self.name = name
        self.discount = discount

#creating an instance of a class
    
    

def main():
        print "\n*******************MOVIES MOVIES**********************"
        c = Customer('Daniel',1)
        c.printinfo()

main()
