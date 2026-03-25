import random

# Selection of Computer
computer_selection = ["Rock","Paper","Scissors"]
select = random.choice(computer_selection)

#Input form User
print("Rock","Paper","Scissors")
User_Selection = input("Please enter your choice: ")

if User_Selection == "Rock":
    print('''   
            _______
        ---'    ____) 
               (_____)
               (_____)
                (____)
         ---.__(___)
                 ''')

elif User_Selection == "Paper":
    print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

elif User_Selection == "Scissors":
    print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)


print(f"Computer Choice: {select}")
#Condition Checking by Rules (Who Win or Lose)
if select == "Rock":
    print('''   
        _______
    ---'    ____)
           (_____)
           (_____)
            (____)
     ---.__(___)
             ''')


elif select == "Paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif select == "Scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)






if User_Selection == select:
    print("Tie")
elif User_Selection == "Rock" and select == "Scissors":
    print("You win")
elif User_Selection == "Scissors" and select == "Paper":
    print("You win")
elif User_Selection == "Paper" and select == "Rock":
    print("You win")
else:
    print("You lose")


