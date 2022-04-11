#intro
name = str(input("what's your name? (press enter after writing your name) "))


non_caps = 0 


  
while non_caps ==0:
  if not name.isalpha():
    print("Please enter only alphabetical characters for your name.")
    name = str(input("what's your name? (press enter after writing your name) "))
    non_caps = 0
  if name.isalpha():
    non_caps = 1



    
print("ʕ•́ᴥ•̀ʔっ♡ Hello {}".format(name)) 
print ("welcome to this harry potter quiz ʕ•́ᴥ•̀ʔっ♡ ")
print ("Harry potter is a book series written by auther JK Rowlings.She wrote a total of 7 books but this quiz is based on 6 of them")
print("   ")
print ("          .。･:*:･(✿ ◕ 3 ◕ ) ❤ ( ◕ ε ◕ ✿ )･:*:･。.")
print("   ")
print ("You'll be instructed to press a number that equals your option then press enter right after you entered it, at the end of the quiz, you will find out who your hogwarts best friend or people in your freind group are!")