import requests
import time
import os
import sys
import random
from colorama import Fore, Back, Style, init

# Initialize Ultimate Hacker Colors
init(autoreset=True)

class WingoHack:
    def __init__(self):
        self.api_url = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.wins = 0
        self.losses = 0
        self.last_period = None
        self.last_prediction = None
        self.access_password = "robin1235"  # তোমার দেওয়া পাসওয়ার্ড

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def login_screen(self):
        """পাসওয়ার্ড প্রটেকশন সিস্টেম"""
        self.clear()
        print(Fore.RED + Style.BRIGHT + "========================================")
        print(Fore.YELLOW + "      🛡️ SECURITY AUTHENTICATION 🛡️")
        print(Fore.RED + "========================================")
        
        password = input(Fore.WHITE + "\n[🔑] Enter Access Password: ")
        
        if password == self.access_password:
            print(Fore.GREEN + "\n[✅] Access Granted! Loading System...")
            time.sleep(1.5)
            return True
        else:
            print(Fore.RED + "\n[❌] Incorrect Password! Connection Terminated.")
            time.sleep(1)
            sys.exit()

    def hacker_banner(self):
        self.clear()
        print(Fore.RED + Style.BRIGHT + """
    ██╗    ██╗██╗███╗   ██╗ ██████╗  ██████╗ 
    ██║    ██║██║████╗  ██║██╔════╝ ██╔═══██╗
    ██║ █╗ ██║██║██╔██╗ ██║██║  ███╗██║   ██║
    ██║███╗██║██║██║╚██╗██║██║   ██║██║   ██║
    ╚███╔███╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
        """)
        print(Back.RED + Fore.WHITE + " 💀 SYSTEM BREACHED: WINGO SERVER HACKED 💀 ")
        print(Fore.RED + " ⚡ HACKED BY : MD ROBIN ISLAM")
        print(Fore.RED + " ⚡ STATUS    : ADMIN ACCESS GRANTED")
        print(Fore.RED + " ⚡ WARNING   : FOLLOW MUST BE 7 STEP (RISK FREE)")
        print(Fore.RED + "="*50)

    def fetch_data(self):
        try:
            params = {"pageNo": 1, "pageSize": 20, "typeId": 1, "language": 0, "random": "4f3d7f7a8a3d4f3d"}
            res = requests.get(self.api_url, headers=self.headers, params=params, timeout=5)
            if res.status_code == 200:
                data = res.json()
                if data['code'] == 0:
                    return data['data']['list']
            return None
        except:
            return None

    def get_hack_signal(self, history):
        if not history: return "WAIT", "CONNECTING..."

        results = []
        for item in history[:10]:
            num = int(item['number'])
            results.append("BIG" if num >= 5 else "SMALL")

        last_1 = results[0]
        last_2 = results[1]
        last_3 = results[2]

        prediction = ""
        hack_type = ""

        if last_1 == last_2:
            prediction = last_1
            hack_type = "TREND DETECTED (DRAGON) 🐉"
        else:
            prediction = "SMALL" if last_1 == "BIG" else "BIG"
            hack_type = "ZIGZAG DETECTED (FLIP) ⚡"

        return prediction, hack_type

    def print_terminal(self, period, pred, hack_type, history):
        self.hacker_banner()

        print(Fore.GREEN + "    [Injecting Payload...] ", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print(Fore.GREEN + "SUCCESS")
        print(Fore.GREEN + "    [Bypassing Firewall...] ", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print(Fore.GREEN + "SUCCESS")
        print(Fore.RED + "-"*50)

        color = Fore.CYAN if pred == "BIG" else Fore.YELLOW
        
        print(Fore.WHITE + "    😈 TARGET PERIOD : " + Fore.RED + str(period))
        print(Fore.WHITE + "    🦠 HACK TYPE     : " + Fore.MAGENTA + hack_type)
        print(Fore.WHITE + "    🎯 PREDICTION    : " + color + Style.BRIGHT + pred + " " + color + "●")
        
        print(Fore.RED + "-"*50)
        print(Back.BLACK + Fore.GREEN + "    💰 INVESTMENT PLAN: USE 7-STEP STRATEGY")
        print(Fore.RED + "-"*50)
        
        print(Fore.WHITE + "    DATA STREAM: ", end="")
        for i in range(8):
            n = int(history[i]['number'])
            c = Fore.CYAN if n >= 5 else Fore.YELLOW
            t = "B" if n >= 5 else "S"
            print(f"{c}{t}", end=" ")
        
        print(f"\n\n    🏆 HACK WINS: {Fore.GREEN}{self.wins} {Fore.WHITE}| 💀 FAIL: {Fore.RED}{self.losses}")

    def run(self):
        # প্রথমে লগইন স্ক্রিন চেক করবে
        if self.login_screen():
            while True:
                history = self.fetch_data()
                if not history:
                    print(Fore.RED + "    [!] SERVER CONNECTION FAILED...", end="\r")
                    time.sleep(2)
                    continue

                current_last_period = int(history[0]['issueNumber'])
                next_period = current_last_period + 1

                if self.last_period == current_last_period:
                    real_num = int(history[0]['number'])
                    real_res = "BIG" if real_num >= 5 else "SMALL"
                    
                    if self.last_prediction == real_res:
                        self.wins += 1
                        print(Back.GREEN + Fore.BLACK + f" ✅ SUCCESS! SERVER HACKED! {real_res} WON! ")
                    else:
                        self.losses += 1
                        print(Back.RED + Fore.WHITE + f" ❌ FAILED! SYSTEM DETECTED! {real_res} CAME! ")
                    
                    time.sleep(4)
                    self.last_period = None

                if self.last_period != next_period:
                    pred, hack_type = self.get_hack_signal(history)
                    self.print_terminal(next_period, pred, hack_type, history)
                    
                    self.last_period = next_period
                    self.last_prediction = pred
                    
                    print(Fore.LIGHTBLACK_EX + "\n    [WAITING FOR NEXT BLOCK]...", end="")
                    
                    for i in range(100):
                        time.sleep(1)
                        if i % 3 == 0:
                            check = self.fetch_data()
                            if check and int(check[0]['issueNumber']) == next_period:
                                break

if __name__ == "__main__":
    try:
        app = WingoHack()
        app.run()
    except KeyboardInterrupt:
        print("\n    [CONNECTION TERMINATED]")