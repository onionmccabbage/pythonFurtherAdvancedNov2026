# you my need to add the requests library
# pip install requests
# python -m pip install requests
# you may need to do this at location of your Python.exe

import requests

def getStuff(n):
    # get is most common. We may use post, put, update etc.
    result = requests.get(f'https://jsonplaceholder.typicode.com/photos/{n}')
    # .json(), .text(), .xml() etc.
    return result.json() # we now have Python structured data

if __name__ == '__main__':
    f = getStuff(8)
    print(f) # we have a dictionary

