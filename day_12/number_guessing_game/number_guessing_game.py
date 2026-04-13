#1. Print logo
#2. Print welcome and ad
#3.0 Create a while loop with the following instructions for program while to_play == 'yes'
#3.1. Use random to chose one number
#4. ask the player to choose a difficulty and save it in a input, in a variable difficult where vaules could be 'easy' or 'hard'
#5. make a fuction named 'logic' to take a paramether difficulty for 'easy' (10 attemps) and 'hard' level, (5 attemps)
#5.1. Ask a guessing number
#5.1.1 check if guessing number is a int valid value by 'try' if yes, continue with the function  if not except: print The input is not valid, please enter a number. and back to the step 5.1.
#5.2. If guessing number is high print too high and if it is low print too low.
#5.3. Check the remain opportunities according to the level choosen and using an while loop with substraction for a the name of the attemps to ask for another guessing number or end the program as lose.
#5.4. if the number is right. Print Won! and end the program breack while loop and go out the funtion.
#6 Call the 'logic' fiction with the parameter difficulty and chosen random number by program 
#7. Ask if the customer wish to play again and save answer in the variable to_play. if the customer write 'yes' re-start the program to the step 3. so encapsule the program in While loop to_play. if the customer choose 'no' end and exit program.
