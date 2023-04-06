# Description: Echo client program that uses TCP to communicate with an Echo server. This program asks the user to enter the IP address, port number of the server, and a message for the server. The program sends the message to the server and listens for replies. The program displays an error message if the IP address or port number are incorrect.
# Developer: Oscar Saavedra
# Date: 04/07/2023

# Import IP Address library
import ipaddress as ipa

def main():
    # Prompt message
    print("TCP SOCKET CLIENT PROGRAM\n")
    
    # Prompt user for the user for the IP address
    try:
        # Use ipaddress library to verify input is an IP address
        ip = ipa.ip_address(input("Enter the server IP address: "))
        # Prompt user for the port number
        port = int(input("Enter the server port number: "))
        
        # Validate port number is in acceptable range
        if((1 <= port <= 65535)):
            
            # Prompt user for their message
            message = input("Enter a message (enter \"quit\" to exit): ")
            
            print(ip)
            print(port)
            print(message)
        else:
            print("ERROR: Invalid port number")
            return
    # Handle invalid IP address exception
    except Exception as error:
        print("ERROR: ", error)
        return
    
if __name__ == "__main__":
    main()