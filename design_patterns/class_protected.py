# Many languages implement constructors with public, private and protected members
# Python sort of lets us do this...

class Employee(): # all classes default to inheriting from object
    '''This class represents an employee with name, age and isAdmin properties'''
    def __init__(self, name:str, age:int, isAdmin:bool):
        self.name = name         # public member. Visible everywhere
        # leading single underscore. protected. Accessible in this class and sub classes
        self._age = age  # WARNING: Python does not fully implement protection        
        # leading double-underscore. private. Accessible only in this class (not in sub classes)
        self.__isAdmin = isAdmin # this is name-mangled to prevent external access
    # here we have a 'protected' method
    def _defaultHelpResponse(self):
        return 'turn it off and on again'

class Intern(Employee): # NB usually separate classes live in separate modules
    '''inherit everything from the Employee class'''
    # NB inheritance works even without calling the parent __init__ method
    # def __init__(self, name, age, isAdmin):
    #     super().__init__(name, age, isAdmin)
    def askForHelp(self):
        # can we also access private members?
        if self.__isAdmin: # __isAdmin is NOT inherited (it is trully private)
            return('leave it with me, I\'ll ger back to you')
        else:
            return self._defaultHelpResponse() # inherited from parent

if __name__ == '__main__':
    emp = Intern('Ross', 30, True)
    # which members can we access
    print(emp.name) # all good (it is a public property)
    print(emp._age) # we can access the _age property, since it is inherited
    # print(emp.__isAdmin) # should fail, since member is private
    print(emp.askForHelp()) # NB we can also access protected methods here!!
