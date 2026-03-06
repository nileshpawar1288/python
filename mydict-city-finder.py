cities = {
    "helsinki": "Finland",
    "stockholm": "Sweden",
    "oslo": "Norway",
    "copenhagen": "Denmark",
    "mumbai": "India",

}
print(cities.keys())
print(cities.values())
city = input("enter city name: ")

if city in cities:
    print(f"{city} is in {cities[city]}")
else:    print(f"{city} is not in the dictionary")
