import requests
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
print(f"""{GREEN}
    ____                        _          _______           __         
   / __ \____  ____ ___  ____ _(_)___     / ____(_)___  ____/ /__  _____
  / / / / __ \/ __ `__ \/ __ `/ / __ \   / /_  / / __ \/ __  / _ \/ ___/
 / /_/ / /_/ / / / / / / /_/ / / / / /  / __/ / / / / / /_/ /  __/ /    
/_____/\____/_/ /_/ /_/\__,_/_/_/ /_/  /_/   /_/_/ /_/\__,_/\___/_/     
                                                                        
""")
host = ("http://api.hackertarget.com/reverseiplookup/?q=")
ip = input("Enter IP Here : ") #this will Enter IP Here
response = requests.get(host + ip )
Sources = response.text
print()
print(f"{RED}Results")
print()
print(Sources)
file = open("domain.txt","w")
file.write(Sources)
file.close()
print(f"{GREEN} ")
print("The results are saved in (domain.txt)") 