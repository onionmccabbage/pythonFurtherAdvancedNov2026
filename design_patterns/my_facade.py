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

class Manager:
    pass


if __name__ == '__main__':
    pass