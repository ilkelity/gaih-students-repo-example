# This is a competition program

print("here is a quiz consist of 10 questions! remember all answers are case sensitive, please answer in upper case!")
print("good luck :)")
score = int(0)
newscore: int
newscore2: int
newscore3: int
newscore4: int
newscore5: int
newscore6: int
newscore7: int
newscore8: int
newscore9: int
newscore10: int
totalscore: int
question = input("WHAT IS THE CAPITOL OF TURKEY?, please answer in uppercase!")
if question == "ankara".upper():
    print("correct!")
    newscore = 10
elif question== "ankara".lower():
    print("uppercase please")
else:
    print("not correct")
    newscore = 0
question2 = input("WHICH INTERNAL ORGAN IS THE CENTRE OF THE NERVOUS SYSTEM AND LOCATED IN THE SKULLS?")
if question2 == "brain".upper():
    print("correct")
    newscore2 = 10
elif question2== "brain".lower():
    print("uppercase please")
    newscore2 = 0
else:
    print("that's wrong")
    newscore2 = 0
question3 = input("WHAT IS THE INTERNAL ORGAN NAME THAT PUMPS BLOOD THROUGH THE BLOOD VESSELS "
                  "BY REPEATED RHYTHMIC CONTRACTIONS? ")
if question3 == "heart".upper():
    print("correct!")
    newscore3 = 10
elif question3 == "heart".lower():
    print("please use uppercase characters!")
    newscore3 = 0
else:
    print("that is not true")
    newscore3 = 0
question4 = input("ARE YOU ALIVE? YES OR NO? ")
if question4 == "yes".upper():
    print("yes, correct1")
    newscore4 = 10
elif question4 == "yes".lower():
    print("not in lowercase characters!")
    newscore4 = 0
else:
    print('NO,You are alive!')
    newscore4 = 0
question5 = input("WHAT IS LARGEST COUNTRY IN THE WORLD")
if question5 == "russia".upper():
    print("you are right")
    newscore5 = 10
elif question5 == "russia".lower():
    print("not in lowercase!")
    newscore5 = 0

else:
    print("that is wrong")
    newscore5 = 0

question6 = input("WHAT IS THE BIGGEST PLANET IN OUR SOLAR SYSTEM?")
if question6 == "Jupiter".upper():
    print("you are right")
    newscore6 = 10
elif question6 == "jupiter".lower():
    newscore6 = 0
else:
    print("your answer is wrong")
    newscore6 = 0

question7 = input("IN TURKEY, WHAT IS THE MOST POPULOUS CITY?")
if question7 == "istanbul".upper():
    print("you are correct")
    newscore7 = 10
elif question7 == "istanbul".lower():
    print("use uppercase characters!")
    newscore7 = 0
else:
    print("that is wrong")
    newscore7 = 0

question8 = input("What's the highest mountain in the world")
if question8 == "Everest".upper():
    print("that's right")
    newscore8 = 10
elif question8 == "everest".lower():
    print("not in lowercase")
    newscore8 = 0
else:
    print("no, that is not true")
    newscore8 = 0
question9 = input("Who did Johnny Depp play in Pirates Of The Caribbean?")
if question9 == "jack sparrow".upper():
    print("you are right")
    newscore9 = 10
elif question9 =="jack sparrow".lower():
    print("please use uppercase characters")
    newscore9 = 0
else:
    print("you are wrong")
    newscore9 = 0

question10 = input("What element does 'O' represent on the periodic table?")
if question10 == "Oxygen".upper():
    print("that's true!")
    newscore10 = 10
elif question10 == "oxygen".lower():
    print("not in lowercase :(")
    newscore10 = 0
else:
    print("that is wrong")
    newscore10 = 0

totalscore = newscore+newscore2+newscore3+newscore4+newscore5+newscore6+newscore7+newscore8+newscore9+newscore10
if totalscore<50:
    print("sadly your score is:", totalscore, "you are unsuccessful :(")
elif totalscore>=50:
    print("well done, your score is:", totalscore, 'you are succeed :)')

