#!/usr/bin/env python3
"""
Simple TCP client that connects to a server
Usage: python client.py [client_port]
       If no port is specified, the OS will assign one dynamically
"""
import socket
import sys

HOST = '127.0.0.1'  # Server address
SERVER_PORT = 50000  # Server listens on this port

def start_client(client_port=None):
    """Connect to the server and send messages"""
    # Create socket with specified or dynamic port allocation
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Enable address reuse to allow immediate port rebinding
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind to specified port or let OS choose
        if client_port:
            try:
                client_socket.bind(('', client_port))
                print(f"Client bound to local port: {client_port}")
            except OSError as e:
                print(f"Error: Could not bind to port {client_port}: {e}")
                print("The port may still be in TIME_WAIT state from a previous connection.")
                client_socket.close()
                sys.exit(1)
        else:
            client_socket.bind(('', 0))  # 0 means OS will assign an available port
            local_port = client_socket.getsockname()[1]
            print(f"Client using dynamically assigned port: {local_port}")
        
        # Connect to the server
        print(f"Connecting to server at {HOST}:{SERVER_PORT}...")
        client_socket.connect((HOST, SERVER_PORT))
        print(f"Connected to {HOST}:{SERVER_PORT}")
        
        # Interactive message loop
        while True:
            # Get message from user
            message = input("\nEnter message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                print("Closing connection...")
                break
            
            # Send message to server
            client_socket.sendall(message.encode('utf-8'))
            
            # Receive response from server
            data = client_socket.recv(1024)
            
            if not data:
                print("Server closed the connection")
                break
            
            response = data.decode('utf-8')
            print(f"Server response: {response}")
            
    except ConnectionRefusedError:
        print(f"Error: Could not connect to server at {HOST}:{SERVER_PORT}")
        print("Make sure the server is running.")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Properly close the connection
        try:
            # Shutdown the socket to send FIN packet
            client_socket.shutdown(socket.SHUT_RDWR)
        except:
            pass  # Socket may already be closed
        
        client_socket.close()
        print("Socket closed")

if __name__ == "__main__":
    # Get client port from command line (optional)
    if len(sys.argv) > 1:
        try:
            client_port = int(sys.argv[1])
            if client_port < 1024 or client_port > 65535:
                print("Warning: Port should be between 1024 and 65535")
                print("Ports below 1024 require elevated privileges")
        except ValueError:
            print(f"Error: Invalid port number '{sys.argv[1]}'")
            print(f"Usage: python {sys.argv[0]} [client_port]")
            sys.exit(1)
    else:
        client_port = None  # Let OS assign port dynamically
    
    start_client(client_port)
