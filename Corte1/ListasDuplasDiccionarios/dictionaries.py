names = ['Jenny','Alex','Juan','Samuel','Manin']
heights = [1.61,1.70,1.67,1.80,1.64]

students = {key:value for key,value in zip(names,heights)}

print (students)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 50]

plays = {key:value for key,value in zip(songs,playcounts)}
print(plays)

plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)