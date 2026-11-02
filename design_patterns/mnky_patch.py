# monkey-patching is a pattern for fixing code
# especially useful when writing tests or mocks for tests
# also good when we cannot edit the original
# use with caution: make sure to provide ample documentation and warnings

import class_protected as clap

# declare a new function (to bee used as a monkey patch)
def munction(self):
    return 'This simian is of unknown age'

#replace the 'showAge' method with our new function
clap.Intern.showAge = munction # replace the original with a new function

a = clap.Intern('Arthur', None, False)
print( a.showAge() )