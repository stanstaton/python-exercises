state_capitals = {
  "Alaska" : "Juneau",
  "Alabama": "Montgomery",
  "Arizona": "Phoenix",
  "Arkansas": "Little Rock",
  "California": "Sacramento",
  "Colorado" : "Denver",
  "Connecticut": "Hartford",
  "Delaware": "Dover",
  "Florida": "Tallahassee",
  "Georgia": "Atlanta",
  "Hawaii": "Honolulu",
  "Idaho": "Boise",
  "Illinois": "Springfield",
  "Indiana": "Indianapolis",
  "Iowa": "Des Moines",
  "Kansas": "Topeka",
  "Kentucky": "Frankfurt",
  "Maine": "Augusta",
  "Maryland": "Annapolis",
  "Massachusetts": "Boston",
  "Michigan": "Lansing",
  "Mississippi": "Jackson",
  "Missouri": "Jefferson City",
  "Minnesota": "St. Paul",
  "Montana": "Helena",
  "Nebraska": "Lincoln",
  "Nevada": "Carson City",
  "New Hampshire": "Concord",
  "New Jersey": "Trenton",
  "New Mexico": "Santa Fe",
  "New York": "Albany",
  "North Carolina": "Raleigh",
  "North Dakota": "Bismarck",
  "Oklahoma": "Oklahoma City",
  "Ohio": "Columbus",
  "Oregon" : "Salem",
  "Pennsylvania": "Harrisburgh",
  "Rhode Island": "Providence",
  "South Carolina": "Columbia",
  "South Dakota": "Pierre",
  "Tennessee": "Nashville",
  "Texas" : "Austin",
  "Utah": "Salt Lake City",
  "Vermont": "Montpelier",
  "Virgina": "Richmond",
  "Washington": "Olympia",
  "West Virginia": "Charleston",
  "Wisconsin": "Madison",
  "Wyoming": "Cheyenne"
}

def lookup_capital(state):
  for keystate, capital in state_capitals.items():
    # print (key)
    if state == keystate:
      print(capital)
      return capital
  print('Did not find the capital you were looking for')

  def lookup_capital2(state):
    if state in state_capitals:
      return f"{state_capitals[state]}, {state}"
  # Lookup state in the state_capitals dict above
  # Fail gracefully if you get a bad state value
  # Return the state and capital formatted as:
  # "Capital, State"
  # Bonus: Make it case-insensitive!

def reverse_lookup(capital):
  for state, keycapital in state_capitals.items():
    # print (key)
    if capital == keycapital:
      print(state)
      return state
  print('Did not find the capital you were looking for')


def reverse_lookup2(capital):
  for state, cap in state_capitals.items():
    if cap == capital:
      return f"{cap} is the capital of {state}."
  return f"Ooops, {capital} was not found!"
  # Find the capitol from the state_capitals dict
  # Return the state and capital formatted as:
  # "Capital, State"
  # Bonus: Make it case-insensitive!

# BONUS: 
# Find how many states and capitals start with a given letter
def starts_with(letter):
  state_dict = []
  capital_dict = []
  for key in state_capitals:
    statefirstletter = key[:1]
    capitalfirstletter = state_capitals[key][:1]

    if letter == statefirstletter:
      print(key)
      state_dict.append(key)
      
    if letter == capitalfirstletter:
      print(state_capitals[key])
      capital_dict.append(state_capitals[key])
     

  print(capital_dict, state_dict)


def starts_with2(letter):
  state_count = 0
  capital_count = 0

  for state, cap in state_capitals.items():
    if state.startswith(letter):
      state_count += 1
    if cap.startswith(letter):
      capital_count += 1
  return f"{state_count} states and {capital_count} capitals start with the letter {letter}"
  # Loop through the above dictionary
  # Count capitals and states letter separately
  # Return a formatted string:
  # "X states and Y capitals begin with the letter Z"
  # Where X and Y are numbers and Z is a single letter char

lookup_capital("Mississippi")
reverse_lookup("Denver")
starts_with2("M")


def choose_a_state():
  state=input("Please enter a state: ")
  lookup_capital(state)

def choose_a_capital():
  capital=input("Please enter a capital: ")
  reverse_lookup(capital)

def choose_a_letter():
  letter =input("Please enter a letter: ")
  starts_with(letter)


choose_a_state()
choose_a_capital()
choose_a_letter()

