#Add logo from the Art.py file and print it 
# Create a variable called score = 0
# while play_game = True 
# get into in all in a main function:
 # keep playing with a while loop, 
  #Print 'Compare A:' 
  #radon 1 a = random.randint(0, (len(data)-1))
  #radon 2 b = random.randint(0, (len(data)-1))
  #From game_data.py file, chose a ramdon dictionary from the list called 'data', dictionary_a = data[a]. then from the dictionary_a choosen, print name eg. print(dictionary_a["name"], a 'description' and 'country'
  #save dictionary_a["follower_number"] on a variable calle a_followers. 
  # print 'VS' logo
  #Print 'Against B:'
  #From game_data.py file, chose another ramdon dictionary from the list called 'data', then from the dictionary choose and print name, a 'description' and 'country'
  #Safe followers amount on B_followers
  #Create a variable called the_highest

  # Make a conditional if A_followers > B_followers so, the_highest = dictinary of data choosen on printed on A option, else the_highest = dictinary of data choosen on printed on B option
  # Then try to print the imput "Who has more followers? Type 'A' or 'B':", save it in 'guessing' variable and save guessing.lower() in a new variable called 'guessing_highest' .
  # Compare the_highest.followers == guessing_highest -> take the followers amount into dictionary positon, that is into the list into the data file. 

  # If the previous condition is true, first score += 1, then delete full the previos print. We can use   import os
    # def clear_screen():
    #     os.system('cls' if os.name == 'nt' else 'clear')
    # After logo clear_screen() and print 'You're right! Current score: {score}'
    # print in the console and display the game again however fist create  print Score and add it 1 point,
    # and the right answer chosen, woud be the new A value, that is a index on the list, so count their position on the list, to do this use list.index() and apply random without this item element. 
   # To this last previous step filter the list first using a list comprehension, then pass the filtered list to random.choice(), like this filtered_list = [item for item in my_list if item != exclude_value]
   #  So save the right answer items in a.
  # however If the answer is wrong, it's guessing is not equal to the_highest finish the program, pay_game = False and print 'Sorry, that's wrong. Final score: {score}'
#  Gameover.
