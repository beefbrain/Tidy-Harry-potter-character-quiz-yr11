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

for character in ans_set:
#character holds the values in ans_set
  #print(character)
#i am printing to test if characters holds the correct values
  char_score[character] +=1
print (char_score)
#printing to test if the vaules are added up correctly 