# a service to access https://swapi.dev/api
import requests

class SwapiService():
    def __init__(self):
        pass
    def getSwapi(self, category='people', id=1): # sensible defaults
        url = f"https://swapi.dev/api/{category}/{id}"
        # print(url)
        response = requests.get(url)
        if response.json() == {'detail': 'Not found.'}:
            r = 'problem'
        else:
            r = response.json()
        # print(r)
        return r
        
if __name__ == "__main__":
    swapi = SwapiService()
    p = swapi.getSwapi('vehicle', 3)
    print(p)