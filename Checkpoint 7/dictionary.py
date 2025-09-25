capitals = {
    "Mexico": "Mexico City",    #assing mexico to mexico city
    "Canada": "Ottawa",         #assign to canada to ottawa
    "Brazil": "Brasília",       #assign brazil to brasilia
    # "Canada": "Montreal"      You have to use unique keys
}

capitals["Italy"] = "Rome"      #make a new key (italy) and assign it rome
del capitals["Brazil"]          #delete brazil and its value
capitals.pop("Canada")          #remove canada and its value
#capitals.clear()

print(capitals)                 #print the capitals dictionary

# students = {                    #create a new dictionary
#     "Hermione": "Gryffindor",   #assign hermione to gryffindor
#     "Harry": "Gryffindor",      #assign harry to gryffindor
#     "Ron": "Gryffindor",        #assing ron to gryffindor
#     "Draco": "Slytherin"        #assign draco to slytherin
# }

# for key in students:            #for loop
#     print(f"{key}: {students[key]}")    #print the key and then the value

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for element in students:
    print(f"{element["name"]}, {element["house"]}, {element["patronus"]}")