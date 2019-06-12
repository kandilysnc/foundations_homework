
# PART ONE: Lists

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48

numbers = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list.
# Display the 4th element of this list.
# Display the sum of the 2nd and 4th element of the list.
# Display the 2nd-largest value in the list.
# Display the last element of the original unsorted list

# !!!!!
# Display the sum of all of the numbers divided by two.
sum(numbers) / 2

# !!!!!
# Print whether the median or the mean of the numbers is higher
import statistics
statistics.mean(numbers)
statistics.median(numbers)

# PART ONE: Dictionaries

# 1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
  'title': '10 Things I Hate About You',
  'year': 1999,
  'director': ' Gil Junger'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# 2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

population = {
  'Manhattan': 1.6,
  'Brooklyn': 2.6,
  'Bronx': 1.4,
  'Queens': 2.3,
  'Staten Island': 0.470
}

# 5) Display the population of Brooklyn.

# 6) Display the combined population of all five boroughs.

# 7) Display what percent of NYC's population lives in Manhattan.

# PART TWO: Lists

countries = ["Ghana", "Peru", "Austria", "Korea", "Australia", "Mexico", "Italy"]

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

# !!!!!
# 2) Using a for loop, print each element of the list
for country in countries:
  print(country)

# !!!!!
# 3) Sort the list permanently.
# Sort the countries, then save it back into the variable
countries = sorted(countries)
countries.sort() # Permanently sort


len(countries)

# 4) Display the first element of the list.
# 5) Display the second-to-last element of the list.
# 6) Delete one of the countries from the list using its name.

# !!!!!!
# 7) Using a for loop, print each country's name in all caps.
name = "Soma"
name.upper()

for country in countries:
  print(country.upper())

# PART TWO: Dictionaries

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
  'name': 'Angel Oak',
  'species': 'Southern live oak',
  'age': 450,
  'location_name': 'Charleston, SC',
  'latitude': 32,
  'longitude': -80
}
tree['name']
tree['age']

# !!!!!!
# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree['name'] + ' is a ' + str(tree['age']) + ' year old tree...')
print(tree['name'], 'is a', tree['age'], 'year old tree...')
print(f"{tree['name']} is a {tree['age']} year old tree...")
print("{name} is a {age} year old tree".format(**tree))

# DOES WORK
"{name} is a {age} year old tree".format(name='Soma', age=100)
# DOES NOT WORK
"{name} is a {age} year old tree".format({'name': 'Soma', 'age': '100'})

"{name} is a {age} year old tree".format(
  name=tree['name'],
  age=tree['age']
)


# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

# PART THREE: Lists of dictionaries

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

places = [{
  'name': 'Moscow',
  'latitude': 55.7558,
  'longitude': 37.6173
}, {
  'name': 'Tehran',
  'latitude': 35.6892,
  'longitude': 51.3890
}, {
  'name': 'Falkland Islands',
  'latitude': -51.7963,
  'longitude': -59.5236
}, {
  'name': 'Seoul',
  'latitude': 37.5665,
  'longitude': 126.9780
}, {
  'name': 'Santiago',
  'latitude': -33.4489,
  'longitude': -70.6693
}]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
