import random
import time
import os
import sys

# Terminal Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Player Blueprint (OOPs Concept)
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

    def deduct_points(self, points):
        self.score -= points

# Main Game Engine (OOPs Concept)
class TruthAndDareGame:
    def __init__(self):
        self.players = []
        self.original_truths = [
            "Group mein sabse zyada jhooth kaun bolta hai?",
            "Aapka sabse bada aur embarrassing secret kya hai?",
            "Agar aapko is room mein se kisi ko date karna ho, toh kaun hoga?",
            "Aapne last time kab aur kis baat par jhooth bola tha?",
            "Kya aapne kabhi school/college mein cheating ki hai? Pakde gaye the?"
        ]
        self.original_dares = [
            "Class ke samne khade hokar kisi teacher ki acting karke dikhao!",
            "Apne phone ka last WhatsApp chat khol kar sabko unke messages padhwao.",
            "{} ko dekho aur ek romantic gana gao!",
            "Agle 2 rounds tak aapko har sentence ke baad 'Moo' bolna padega.",
            "{} ke pair chhuo aur bolo 'Aap hi mere bhagwan ho'!"
        ]
        self.truths = list(self.original_truths)
        self.dares = list(self.original_dares)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_beep(self):
        sys.stdout.write('\a')
        sys.stdout.flush()

    def show_ascii_art(self):
        art = f"""{Colors.CYAN}
  _____                _     _        ___    ____                    
 |_   _| __ _   _  _ _| |__  | |__    ( _ )  |  _ \\   __ _  _ __  ___ 
   | |  '__/ _` | | | | __| | '_ \\   / _ \\  | | | | / _` || '__|/ _ \\
   | | |  | (_| | |_| | |_  | | | | | (_) | | |_| || (_| || |  |  __/
   |_|___\__,_|\\__,_|\\__| |_| |_|  \\___/  |____/  \\__,_||_|   \\___|
        {Colors.ENDC}"""
        print(art)

    def setup_players(self):
        self.clear_screen()
        self.show_ascii_art()
        
        while True:
            try:
                num = int(input(f"{Colors.BOLD}Kitne log khel rahe hain? (Min 2): {Colors.ENDC}"))
                if num >= 2:
                    break
                print(f"{Colors.FAIL}Kam se kam 2 players chahiye bhai!{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Valid number daalo yaara.{Colors.ENDC}")

        for i in range(num):
            while True:
                name = input(f"Player {i+1} ka naam: ").strip()
                if name:
                    # Player object banakar list mein daal rahe hain
                    self.players.append(Player(name))
                    break
                print(f"{Colors.FAIL}Naam khali nahi ho sakta!{Colors.ENDC}")

    def show_scoreboard(self):
        print(f"\n{Colors.BOLD}--- 📊 CURRENT SCOREBOARD ---{Colors.ENDC}")
        for p in self.players:
            print(f"👤 {p.name}: {Colors.WARNING}{p.score}{Colors.ENDC} Points")
        print("-----------------------------\n")

    def spin_bottle(self):
        print("🍾 Bottle ghum rahi hai...")
        for _ in range(4):
            time.sleep(0.4)
            print(".", end="", flush=True)
            self.play_beep()
        print("\n")

    def start_game_loop(self):
        while True:
            self.clear_screen()
            self.show_scoreboard()
            self.spin_bottle()

            current_player = random.choice(self.players)
            self.play_beep()
            print(f"🎯 Target Locked! Baari hai: {Colors.BOLD}{Colors.FAIL}{current_player.name.upper()}{Colors.ENDC} ki!")

            choice = input(f"\n{Colors.CYAN}(T)ruth{Colors.ENDC} ya {Colors.FAIL}(D)are{Colors.ENDC}? [Ya 'quit' band karne ke liye]: ").lower().strip()

            if choice == 'quit':
                break
            elif choice in ['t', 'truth']:
                if not self.truths:
                    self.truths = list(self.original_truths)
                task = random.choice(self.truths)
                self.truths.remove(task)
                print(f"\n{Colors.CYAN}🤔 TRUTH FOR {current_player.name.upper()}:{Colors.ENDC}\n👉 {Colors.BOLD}{task}{Colors.ENDC}")
            elif choice in ['d', 'dare']:
                if not self.dares:
                    self.dares = list(self.original_dares)
                task = random.choice(self.dares)
                self.dares.remove(task)
                
                if "{}" in task:
                    others = [p.name for p in self.players if p.name != current_player.name]
                    target = random.choice(others) if others else "kisi dost"
                    task = task.format(target)
                print(f"\n{Colors.FAIL}⚡ DARE FOR {current_player.name.upper()}:{Colors.ENDC}\n👉 {Colors.BOLD}{Colors.WARNING}{task}{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}Galat input! Round skipped.{Colors.ENDC}")
                time.sleep(1.5)
                continue

            print("\n---------------------------------------------")
            status = input("Task poora kiya? (Y)es / (N)o: ").lower().strip()
            if status in ['y', 'yes']:
                print(f"🎉 {Colors.GREEN}+10 Points!{Colors.ENDC}")
                current_player.add_points(10)
            else:
                print(f"👎 {Colors.FAIL}-5 Points! Darpok!{Colors.ENDC}")
                current_player.deduct_points(5)

            input(f"\nPress Enter for next round...")

        self.end_game()

    def end_game(self):
        self.clear_screen()
        print(f"{Colors.HEADER}============================================={Colors.ENDC}")
        print(f"{Colors.HEADER}               🎮 GAME OVER 🎮                {Colors.ENDC}")
        print(f"{Colors.HEADER}=============================================\n")
        
        # Winner nikalne ka logic object list se
        winner = max(self.players, key=lambda p: p.score)
        print(f"🏆 Sabse bada khiladi: {Colors.GREEN}{Colors.BOLD}{winner.name.upper()}{Colors.ENDC} ({winner.score} Points)!")

# Game Start Karne Ka Standard Tareeka
if __name__ == "__main__":
    game = TruthAndDareGame()
    game.setup_players()
    game.start_game_loop()