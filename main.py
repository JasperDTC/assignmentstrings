# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

"""1. Create a variable for every player that scored."""
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

"""2. Create a variable for each minute 
of the match that a goal was scored in"""
goal_0 = 32
goal_1 = 54


"""3. Using the +-operator, create a string that reports on 
who scored when"""
scorers = player_1 + ' ' + str(goal_0) + ', ' + player_2 + ' ' + str(goal_1)
print(scorers)

"""4. Use f-strings or the +-operator to create a single 
string with information about who scored when """
report = player_1 + ' scored in the' + ' ' +  str(goal_0) +'nd minute' + '\n'  + player_2 + ' scored in the' + ' ' + str(goal_1) + 'th minute'

report_1 = f'{player_1} scored in the {goal_0}nd minute {player_2} scored in the {goal_1}th minute'

#PART 2
"""Description: Store the following values in the given variable, and do each of those exercises in a single line of code."""

"""1. Choose a player that played in the soccer match and store his name as a string in the variable player."""
player = 'Ronald Koeman'

"""2. first_name: use slicing and the find-method (help) to isolate and store the player's first name."""
#2a. Using the slicing method
first_name = player[0:6]

#2b(???). Using the find-method
first_name_1 = player.find("Ronald")
print(first_name_1)  
""" De uitkomst hiervan is 0. Het find command kan dus alleen gebruikt worden voor het vinden van de locatie
van een cijfer of letter, en niet voor het opslaan van de speler zijn voornaam. Of is er wel een manier om met find de voornaam op te slaan?""" 

"""3. last_name_len: use find, slicing and len to isolate and store the length of their last name."""

# using find
last_name = player.find("Koeman")
print(last_name)

#using slicing(???) Hier sla ik dus niet de lengte van de achternaam op maar de achternaam zelf. 
#Hoe kun je met slicing de lengte van de achternaam opslaan?
last_name_len = player[-6:]
print(last_name_len)

#using len
last_name_len = len(player[7:])
print(last_name_len)

"""4. name_short: isolate and store the player's name in this format: G. von Examplestein."""
name_short = player[0:1] + '. ' + player[-6:]

"""5. chant: this is what the crowd chants when it looks like your player is going to score a goal 
-- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. 
Make sure the last character of this string is not a space! For our example player:

Gut! Gut! Gut!"""
chant = (first_name + '! ') * 5 + first_name + '!'
print(chant)

#Waarom werkt dit niet? chant_1 = (first_name + '! ') * 6 - ' '
#Waarschijnlijk omdat je niet wat kan aftrekken van een string, maar er wel wat bij op kunt tellen.

""" 6. good_chant: Make super-sure the last character of chant is not a space 
by using the inequality operator (!=). Try this in your REPL for an example: 
print(2 != 3). Also try: print(2 != 2)."""
good_chant = chant [-1] != ' '
print(good_chant)