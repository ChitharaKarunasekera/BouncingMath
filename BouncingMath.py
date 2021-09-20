# ============Main Code=============
# Import packages quick game
import QuickGame.GetInput
import CustomGame.Easy
import CustomGame.Medium
import CustomGame.Hard
import Database.gamedb
import Database.createdb
import sys

# Creating variables
begin = ''
num1 = 0
opp = ''
num2 = 0
count = 0
ans = 0

# begin = str(sys.argv[1])

# Checking the existence of the database
ex = Database.createdb.bdexist()
if ex == 0:
    # Function to create databse
    Database.createdb.createdb()

elif ex == 1:
    pass
else:
    print("Opps!! something is wrong with your xamp connection")

# Checking the existence of tables
extbl = Database.createdb.tblexist()
if extbl == 0:
    # Function to create table
    Database.createdb.createtbl()
    Database.createdb.alttbl()
elif extbl == 1:
    pass
else:
    print("Opps!! something is wring with your xamp connection")

if sys.argv[1] == "play":
    while True:

        # Display Selection menue
        print("==========Game Menu==========")
        print("1 - Quick game")
        print("2 - Custom game")
        print("3 - View  past game details")
        print("4 - Exit")
        print("-----------------------------\n")
        choice = input("Enter your option: ")
        print("\n")
        if choice == '4':
            print("Game Over")
            break

        elif choice == '1':
            # ============Quick game==========
            name = QuickGame.GetInput.getname()

            # Calling function to display questions
            QuickGame.GetInput.questions()
            print("=============Game Results=========")
            print("Your name is", name)
            print("You played with Quick game play mode.")
            print("You answered 10 questions")
            print("\n", end="")

            # Calling function to display player performance information
            QuickGame.GetInput.info()
            print("\n", end="")

            # Calling finction to display score
            print("Correct answers: ", QuickGame.GetInput.score())
            print("Score as percentage: ", QuickGame.GetInput.perc(), "%")
            print("\n", end="")

        elif choice == '2':
            # ===========Custom game==========

            # Levels
            print("\n", end=" ")
            print("******Difficulty Levels******")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("\n", end="")

            # Level Selection
            level = input("Select Level: ")
            print("\n", end="")
            # -------------------Level Easy--------------
            if level == '1':
                lev = "Easy"

                # Getting name and no.of Questions
                name, num = CustomGame.Easy.details()

                # Calling function to display questions
                CustomGame.Easy.questions()

                # Function to display player performance
                print("============Game Results=========")
                print("Your name is", name)
                print("You played with Easy mode.")
                print("You answered ", num, "questions")
                print("\n", end="")
                CustomGame.Easy.performance()

                # Calling function to calculate correct answes
                score = CustomGame.Easy.score()
                print("No.of Correct answers: ", score)

                # Calling function to calculate percentage
                perc = CustomGame.Easy.percScore()
                print("Percentage score ", perc, "%")
                print("\n", end="")

                # Geting current date and time
                time, date = CustomGame.Easy.clock()
                print("Time : ", time)
                print("Date : ", date)
                print("\n", end="")

                # Database connection
                Database.gamedb.connect()

                # Inserting values to database
                Database.gamedb.insert(name, num, score, perc, lev, time, date)


            # -------------------Level Medium--------------
            elif level == '2':
                lev = "Medium"

                # Getting name and no.of Questions
                name, num = CustomGame.Medium.details()

                # Calling function to display qestions
                CustomGame.Medium.questions()

                # Function to display player performance
                print("Your name is", name)
                print("You played with Medium mode.")
                print("You answered ", num, "questions")
                print("\n", end="")
                CustomGame.Medium.performance()

                # Calling function to calculate score
                score = CustomGame.Medium.score()
                print("No.of Correct answers: ", score)

                # Calling function to calculate percentage
                perc = CustomGame.Medium.percScore()
                print("Percentage score: ", perc, "%")
                print("\n", end="")

                # Geting current date and time
                time, date = CustomGame.Medium.clock()
                print("Time : ", time)
                print("Date : ", date)
                print("\n", end="")

                # Database connection
                Database.gamedb.connect()

                # Inserting values to database
                Database.gamedb.insert(name, num, score, perc, lev, time, date)

            # -------------------Level Medium--------------
            elif (level == '3'):
                lev = "Hard"
                # Getting name and no.of Questions
                name, num = CustomGame.Hard.details()

                ##Calling function to display qestions
                CustomGame.Hard.questions()

                # Function to display player performance
                print("Your name is", name)
                print("You played with Hard mode.")
                print("You answered ", num, "questions")
                print("\n", end="")
                CustomGame.Hard.performance()

                # Calling function to calculate score
                score = CustomGame.Hard.score()
                print("No.of Correct answers: ", score)

                # Calling function to calculate percentage
                perc = CustomGame.Hard.percScore()
                print("Percentage score: ", perc, "%")
                print("\n", end="")

                # Geting current date and time
                time, date = CustomGame.Hard.clock()
                print("Current time : ", time)
                print("Current date : ", date)
                print("\n", end="")

                # Database connection
                Database.gamedb.connect()

                # Inserting values to database
                Database.gamedb.insert(name, num, score, perc, lev, time, date)
            else:
                print("Invalied Difficulty level !!!")

        elif choice == '3':
            # ------------Past game details-------------

            # Database connection
            Database.gamedb.connect()

            # Get user option
            Database.gamedb.method()

else:
    print("please type <play> to start the game")
