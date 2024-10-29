import random

def generate_random_ip():
    return f"192.168.1.{random.randint(1, 20)}"

def check_firewall_rules(ip, rules):
    # arguments: ip_address and firewall_rules dictionary
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action  # will returm "block"
        return "allow"  # otherwise, allow

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.11": "block",
        "192.168.1.14": "block",
        "192.168.1.15": "block",
        "192.168.1.19": "block",
        "192.168.1.17": "block"
    }
    
    # to simulate network traffic
    for _ in range(12):
        ip_address = generate_random_ip()  
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()