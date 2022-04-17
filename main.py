#def function for non int error handling 

def int_only():  
  while True:
    try:
      print(" ")
      ans1 = 0
      ans1 = int(input("Enter your option here... \n\n"))
      
      return ans1
      break
    except ValueError:  
        print("\n\nPlease input integer only... \n ****************************")     
        continue
#mathcing dict with chosen list def function(+1)(adding to dict value)
def update_dict(up_dict, cho_set):
  for character in cho_set:
    up_dict[character] +=1
  return up_dict
#mathcing dict with chosen list def function(-1)(taking away from dict value)
def update_dict_n(up_dict, cho_set):
  for character in cho_set:
    up_dict[character] -=1
  return up_dict
#intro
name = str(input("what's your name? (press enter after writing your name) "))
print (" ")

non_caps = 0 
#non apla error handle    
while non_caps ==0:
  if not name.isalpha():
    print ("******************************************************* \n Please enter only alphabetical characters for your name. \n ******************************************************* \n \n ")
    name = str(input("what's your name? (press enter after writing your name) "))
    print(" ")
    
    non_caps = 0
  if name.isalpha():
    non_caps = 1




print(" \n \n ʕ•́ᴥ•̀ʔっ♡ Hello {}".format(name)) 
print ("welcome to this harry potter quiz ʕ•́ᴥ•̀ʔっ♡ \n Harry potter is a book series written by auther JK Rowlings.She wrote a total of 7 books but this quiz is based on 6 of them \n \n .。･:*:･(✿ ◕ 3 ◕ ) ❤ ( ◕ ε ◕ ✿ )･:*:･。. \n \n You'll be instructed to press a number that equals your option then press enter right after you entered it, at the end of the quiz, you will find out who your hogwarts best friend or the people in your freind group are! \n \n ")

input("input anything to continue...")
print(" \n \n \n \n ")

def main():
  #dictionary of all the characters all characters have the same value of 0 so i found a finction that is a short cut for this
  char_score = {}.fromkeys(["Hermioni Granger", "Harry Potter", "Ron Weasley", "Draco Malfoy", "Neville Longbottom", "Luna Lovegood", "Cedric Diggory", "Fred and George Weasley", "Ginny Weasley" ], 0)
  #question 1--------------------------------------------
  print("""----------------------------------------------------\n Q1:⚡🧙 Who would you want to be friends with? ⚡🧙\n--------------------------------------------------- \n Someone who is a bit of a bad influence, breaking rules are part of the fun \n Enter 0 \n  \nSomeone who is a good influence so they can encurage me to stay on track \n Enter 1 \n \nSomeone a bit quiet and down to earth, they are very relaxing to hang out with \n Enter 2 \n \n""")
  
  #calling non int error hadling function
  ans = int_only()
  
  #making sure that input is within option range
  while ans > 2:
    print("That is not an option, try again \n ******************************** \n \n ")
    ans = int_only()
    if ans <=2:
     break
  #sets for chosen option
  bad_boy_girl = {"Harry Potter", "Draco Malfoy", "Ginny Weasley"} 
  gd_influ = {"Hermioni Granger", "Neville Longbottom", "Ginny Weasley"} 
  quiet = {"Neville Longbottom", "Luna Lovegood", "Cedric Diggory"} 
  ans_set = {}
  #mathcing input with mathcing set
  if ans == 0:
      ans_set = bad_boy_girl
  elif ans == 1:
      ans_set = gd_influ
  elif ans == 2:
    ans_set = quiet
  
  # the keys in the the dictionary char_score is the same to the value of all of the sets. i need to use a for loop to link them as the for loop will check the dictionary keys one after the other.
  
  #calling function that matches chosen set and dict
  char_score = update_dict(char_score, ans_set)
  
  #^privious processes are repeated for every question just with diffeerent print statments and different question ranges and sets
  #question 2 _--------------------------------------------
  print("""---------------------------------------------\nQ2:🪄🦌I would like my friends to be...🪄🦌\n---------------------------------------------\n Funny, I love to have a good laugh with my friends \n Enter 0 \n \n Popular, it will improve my social status at hogwarts \n Enter 1 \n \n Bravery, thats how I know they will never be afraid to stad up for me or what is right \n Enter 2 \n \n""")
  
  ans = int_only()
  
  while ans > 2:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=2:
     break
  
  funny ={"Ron Weasley", "Draco Malfoy", "Fred and George Weasley", "Ginny Weasley"}
  popular = {"Harry Potter", "Draco Malfoy", "Cedric Diggory"}
  brave= {"Harry Potter", "Cedric Diggory"}
  ans_set = {}
  
  if ans == 0:
      ans_set = funny
  elif ans == 1:
      ans_set = popular
  elif ans == 2:
    ans_set = brave
  
  char_score = update_dict(char_score, ans_set)
  #question 3------------------------------------
  print("""-----------------------------------------------------------------\nQ3:🪄🐇 Which one of these traits would you like in a friend?🪄🐇\n-----------------------------------------------------------------\n I would like my friend to be positive and brighten things up even when im sad \n Enter 0 \n \n Curagous, I love to do things a little out my comfort zone and it would be nice to have friends to acompany me \n Enter 1 \n \n Inteligence, they can help me get out of tough situations with their wit! and it would be fun to join academic clubs together \n Enter 2 \n \n""")
  
  ans = int_only()
  while ans > 2:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=2:
     break
      
  positivity = {"Luna Lovegood", "Fred and George Weasley"}
  courageous = {"Ron Weasley", "Neville Longbottom"}
  intelligence = { "Hermioni Granger", "Draco Malfoy", "Cedric Diggory", "Ginny Weasley"}
  
  
      
  if ans == 0:
      ans_set = positivity
  elif ans == 1:
      ans_set = courageous
  elif ans == 2:
    ans_set = intelligence
  
  char_score = update_dict(char_score, ans_set)
  
  #question 4-----------------------------------------
  print("--------------------------------------------------------------\n Q4: 🏰🦅 What quality do you think is the most admirable 🏰🦅\n---------------------------------------------------------------\n loyalty, the trust that can be apon them is very reassuring \n Enter 0 \n \n sacraficing, It is so admirable when someone can think of others over themselfs \n Enter 1 \n \n Accepting, people who don't judge people and accept people for who they are \n Enter 2 \n \n kindness, I love it when people think about the little things to help people out \n Enter 3 \n \n helpfulness, these people go out of their way to help with homework, tests, or little things in general \n Enter 4 \n \n")
  
  ans = int_only()
  while ans > 4:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=4:
     break
  
  
  loyal = {"Hermioni Granger", "Harry Potter", "Ron Weasley", "Neville Longbottom", "Luna Lovegood", "Cedric Diggory", "Fred and George Weasley", "Ginny Weasley"}
  sacrifice  = {"Hermioni Granger",   "Harry Potter", "Cedric Diggory"}
  accept = {"Harry Potter", "Luna Lovegood", "Cedric Diggory", "Ginny Weasley"} 
  kind = {"Neville Longbottom", "Cedric Diggory", "Luna Lovegood"}
  helpful = {"Hermioni Granger", "Neville Longbottom", "Cedric Diggory", "Ginny Weasley"}
  
  if ans == 0:
      ans_set = loyal
  elif ans == 1:
      ans_set = sacrifice
  elif ans == 2:
    ans_set = accept
  elif ans == 3:
    ans_set = kind
  elif ans == 4:
    ans_set = helpful
    
  char_score = update_dict(char_score, ans_set)
  
  
  
  print("-------------------------------------\n🪄⚗️ Pick a hogwarts subject 🪄⚗️\n------------------------------------\n Defence against the dark arts \n Enter 0 \n \n Herbology \n Enter 1 \n \n Care of magical creatures \n Enter 2 \n \n Flying class \n Enter 3 \n \n Arithmatics (wizerding mathmatics) \n Enter 4 \n \n Magical Charms and spells \n Enter 5 \n \n ")
  
  ans = int_only()
  while ans > 5:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=5:
     break
  
  def_dark_art = {"Ron Weasley", "Harry Potter", "Draco Malfoy"}
  herb = {"Neville Longbottom", "Fred and George Weasley"}
  care_magic_cre = {"Luna Lovegood"}
  fly_class= {"Ginny Weasley", "Cedric Diggory", "Fred and George Weasley"}
  arith = {"Hermioni Granger", "Harry Potter", "Draco Malfoy"}
  charms = {"Cedric Diggory"}
  
  if ans == 0:
      ans_set = def_dark_art
  elif ans == 1:
      ans_set = herb
  elif ans == 2:
    ans_set = care_magic_cre
  elif ans == 3:
    ans_set = fly_class
  elif ans == 4:
    ans_set = arith
  elif ans_set == 5:
    ans_set = charms
  
  char_score = update_dict(char_score, ans_set)
  
  
  #Question 6---------------------------------------
  print("---------------------------------\nQ6: 💛🏆 What is your hobby? 💛🏆\n---------------------------------\n Playing physical Sports\n Enter 0\n \n Playing video or board games\n Enter 1\n \n Painting, drawing or art in general\n Enter 2\n \n Reading books or comics \n Enter 3\n \n Cooking \n Enter 4 \n \n Gardening \n Enter 5 \n \n Making jokes, memes or funny tiktoks \n Enter 6 \n \n ")
  
  
  ans = int_only()
  
    
  while ans > 6:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=6:
     break
      
  play_sport = {"Ginny Weasley", "Cedric Diggory", "Fred and George Weasley", "Harry Potter", "Draco Malfoy"}
  vid_brd_game = {"Ron Weasley"} 
  art = {"Luna Lovegood"}
  reading = {"Hermioni Granger"}
  cooking = {"Neville Longbottom"}
  gardening = {"Neville Longbottom", "Luna Lovegood"}
  joke_memes = {"Fred and George Weasley"}
  
  if ans == 0:
      ans_set = play_sport
  elif ans == 1:
      ans_set = vid_brd_game
  elif ans == 2:
    ans_set = art
  elif ans == 3:
    ans_set = reading
  elif ans == 4:
    ans_set = cooking
  elif ans_set == 5:
    ans_set = gardening
  elif ans_set == 6:
    ans_set = joke_memes
  
  char_score = update_dict(char_score, ans_set)
#Question 7---------------------------------------
  print("-----------------------------------------------\nQ7: 💙🍺How are you spending your weekend? 💙🍺\n-----------------------------------------------\n Reading a good book or comics\n Enter 0\n \n Something by myself, I enjoy my alone time\n Enter 1\n \n Binge watching a series or movies \n Enter 2\n \n plan something with my friends \n Enter 3 \n \n Doing something with family \n Enter 4 \n \n")
  ans = int_only()
  
    
  while ans > 4:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=4:
     break
      
  read_book = {"Hermioni Granger",  "Neville Longbottom"}
  myself = {"Luna Lovegood"}
  binge = {"Ron Weasley"}
  friends = {"Harry Potter", "Cedric Diggory"}
  family = {"Ginny Weasley", "Fred and George Weasley", "Draco Malfoy"}
  
  if ans == 0:
      ans_set = read_book
  elif ans == 1:
      ans_set = myself
  elif ans == 2:
    ans_set = binge
  elif ans == 3:
    ans_set = friends
  elif ans == 4:
    ans_set = family
  
  
  char_score = update_dict(char_score, ans_set)
  #Question 8---------------------------------------
  print("---------------------------------------------------------------------\nQ8: 😤 what is an annoying trait you cannot tollerate in a person? 😤\n---------------------------------------------------------------------\n Oversensitivity, I can never make any jokes around them as they are always offended\n Enter 0\n \n Insensitivity, they never realise when they've crossed the line \n Enter 1 \n \n Arrogence, They always think their better than everyone else, its so annoying \n Enter 2 \n \n When they're oppinionated, they always think they are right and are not willing to cosider other opinions \n Enter 3 \n \n They do not think before they do things, Like they screw up so bad which easily could have need avoided if they just used their heads!\n Enter 4 \n \n Pessimistic, their negativity does not make me feel any better in tough situations, like would it hurt to be a little positive? \n Enter 5 \n \n Impatience, they get mad so easily \n Enter 6")
  ans = int_only()
  
    
  while ans > 6:
    print("That is not an option, try again")
    print("********************************")
    print(" ")
    ans = int_only()
    if ans <=6:
     break
  oversensitive = {"Neville Longbottom"}
  insensitive = {"Hermioni Granger", "Ron Weasley", "Luna Lovegood", "Fred and George Weasley", "Draco Malfoy"}
  arrogant = {"Ron Weasley",  "Draco Malfoy"}
  opinionated = {"Hermioni Granger", "Harry Potter", "Luna Lovegood", "Ginny Weasley"}
  before_think = {"Harry Potter", "Fred and George Weasley", "Ron Weasley", "Cedric Diggory"} 
  pessimist = {"Draco Malfoy", "Ron Weasley"}
  impatient = {"Hermioni Granger", "Ginny Weasley"}
  
  if ans == 0:
      ans_set = oversensitive
  elif ans == 1:
      ans_set = insensitive
  elif ans == 2:
    ans_set = arrogant
  elif ans == 3:
    ans_set = opinionated
  elif ans == 4:
    ans_set = before_think
  elif ans_set == 5:
    ans_set = pessimist
  elif ans_set == 6:
    ans_set = impatient
  
  char_score = update_dict_n(char_score, ans_set)
  #Question 9---------------------------------------
  
  print("------------------------------------------------------------------\nQ9:🌸💛 What is an annoying trait you don't mind in a person? 🌸💛\n------------------------------------------------------------------\n Oversensitivity\n Enter 0\n \n Insensitivity \n Enter 1 \n \n Arrogence \n Enter 2 \n \n When they're oppinionated \n Enter 3 \n \n They do not think before they do things \n Enter 4 \n \n Pessimistic \n Enter 5 \n \n Impatience \n Enter 6 \n \n ")
  ans = int_only()
  
    
  while ans > 6:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=6:
     break
      
  oversensitive = {"Neville Longbottom"}
  insensitive = {"Hermioni Granger", "Ron Weasley", "Luna Lovegood", "Fred and George Weasley", "Draco Malfoy"}
  arrogant = {"Ron Weasley",  "Draco Malfoy"}
  opinionated = {"Hermioni Granger", "Harry Potter", "Luna Lovegood", "Ginny Weasley"}
  before_think = {"Harry Potter", "Fred and George Weasley", "Ron Weasley", "Cedric Diggory"} 
  pessimist = {"Draco Malfoy", "Ron Weasley"}
  impatient = {"Hermioni Granger", "Ginny Weasley"}
  
  if ans == 0:
      ans_set = oversensitive
  elif ans == 1:
      ans_set = insensitive
  elif ans == 2:
    ans_set = arrogant
  elif ans == 3:
    ans_set = opinionated
  elif ans == 4:
    ans_set = before_think
  elif ans_set == 5:
    ans_set = pessimist
  elif ans_set == 6:
    ans_set = impatient
  
  char_score = update_dict(char_score, ans_set)
  
  #Question 10--------------------------------------
  print("---------------------------------------------------------\nQ10: 🪄🐕Would you rather have a friend who is very…🪄🐕\n---------------------------------------------------------\n Boring\n Enter 0\n \n Odd \n Enter 1 \n \n")
  
  ans = int_only()
  
    
  while ans > 1:
    print("That is not an option, try again \n ******************************** \n")
    ans = int_only()
    if ans <=1:
     break
  
  boring = {"Neville Longbottom"} 
  odd = {"Luna Lovegood"} 
  
  if ans == 0:
    ans_set = boring
  elif ans == 1:
    ans_set = odd
  
  
  char_score = update_dict(char_score, ans_set)
  
  #print (char_score)
  #printing to test if the vaules are added up correctly 
  
  #I need to order the dictionary from largest to smallest and i found a format for that.
  
  #I need to order the dictionary from largest to smallest and i found a format for that.
  
  sort_char_score = sorted(char_score.items(), key=lambda x: x[1], reverse=True)
  
  
  
  i = 0
  #the value of i will increase by one every loop thus will check the first key would become the next key and the next key would become the key after next key
  # i will be the amount of ties, the value of i changes 
  while i < len(sort_char_score)-2:
    first_key = list(sort_char_score)[i] 
    next_key = list(sort_char_score)[i+1]
  #print (first_key) <--- printing to see if expected
  #print (next_key)<---- to see of expected
    #^this goes on until there are no ties, if there are no ties, the loop     will be broken
    if first_key[1] == next_key[1]:
      i +=1
      
    else:
      break
    
      
  #I print the results here
  #print (i)
  #I need to print the key of the sorted dictionary up to 'i' place holder 
  # i will be using a for loop for this
  
  
  for j in range(i+1):
    first_key = list(sort_char_score)[j] 
  #i am only printing the keys
    print (first_key [0],  end = '')
    print (",",  end = ' ')
  
  if i == 0:
    print("is your hogwarts best friend, you guys have so much in common!")
  else:
    print(" and you would make a wonderful friend group at Hogwarts, you all have so much in common!  ")
    
  print ("\n \n \n \n Press 0 to play again or any other number to finish...")
  ans = int_only()
  if ans == 0:
    print('\n \n \n \n \n \n ')
    main()
  else:
    print('\n \n \n \n ')
    print("I hope you enjoyed this quiz young wizrad!")
    exit()
#this is where the body of my quiz starts
main()