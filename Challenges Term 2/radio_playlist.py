weekly_playlist = ["Blinding Lights", "Levitating", "As it was", "Heat Waves", "Good 4 u"]

weekly_playlist.append("Driver's license")
weekly_playlist.insert(1, "Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")
print(weekly_playlist.index("Levitating"))
print(weekly_playlist.count("As it was"))
weekly_playlist.reverse()
print(weekly_playlist)
weekly_playlist.sort()
print(weekly_playlist)
print(weekly_playlist)
print(len(weekly_playlist))

#challenge
i = 1
while i <= len(weekly_playlist):
    first = weekly_playlist[0]
    weekly_playlist.append(first)
    weekly_playlist.pop(0)
    print(weekly_playlist)
    i += 1