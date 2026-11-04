import time
from threading import Thread, Semaphore, current_thread
import requests
from weather import Weather

# some global assets
CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]
# CITIES = [
#     'Athlone', 'Galway', 'Belfast', 
#     'Genoa', 'Cork', 'Madrid'
# ]
n_threads = 4 # NB usually a power of two
thread_list = []
reports = []
sem = Semaphore(1)

# print( f'[{current_thread().name}] {w}')

class WeatherGetter(Thread):
    def __init__(self):
        Thread.__init__(self)
        global CITIES
        global reports
        global sem
    def run(self):
        while len(CITIES)>0:
            sem.acquire()
            self.city = CITIES.pop() # we could use a city genertor here (or DB etc.
            # print(CITIES)
            sem.release()
            url_template = (
                'http://api.openweathermap.org/data/2.5/'
                'weather?q={}&units={}&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
            response = requests.get(url_template.format(self.city, 'metric'))
            data = response.json()
            self.temperature = data['main']['temp']
            self.description = data['weather'][0]['description']
            weather = Weather(city=self.city, temp=self.temperature, desc=self.description)
            reports.append(weather)

def main():
    start = time.perf_counter()
    for _ in range(0, n_threads):
        wg = WeatherGetter()
        thread_list.append(wg)
        wg.start()
    # now we wait for all the threads to complete
    for thread in thread_list:
        thread.join()
    print(f"Time: {time.perf_counter() - start} seconds")
    for report in reports:
        print(report) # each report is a Weather isntance, with __str__

if __name__ == '__main__':
    main()
