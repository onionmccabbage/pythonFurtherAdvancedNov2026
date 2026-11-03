CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]
# Any ordinal collectin can be used as an iterable like this
c = iter(CITIES)

# we can then grab each member in turn like this
# print( next(c) )
# print( next(c) )
# print( next(c) )
# print( next(c) )
# print( next(c) )

# Alternatively, use a generator
def genCities(l):
    '''yield values for city names derived from l'''
    for _ in l:
        yield _ # the yield statement makes this function become a generator


if __name__ == '__main__':
    gc = genCities(CITIES)
    print( gc )
    print( gc.__next__() ) # Dublin
    print( gc.__next__() ) # 
    print( gc.__next__() ) # 
    print( gc.__next__() ) # 
