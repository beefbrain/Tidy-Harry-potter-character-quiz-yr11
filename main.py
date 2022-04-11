#def function for non int error handling 
def int_only():  
  while True:
    try:
      print(" ")
      ans1 = 0
      ans1 = int(input("Enter your option here..."))
      print(" ")
      return ans1
      break
    except ValueError:  
        print ("")
        print("Please input integer only...") 
        print("****************************")     
        continue
def update_dict(up_dict, cho_set):
  for character in cho_set:
    up_dict[character] +=1
  return up_dict
#dictionary of all the characters all characters have the same value of 0 so i found a finction that is a short cut for this
char_score = {}.fromkeys(["Hermioni Granger", "Harry Potter", "Ron Weasley", "Draco Malfoy", "Neville Longbottom", "Luna Lovegood", "Cedric Diggory", "Fred and George Weasley", "Ginny Weasley" ], 0)

print ("Who would you want to be friends with?")
print ("--------------------------------------")
print ("someone who is a bit of a bad influence, breaking rules are part of the fun")
print ("Enter 0")
print ("Someone who is a good influence so they can encurage me to stay on track")
print ("Enter 1")
print ("Someone a bit quiet and down to earth, they are very relaxing to hang out with")
print ("Enter 2")
#what id id to make this work was made my while and if statememnt more specific and added the input in the loop which i didn't do before.


ans = int_only()

  
while ans > 2:
  print("That is not an option, try again")
  print("********************************")
  print(" ")
  ans = int_only()
  if ans <=2:
   break
  
bad_boy_girl = {"Harry Potter", "Draco Malfoy", "Ginny Weasley"} 
gd_influ = {"Hermioni Granger", "Neville Longbottom", "Ginny Weasley"} 
quiet = {"Neville Longbottom", "Luna Lovegood", "Cedric Diggory"} 
ans_set = {}

if ans == 0:
    ans_set = bad_boy_girl
elif ans == 1:
    ans_set = gd_influ
elif ans == 2:
  ans_set = quiet

# the keys in the the dictionary char_score is the same to the value of all of the sets. i need to use a for loop to link them as the for loop will check the dictionary keys one after the other.

char_score = update_dict(char_score, ans_set)

#print (char_score)
#printing to test if the vaules are added up correctly 

#I need to order the dictionary from largest to smallest and i found a format for that.

#I need to order the dictionary from largest to smallest and i found a format for that.

sort_char_score = sorted(char_score.items(), key=lambda x: x[1], reverse=True)

i = 0
#the value of i will increase by one every loop thus will check the first key would become the next key and the next key would become the key after next key
# i will be the amount of ties, the value of i chanches 
while i < len(sort_char_score) - 2:
  first_key = list(sort_char_score)[i] 
  next_key = list(sort_char_score)[i+1]
  #print (first_key)
  #print (next_key)
  #^this goes on until there are no ties, if there are no ties, the loop     will be broken
  if first_key[1] == next_key[1]:
    i +=1
    
  else:
    break
  
    
#I print the results here
#print (i)
#I need to print the key of the sorted dictionary up to 'i' place holder 
# i will be using a for loop for this


for j in range(i):
  first_key = list(sort_char_score)[j] 
#i am only printing the keys
  print (first_key [0],  end = '')
  print (",",  end = ' ')

if i == 0:
  print("is your hogwarts best friend, you guys have so much in common!")
else:
  print(" and you would make a wonderful friend group at Hogwarts, you all have so much in common!")