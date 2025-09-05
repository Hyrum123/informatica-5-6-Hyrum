independence_stages = ["Inicio", "Organización", "Resistencia", "Consumación"]
print(independence_stages[0])
print(len(independence_stages))

#list methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages)
leaders.insert(1, "José María Morelos y Pavón")
#leaders.remove("Vicente Guerrero")
leaders.append("Agustín de Iturbide")
#leaders.pop(1)
#leaders.clear()
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#leaders.sort()
#leaders.reverse()
new_leaders = leaders.copy()

print(new_leaders)
print(leaders)