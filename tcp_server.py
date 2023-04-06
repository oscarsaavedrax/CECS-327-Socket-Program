# Description: Echo server program that uses TCP to communicate with an Echo client. This server receives a message from the client, changes the letters of the message to capital letters, then sends it back to the same client.
# Developer: Oscar Saavedra
# Date: 04/07/2023

# Import argparse library to handle commandline arguments
import argparse as agp
# Import socket library
import socket

def main(ip, port):
    # Create a socket instance with IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address
        s.bind((ip, port))
        # Enable server to accept connections, only 1 unacceptable connection allowed
        s.listen(1)
        # Accept a connection & create socket object to send/receive data
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            # Infinite loop to send and receive multiple messages to/from client
            while True:
                # Get message from client up to 1024 bytes
                message = conn.recv(1024)
                # If no messages then exit
                if not message:
                    break
                # Reply to client with message in all CAPS
                print("Message: ", message)
                conn.sendall(message.upper())
            
if __name__ == "__main__":
    # Create a parser to handle the commandline arguments
    parser = agp.ArgumentParser(description="Echo server")
    # Add argument information for IP address input
    parser.add_argument("--ip", default="0.0.0.0", help="IP address to bind the server (default: 0.0.0.0)")
    # Add argument information for port number input
    parser.add_argument("--port", type=int, default=12345, help="Port to bind the server (default: 12345)")
    # Parse the arguments
    args = parser.parse_args()
    # Start main and send in commandline arguments
    main(args.ip, args.port)