import random


class Location(object):

    AREA = {
        'NORTH_EAST': (35.86901, 139.81018),
        'NORTH_WEST': (35.86453, 139.32578),
        'SOUTH_EAST': (35.54527, 139.79325),
        'SOUTH_WEST': (35.58026, 139.33355),
    }

    def __init__(self):
        self.latitude = 35.68944
        self.longitude = 139.69167

    def random_find(self):
        latitude_max = max(self.AREA.values(), key=lambda x: x[0])[0]
        latitude_min = min(self.AREA.values(), key=lambda x: x[0])[0]
        longitude_max = max(self.AREA.values(), key=lambda x: x[1])[1]
        longitude_min = min(self.AREA.values(), key=lambda x: x[1])[1]

        self.latitude = random.uniform(latitude_min, latitude_max)
        self.longitude = random.uniform(longitude_min, longitude_max)
        return round(self.latitude, 5), round(self.longitude, 5)


if __name__ == "__main__":
    place = Location()
    destination = place.random_find()
    print(f'{destination[0]},{destination[1]}')
