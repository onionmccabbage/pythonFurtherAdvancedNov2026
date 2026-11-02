import sys
# NB in Python 3.15 everything defults to UTF-8
class Redirect:
    '''This class will redirect output to another stream
    then recover the original output stream'''
    def __init__(self, new_stdout):
        '''this methd is called once, when we create an instance'''
        self.new_stdout = new_stdout # we may validate here with get/set methods
    def __enter__(self):
        '''this method is called every time we make use of an instance'''
        self.__original_stdout = sys.stdout # make a note of the curremt standard output
        sys.stdout = self.new_stdout # apply the new output stream
    # NB we MUST provide the arguemnts below
    def __exit__(self, exc_type, exc, tb):
        '''this method is called every time we stop using an instance'''
        sys.stdout = self.__original_stdout # pu things back how they were
    def __del__(self):
        '''often used for clean-up then the class instace is destroyed'''

def main():
    my_text = 'long string of content to be redirected'
    fout = open('logfile.txt', 'at')
    r = Redirect(fout)
    with r:
        print(my_text)
    print('Back to the default stdout (the console)')

if __name__ == '__main__':
    print( sys.stdout ) # default mode is 'w' for (over)write
    print( sys.stdin )  # default mode is 'r' for read, aas used with 'input'
    print( sys.stderr) 
    main()




