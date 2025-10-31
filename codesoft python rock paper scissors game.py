import random
print("❁´◡`❁ Rock-Paper-scissors Game❁´◡`❁")
choices=["rock","paper","scissors"]
user_score= comp_score=0
while True:
    user = input("\nEnter Rock, Paper, or Scissors:").lower()
    if user not in choices:
        print("❌ Invalid choice! Try Again.")
        continue
    comp = random.choice(choices)
    print(f"You chose: {user}")
    print(f"Computer chose: {comp}")

    if user == comp:
        print("┬┬﹏┬┬ It's a Tie!")
    elif(user == "rock" and comp == "scissors")or\
        (user == "scissors" and comp == "paper")or\
        (user == "paper" and comp == "rock"):
        print("✅ you win!")
        user_score += 1
    else:
        print("❌ you lose!")

        comp_score += 1
    print(f"^_____^ Score➡️You: {user_score} | computer: {comp_score}")
    again=input("play again? (yes/no):").lower()
    if again !="yes":
        print("\nThanks for playing!")
        break
        
        
    

