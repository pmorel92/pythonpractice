states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville',
}

cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

print("-" * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print("-" * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print("-" * 10)
for state, abbrev, in list(states.items()):
    print("{} is abbreviated {}".format(state, abbrev))

print("-" * 10)
for abbrev, city in list(cities.items()):
    print("{} has the city {}".format(abbrev, city))

print("-" * 10)
for state, abbrev in list(states.items()):
    print("{} state is abbreviated {}".format(state, abbrev))
    print("and has the city {}".format(cities[abbrev]))
print("-" * 10)

state = states.get('Texas')

if not state:
    print("Sorry no Texas")

city = cities.get('TX', 'Does not Exist')
print("The city for the state 'TX' is: {}".format(city))
