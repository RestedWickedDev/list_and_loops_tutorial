songs = ["ROCKSTAR", "Do it", "For The Night"]
print(songs[0])
print(songs[-1])
print(songs[1:3])
songs[2] ="Action Movie Hero Boy"
print(songs)
songs.extend(["On This Rock", "Black Swan (Ft.Dan Avidan)", "Only The Best"])
songs.pop(1)

animals = ["Dog", "Octopus", "Spider"]
animals.append("Crab")
print(animals[2])
animals.pop(0)

for animal in animals:
    print(animal)