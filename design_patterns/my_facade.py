# a facade gives us a single point of entry to many different classes, functions etc.
# here are some disparate classes (containing different functionality)
class Coder:
    def __init__(self):
        print('coder writes some code')
    def __isAvailable(self):
        return True # we would have logic to return True/False
    def book_time(self):
        if self.__isAvailable():
            print('coder is available and has been booked')

class Tester:
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place for due diligence')

class Technician:
    def __init__(self):
        print('preparing equipment for the team')
    def doTechyStuff(stuff):
        print('equipment is in place and configured')

class Artisan:
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')


# tyically all the subsystems would be imported from elsewhere
class Manager:
    '''This manager will be a facade to all the other classes
    They are each different and can be accessed via the manager'''
    def __init__(self):
        print('The manager says I can arrange a project team')
    def arrange(self):
        '''The facade provides instances of each other subsystem'''
        self.coder = Coder()
        self.technician = Technician()
        self.tester = Tester()
        self.artisan = Artisan()
        # we may manage these subsystems
        self.coder.book_time()
        self.tester.testing()
        self.technician.doTechyStuff()
        self.artisan.make_prototype()


if __name__ == '__main__':
    m = Manager()
    m.arrange()