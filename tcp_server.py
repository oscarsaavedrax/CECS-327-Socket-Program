# Description: Echo server program that uses TCP to communicate with an Echo client. This server receives a message from the client, changes the letters of the message to capital letters, then sends it back to the same client.
# Developer: Oscar Saavedra
# Date: 04/07/2023

# Import argparse library to handle commandline arguments
import argparse as agp

def main(ip, port):
    print(ip)
    print(port)
    
if __name__ == "__main__":
    # Create a parser to handle the commandline arguments
    parser = agp.ArgumentParser(description="Echo server")
    # Add argument information for IP address input
    parser.add_argument("--ip", default="", help="IP address to bind the server (default: "")")
    # Add argument information for port number input
    parser.add_argument("--port", type=int, default=12345, help="Port to bind the server (default: 12345)")
    # Parse the arguments
    args = parser.parse_args()
    # Start main and send in commandline arguments
    main(args.ip, args.port)