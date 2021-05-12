cities = ["Adelaide", "San Francisco", "New York", "Darwin", "Sydney"]

with open("/Users/Vasil/Desktop/Cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
