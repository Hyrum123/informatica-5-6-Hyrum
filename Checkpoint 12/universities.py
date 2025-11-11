import requests

universities = {"Tecmilenio": {"majors": 9, "cost": 1200, "distance": 299, "name": "Universidad Tecmilenio"}, 
                "UACJ": {"majors": 8, "cost": 3800, "distance": 308, "name": "Universidad Autónoma de Ciudad Juárez"}, 
                "BYUI": {"majors": 90, "cost": 4400, "distance": 1985, "name": "Brigham Young University - Idaho"}, 
                "ITS NCG": {"majors": 7, "cost": 2940, "distance": 25, "name": "Instituto Tecnológico Superior de Nuevo Casas Grandes"}, 
                "ELPAC": {"majors": 1, "cost": 28000, "distance": 283, "name": "Universidad Autónoma de Chihuahua"}}

while True:
    try: 
        name = input("Type a university name: ")
        print(f"The distance from Colonia to {name} is {universities[name]["distance"]}km")
        break
    except KeyError:
        print("This is not a university, try again")
        pass

response = requests.get("http://universities.hipolabs.com/search?name="+universities[name]["name"])
search = response.json()
for result in search:
    print(result["name"], result["domains"])