#====== SC SEND BY >> KALYAN KING

#===== TEAM NAME : KGF CYBER TEAM

import requests
import os

# ===============================
# 🎨 Color Codes
# ===============================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ===============================
# 💥 TOOL BANNER 💥
# ===============================
banner = f"""
{CYAN}{BOLD}
██████  ██████  ██████  ██████ 
██      ██  ██  ██  ██  ██  ██
████    ██████  ██      ██████
██      ██  ██  ██      ██  ██
██████  ██  ██  ██████  ██  ██
{RESET}
"""

print(banner)
print(f"{YELLOW}{BOLD}🔥 TOOL: Free Fire Like 🔥{RESET}")
print(f"{GREEN}{BOLD}👑 DEVELOPER: KALYAN KING 👑{RESET}")
print(f"{CYAN}{BOLD}⚡ STATUS: FREE ⚡{RESET}")
print("="*50)

# ===============================
# 🌐 Open Telegram Link
# ===============================
os.system("xdg-open https://t.me/KGF_TEAM_CYBER")

# ===============================
# 👍 Send Like Function
# ===============================
def send_like():
    try:
        uid = input(f"{YELLOW}Enter UID to send like: {RESET}")
        if not uid.strip():
            print(f"{RED}⚠️ UID cannot be empty!{RESET}")
            return
        url = f"https://devraj.crazybook.my.id/likeapi.php?uid={uid}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{GREEN}✅ Like successfully sent!{RESET}")
        else:
            print(f"{RED}❌ Failed to send like. Status code: {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}⚠️ An error occurred: {e}{RESET}")

if __name__ == "__main__":
    send_like()