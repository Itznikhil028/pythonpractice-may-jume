import random
import time
import os

# Screen clear karne ka function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Truth aur Dare ke mazedaar sawal aur tasks
truths = [
    "Group mein sabse zyada jhooth kaun bolta hai?",
    "Aapka sabse bada aur embarrassing secret kya hai?",
    "Agar aapko is room mein se kisi ko date karna ho, toh kaun hoga?",
    "Aapne last time kab aur kis baat par jhooth bola tha?",
    "Kya aapne kabhi school/college mein cheating ki hai? Pakde gaye the?",
    "Is group mein aapko sabse zyada annoying kaun lagta hai?"
]

dares = [
    "Class ke samne khade hokar kisi teacher ki acting karke dikhao!",
    "Apne phone ka last WhatsApp chat khol kar sabko unke messages padhwao.",
    "Apne kisi dost ko call karke bolo 'Mujhe tumse pyaar ho gaya hai' aur call kaat do.",
    "Agle 2 rounds tak aapko har sentence ke baad 'Moo' (gaay ki tarah) bolna padega.",
    "Apni contact list mein se kisi random person ko 'I am single' message bhejo.",
    "Bina hase agle 1 minute tak sabko ajeeb chehre banakar dikhao."
]

def main():
    clear_screen()
    print("=============================================")
    print("     🔥 WELCOME TO TRUTH & DARE 🔥   ")
    print("=============================================\n")
    
    # Players ke naam input lena
    while True:
        try:
            num_players = int(input("How many players playing? (Minimum 2): "))
            if num_players >= 2:
                break
            print("Atleast 2 players required bhai!")
        except ValueError:
            print("Enter a valid number.")
            
    players = []
    scores = {}
    
    for i in range(num_players):
        name = input(f"Player {i+1} ka naam: ").strip()
        players.append(name)
        scores[name] = 0 # Sabka starting score 0
        
    print("\nChalo, Game Start Karte Hain! Press Enter...")
    input()

    # Main Game Loop
    while True:
        clear_screen()
        print("--- SCOREBOARD ---")
        for p, s in scores.items():
            print(f"👤 {p}: {s} Points")
        print("------------------\n")
        
        # Suspense banane ke liye "Bottle Spin" effect
        print("🍾 Bottle ghum rahi hai...")
        for _ in range(3):
            time.sleep(0.5)
            print("...")
        
        # Random player select karna
        current_player = random.choice(players)
        print(f"\n🎯 Target Locked! Agli baari hai: ** {current_player.upper()} ** ki!")
        
        # Choice lena
        choice = input("\nKya chunoge bhai? (T)ruth ya (D)are? [Ya 'quit' game band karne ke liye]: ").lower().strip()
        
        if choice == 'quit':
            break
            
        if choice in ['t', 'truth']:
            question = random.choice(truths)
            print(f"\n🤔 TRUTH QUESTION FOR {current_player}:")
            print(f"👉 {question}")
            
        elif choice in ['d', 'dare']:
            task = random.choice(dares)
            print(f"\n⚡ DARE TASK FOR {current_player}:")
            print(f"👉 {task}")
            
        else:
            print("\nGalat input! Agli baar sahi se T ya D likhna. Yeh round skip ho gaya.")
            time.sleep(2)
            continue
            
        # Task poora kiya ya nahi
        print("\n---------------------------------------------")
        status = input("Kya task poora kiya? (Y)es / (N)o: ").lower().strip()
        
        if status in ['y', 'yes']:
            print(f"🎉 Shabaash! {current_player} ko milte hain +10 points!")
            scores[current_player] += 10
        else:
            print(f"👎 Darpok! {current_player} ke -5 points ho gaye!")
            scores[current_player] -= 5
            
        print("\nAgla round khelne ke liye Enter dabayein...")
        input()

    # Game khatam hone par final winner declare karna
    clear_screen()
    print("=============================================")
    print("               KHEL KHATAM BETA 🎮                  ")
    print("=============================================\n")
    print("Final Scores:")
    for p, s in scores.items():
        print(f"{p}: {s} points")
        
    winner = max(scores, key=scores.get)
    print(f"\n🏆 iss game ka winner he : ** {winner.upper()} **! Claps 👏 hehe")

if __name__ == "__main__":
    main()