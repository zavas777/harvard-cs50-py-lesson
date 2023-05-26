# list of dicts:

people = [
    { "name": "Bruce", "branch": "Kung Fu" },
    { "name": "Roy", "branch": "Shooting"},
    { "name": "Rob", "branch": "JyuJutsu"}
]

# def f(individual):
#    return individual["name"] # or individual["branch"]

# people.sort(key=f)

# lambda input: output
people.sort(key=lambda individual: individual["name"])

print(people)




