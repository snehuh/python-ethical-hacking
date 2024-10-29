import os #interact with OS
import sys #SYSTEM specific operations
import time #calculate time intervals
from collections import defaultdict  #store and manage packet counts
from scapy.all import sniff, IP  # sniff function and IP class

# what is default dict?
THRESHOLD = 40
print(f"THRESHOLD: {THRESHOLD}")

def packet_callback(packet):
    src_ip = packet[IP].src 
    packet_count[src_ip] += 1
    current_time = time.time()
    time_interval = current_time - start_time[0]

    # check if dos happening at freq of once/sec
    if time_interval >= 1:
        for ip, count in packet_count.items():
            packet_rate = count / time_interval
            # print ip and packet rate for testing

            if packet_rate > THRESHOLD and ip not in blocked_ips:
                print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
                # now we block the IP
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)

        packet_count.clear()
        start_time[0] = current_time

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script requires root privileges")
        sys.exit(1)
        #why root? because need access to network 

         # what is a default dict?
         # ans: an invisible safety net for missing keys. says 0 by default
        packet_count = defaultdict(int)
        start_time = [time.time()]
        blocked_ips = set()

        print("Monitoring network traffic.....")
        sniff(filter=ip, prn=packet_callback)


'''
# execution set up

2 vms: left runs dos_blocker, 2nd : packetr flooding script

- set up these vms and try it

sudo iptables -L INPUT -n  (to check if no IPs are blokced now)

later you can unblock and try again!

limitations:
- the method of evaluation is transfer rate
    - there might false positives and false negatives
'''