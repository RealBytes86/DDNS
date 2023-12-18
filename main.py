import requests 
import socket
import time

def update_ddns_no_ip_com(username, password, hostname, secondRequest) -> None:
    
    myip = None
    old_ip = None
    response = None
    
    while True:
        
        try:
            myip = requests.get('http://api.ipify.org')
            myip = myip.text
            print(f"MyIP: {myip}")
        except:
            continue
            
        try:
            old_ip = socket.gethostbyname(hostname)
            print(f"OldIP: {old_ip}")
        except:
            continue
        
        if myip == old_ip:
            None
        else:
            try:
                response = requests.get(f"http://{username}:{password}@dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={myip}")
                print(f"Response: {response.status_code}")
            except:
                continue
        
        time.sleep(secondRequest)
        continue

update_ddns_no_ip_com(username="", password="", hostname="", secondRequest=3)