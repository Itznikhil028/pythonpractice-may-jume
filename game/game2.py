import random
import time
import os
import sys

# Terminal mein colors lane ke liye (ANSI Escape Codes)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Laptop se sound nikalne ka function
def play_beep():
    sys.stdout.write('\a')
    sys.stdout.flush()

original_truths = [
    "Group mein sabse zyada jhooth kaun bolta hai?",
    "Aapka sabse bada aur embarrassing secret kya hai?",
    "Agar aapko is room mein se kisi ko date karna ho, toh kaun hoga?",
    "Aapne last time kab aur kis baat par jhooth bola tha?",
    "Kya aapne kabhi school/college mein cheating ki hai? Pakde gaye the?",
    "Is group mein aapko sabse zyada annoying kaun lagta hai?"
]

# Note: Kuch dares mein {} lagaya hai taaki dusre player ka naam wahan aa sake dynamically!
original_dares = [
    "Class ke samne khade hokar kisi teacher ki acting karke dikhao!",
    "Apne phone ka last WhatsApp chat khol kar sabko unke messages padhwao.",
    "{} ko dekho aur ek romantic gana gao!",
    "Agle 2 rounds tak aapko har sentence ke baad 'Moo' bolna padega.",
    "{} ke pair chhuo aur bolo 'Aap hi mere bhagwan ho'!",
    "Bina hase agle 1 minute tak sabko ajeeb chehre banakar dikhao.",
    "{} ka phone chhino aur unki gallery check karo 10 seconds ke liye!"
]

truths = list(original_truths)
dares = list(original_dares)

def main():
    global truths, dares
    clear_screen()
    print(f"{Colors.HEADER}============================================={Colors.ENDC}")
    print(f"{Colors.HEADER}     🔥 WELCOME TO CONSOLE TRUTH & DARE PRO 🔥   {Colors.ENDC}")
    print(f"{Colors.HEADER}============================================={Colors.ENDC}\n")
    
    while True:
        try:
            num_players = int(input("Kitne log khel rahe hain? (Minimum 2): "))
            if num_players >= 2:
                break
            print(f"{Colors.FAIL}Kam se kam 2 players toh hone chahiye bhai!{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please ek valid number daalo.{Colors.ENDC}")
            
    players = []
    scores = {}
    
    for i in range(num_players):
        name = input(f"Player {i+1} ka naam: ").strip()
        players.append(name)
        scores[name] = 0
        
    print(f"\n{Colors.GREEN}Chalo, Game Start Karte Hain! Press Enter...{Colors.ENDC}")
    input()

    while True:
        clear_screen()
        print(f"{Colors.BOLD}--- 📊 SCOREBOARD ---{Colors.ENDC}")
        for p, s in scores.items():
            print(f"👤 {p}: {Colors.WARNING}{s}{Colors.ENDC} Points")
        print("---------------------\n")
        
        # Suspense Sound and Animation Effect
        print("🍾 Bottle ghum rahi hai...")
        for _ in range(4):
            time.sleep(0.5)
            print(".", end="", flush=True)
            play_beep() # Chhoti tik-tik sound
        print("\n")
        
        current_player = random.choice(players)
        
        # Target lock sound effect
        play_beep()
        time.sleep(0.1)
        play_beep()
        
        print(f"🎯 Target Locked! Agli baari hai: {Colors.BOLD}{Colors.FAIL}{current_player.upper()}{Colors.ENDC} ki!")
        
        choice = input(f"\nKya chunoge bhai? {Colors.CYAN}(T)ruth{Colors.ENDC} ya {Colors.FAIL}(D)are{Colors.ENDC}? [Ya 'quit' to exit]: ").lower().strip()
        
        if choice == 'quit':
            break
            
        if choice in ['t', 'truth']:
            if not truths:
                print(f"\n{Colors.WARNING}[Saare Truth khatam! Resetting...]{Colors.ENDC}")
                truths = list(original_truths)
                
            question = random.choice(truths)
            truths.remove(question)
            
            print(f"\n{Colors.CYAN}🤔 TRUTH QUESTION FOR {current_player.upper()}:{Colors.ENDC}")
            print(f"👉 {Colors.BOLD}{question}{Colors.ENDC}")
            
        elif choice in ['d', 'dare']:
            if not dares:
                print(f"\n{Colors.WARNING}[Saare Dare khatam! Resetting...]{Colors.ENDC}")
                dares = list(original_dares)
                
            task = random.choice(dares)
            dares.remove(task)
            
            # Dynamic Name Logic: Agar dare mein {} hai, toh kisi aur random player ka naam wahan daal do
            if "{}" in task:
                other_players = [p for p in players if p != current_player]
                random_target = random.choice(other_players) if other_players else "kisi dost"
                task = task.format(random_target)
            
            print(f"\n{Colors.FAIL}⚡ DARE TASK FOR {current_player.upper()}:{Colors.ENDC}")
            print(f"👉 {Colors.BOLD}{Colors.WARNING}{task}{Colors.ENDC}")
            
        else:
            print(f"\n{Colors.FAIL}Galat input! Round skipped.{Colors.ENDC}")
            time.sleep(2)
            continue
            
        print("\n---------------------------------------------")
        status = input("Kya task poora kiya? (Y)es / (N)o: ").lower().strip()
        
        if status in ['y', 'yes']:
            print(f"🎉 {Colors.GREEN}Shabaash! {current_player} ko milte hain +10 points!{Colors.ENDC}")
            scores[current_player] += 10
        else:
            print(f"👎 {Colors.FAIL}Darpok! {current_player} ke -5 points ho gaye!{Colors.ENDC}")
            scores[current_player] -= 5
            
        print("\nAgla round khelne ke liye Enter dabayein...")
        input()

    clear_screen()
    print(f"{Colors.HEADER}============================================={Colors.ENDC}")
    print(f"{Colors.HEADER}               🎮 GAME OVER 🎮                {Colors.ENDC}")
    print(f"{Colors.HEADER}=============================================\n")
    print("Final Scores:")
    for p, s in scores.items():
        print(f"{p}: {s} points")
        
    winner = max(scores, key=scores.get)
    print(f"\n🏆 Aur is game ka sabse bada player hai: {Colors.GREEN}{Colors.BOLD}{winner.upper()}{Colors.ENDC}! Claps 👏")

if __name__ == "__main__":
    main()