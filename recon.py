'''
def custom_nmap(ip):
    var = f"nmap -A -p- {ip} -v"
    print(f"running nmap scan against {ip}...")
    print(f"nmap command: {var}")


# start point to automate your recon
custom_nmap(input("What IP would you like to scan?"))
'''

#--------------------------------------------------------
# -------------- BUILD YOUR OWN RECON TOOL -------------
# --------------------------------------------------------

import os 

def recon(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")
    # print results
    os.system(f"dirb {ip}")
    # save results to a file
    os.system(f"sqlmap {ip}")
    

ip = input("What IP would you like to scan?")
# error handing should be done. assuming only correct input for now
recon(ip)