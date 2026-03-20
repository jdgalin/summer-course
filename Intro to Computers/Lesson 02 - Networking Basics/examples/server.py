#!/usr/bin/env python3
"""
Simple TCP server that listens on port 50000
Handles multiple clients concurrently using threading
"""
import socket
import sys
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 50000        # Port to listen on

# Thread-safe counter for active clients
active_clients = 0
clients_lock = threading.Lock()

def handle_client(conn, addr):
    """Handle communication with a single client"""
    global active_clients
    
    with conn:
        with clients_lock:
            active_clients += 1
            print(f"\n[+] Client connected: {addr[0]}:{addr[1]} (Active clients: {active_clients})")
        
        try:
            while True:
                # Receive data from client
                data = conn.recv(1024)
                
                if not data:
                    break
                
                message = data.decode('utf-8')
                print(f"[{addr[0]}:{addr[1]}] {message}")
                
                # Echo the message back with a prefix
                response = f"Server received: {message}"
                conn.sendall(response.encode('utf-8'))
                
        except Exception as e:
            print(f"[!] Error with client {addr[0]}:{addr[1]}: {e}")
        finally:
            with clients_lock:
                active_clients -= 1
                print(f"[-] Client disconnected: {addr[0]}:{addr[1]} (Active clients: {active_clients})")

def start_server():
    """Start the TCP server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Allow reuse of address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            server_socket.bind((HOST, PORT))
        except OSError as e:
            print(f"Error binding to port {PORT}: {e}")
            sys.exit(1)
        
        server_socket.listen()
        # Set timeout so accept() doesn't block indefinitely
        # This allows KeyboardInterrupt to be caught properly on Windows
        server_socket.settimeout(1.0)
        
        print(f"Server listening on {HOST}:{PORT}")
        print("Waiting for clients... (Press Ctrl+C to stop)")
        
        try:
            while True:
                try:
                    # Accept incoming connection
                    conn, addr = server_socket.accept()
                    
                    # Create and start a new thread to handle this client
                    client_thread = threading.Thread(
                        target=handle_client,
                        args=(conn, addr),
                        daemon=True  # Thread will exit when main program exits
                    )
                    client_thread.start()
                    
                except socket.timeout:
                    # Timeout allows us to check for KeyboardInterrupt
                    continue
                
        except KeyboardInterrupt:
            print("\n\nServer shutting down...")
            print(f"Final active clients: {active_clients}")

if __name__ == "__main__":
    start_server()
