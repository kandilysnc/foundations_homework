# https://swapi.co/api/people/1/

person = {
    "name": "Luke Skywalker", 
    "height": "172", 
    "mass": "77", 
    "hair_color": "blond", 
    "skin_color": "fair", 
    "eye_color": "blue", 
    "birth_year": "19BBY", 
    "gender": "male", 
    "homeworld": "https://swapi.co/api/planets/1/", 
    "films": [
        "https://swapi.co/api/films/2/", 
        "https://swapi.co/api/films/6/", 
        "https://swapi.co/api/films/3/", 
        "https://swapi.co/api/films/1/", 
        "https://swapi.co/api/films/7/"
    ], 
    "species": [
        "https://swapi.co/api/species/1/"
    ], 
    "vehicles": [
        "https://swapi.co/api/vehicles/14/", 
        "https://swapi.co/api/vehicles/30/"
    ], 
    "starships": [
        "https://swapi.co/api/starships/12/", 
        "https://swapi.co/api/starships/22/"
    ], 
    "created": "2014-12-09T13:50:51.644000Z", 
    "edited": "2014-12-20T21:17:56.891000Z", 
    "url": "https://swapi.co/api/people/1/"
}

print(person['name'])

# To install requests:
# pip - pip installs packages

# Say "we want to use the requests library"
# Please go download that web page and print it out
import requests

response = requests.get('https://swapi.co/api/people/1/')
print(response)

print(response.text)
# JSON - JavaScript Object Notation

# Convert the JSON into a dictionary
# The JSON looks just like a dictionary
# but it's actually text! So response.json()
# converts it into actually being a dictionary
data = response.json()

print(data)
print(data['name'])

print(data.keys())
print(data['films'])

# /api/people/123234234
# /api/films/209302933


# Use Python to visit this URL
# convert the json to something Python can understand
# and print out the name of that film
# https://swapi.co/api/films/2/

# Use requests to download the URL
response = requests.get('https://swapi.co/api/films/2/')
# Use response.json() to convert the JSON into something Python knows
film = response.json()

# Look at the keys - what's in there?
print(film.keys())
# Okay, we want the title
print(film['title'])




response = requests.get('https://swapi.co/api/people/1/')
person = response.json()
print("Looking at the person", person['name'])
print(person['films'])

for film_url in person['films']:
  print(film_url)
  print("Requesting the data from", film_url)
  response = requests.get(film_url)
  film = response.json()
  print(film['title'])

# pip install jupyter
# jupyter