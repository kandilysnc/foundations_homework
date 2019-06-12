# 1) I have a list called bubblegum. How do I get the first element? The last element?

bubblegum = [1, 2, 3, 4]
bubblegum[0]

bubblegum[3]
bubblegum[len(bubblegum) - 1]

bubblegum[-1]

# 2) What function or method…
# ...tells how many elements are in a list?
len(bubblegum)
# ...replaces text in a string with other text?
name.replace("o", "a")
# ...gives you the keys of a dictionary?
movie.keys()


# 3) What is the output of the following code? Which lines give you errors?

borough_name = 'Manhattan'
z = [ 'Manhattan', 'Queens' ]
x = { 
  'borough_name': 'Manhattan', 
  'population': 500 
}
y = {
  'Manhattan': 500,
  'Queens': 200
}

x.keys()[0] # 'borough_name'
x[x.keys()[0]] # first element


print('borough_name') # borough_name
print(borough_name) # Manhattan
x['borough_name'] # go look for the 'borough_name' in x
x[borough_name] # go look up the variable borough_name. AFter you've found that variable, switch it in. x['Manhattan']. Then go look for the 'Manhattan' key inside of x

print(x['borough_name']) # prints Manhattan
print(x[borough_name]) # Key not found print(x['Manhattan'])
print(x[0])  


print(y['borough_name']) # Key Error!!!
print(y[borough_name]) # y['Manhattan'] -> 500
print(y[0]) # KeyError not found 0


print(z['borough_name']) # Error
print(z[borough_name]) # z['Manhattan'] -> Error
print(z[0]) # 'Manhattan'

# 4)  Print out each art piece’s name. 
art_pieces = [
  { ‘title’: ‘Gold Star’, ‘year’: 1805 }, 
  { ‘title’: ‘Blunderbuss‘, ‘year’: 1800 },
  { ‘title’: ‘Chairlift’, ‘year’: 1976 },
  { ‘title’: ‘Rancor’, ‘year’: 2002 }
]
for art in art_pieces:
  print(art['title'])

names = ['Gold Star', 'Blunderbuss', 'Chairlift', 'Rancor']
for name in names:
  print(name)
print(names)

# LIST COMPREHENSION!!!!!!
# An easy way to just pull out one part of a bunch of dictionaries

# A new list of JUST the names of the art pieces
names = [art['title'] for art in art_pieces]
# ['Gold Star', 'Blunderbuss', 'Chairlift', 'Rancor']

# A new list of JUST the names of art pieces from AFTER 1900
names = [art['title'] for art in art_pieces if art['year'] > 1900]
# ['Chairlift', 'Rancor']

# 5) Given the following, write code to calculate how many murders we have in total.

murders = {
  'Albany': 23,
  'Kings County': 10,
  'Rochester': 7,
  'Yonkers': 9
}
murders['Albany'] + murders['Kings County'] + murders['Rochester'] + murders['Yonkers']

sum(murders.values())

other_murders = [
  { 'name': 'Albany', 'murders': 23 },
  { 'name': 'Kings County', 'murders': 10 },
  { 'name': 'Rochester', 'murders': 7 },
  { 'name': 'Yonkers', 'murders': 9 }
]

murder_count = [other['murders'] for other in other_murders]
sum(murder_count)

