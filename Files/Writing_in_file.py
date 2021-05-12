# cities = ["Adelaide", "San Francisco", "New York", "Darwin", "Sydney"]
#
# with open("/Users/Vasil/Desktop/Cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True) # flush the memory buffer.
#         # not needed in modern computers

cities = []
with open("/Users/Vasil/Desktop/Cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

