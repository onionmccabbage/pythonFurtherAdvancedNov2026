# Many languages implement constructors with public, private and protected members
# Python sort of lets us do this...

class Employee(): # all classes default to inheriting from object
    '''This class represents an employee with name, age and isAdmin properties'''
    def __init__(self, name:str, age:int, isAdmin:bool):
        self.name = name         # public member. Visible everywhere
        # leading single underscore. protected. Accessible in this class and sub classes
        self._age = age  # WARNING: Python does not fully implement protection        
        # leading double-underscore. private. Accessible only in this class (not in sub classes)
        self.__isAdmin = isAdmin 
    # here we have a 'protected' method
    def _defaultHelpResponse(self):
        return 'tun it off and on again'

class Intern(Employee): # NB usually separate classes live in separate modules
    '''inherit everything from the Employe class'''

if __name__ == '__main__':
    emp = Intern('Ross', 30, True)
    # which members can we access
    print(emp.name) # all good (it is a public property)