import sys
import socket
sys.path.insert(0, '..') # Import the files where the modules are located

from constants import *
from ds_node import DSNode

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a remote server (doesn't have to be reachable)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        ipv4_address = s.getsockname()[0]
        return ipv4_address
    except Exception as e:
        print("Error occurred while getting IPv4 address:", e)
        return None

def ds_node():
    ip = get_ip_address()
    print("\033[93m" + f"Your ip is {ip}\n" + "\033[0m")
    print("\033[93m" + f"Enter Port and ID number for the node:\n" + "\033[0m")
    port = int(input())
    id = int(input())
    node_1 = DSNode(ip, port, id, 2, 2)
    node_1.start()

    while(True):
        print("\033[94mPress 1 to connect to a node\033[0m")
        print("\033[94mPress 2 to start the dolev strong protocol\033[0m")
        print("\033[94mPress 3 to give the accepted message\033[0m")
        print("\033[94mPress 4 to stop the node\033[0m")
        
        choice = int(input())
        
        if choice == 1:
            port = int(input("\033[94mEnter the port of the node you want to connect to\n\033[0m"))
            node_1.connect_with_node(ip , port)
        elif choice == 2:
            num = int(input("\033[94mEnter the number you want to send\n\033[0m"))
            node_1.start_the_protocol(num)
        elif choice == 3:
            node_1.give_results()
        elif choice == 4:
            node_1.stop()
            break
        
ds_node()
    
