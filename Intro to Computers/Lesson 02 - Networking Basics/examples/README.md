# Socket Communication Demo

This demo showcases TCP socket communication between a server and multiple clients, demonstrating important networking concepts like port binding, concurrent connections, and socket reuse.

## Files

- **`server.py`** - Multi-threaded TCP server listening on port 50000
- **`client.py`** - TCP client with configurable local port

## Quick Start

### 1. Start the Server

```bash
python server.py
```

The server will listen on `127.0.0.1:50000` and wait for client connections.

### 2. Connect Clients

Open new terminal windows and run:

```bash
# Client with OS-assigned port
python client.py

# Client with specific port (e.g., 51000)
python client.py 51000

# Another client with different port
python client.py 52000
```

Each client can send messages to the server, which will echo them back. Type `quit` to disconnect a client.

## Demonstrations

### Demo 1: Multiple Clients Can Connect to the Same Server

This demonstrates that **multiple clients can connect to the same server port** because the server uses threading to handle each connection independently.

**Steps:**
1. Start the server in Terminal 1
2. Start first client in Terminal 2: `python client.py 51000`
3. Start second client in Terminal 3: `python client.py 52000`
4. Send messages from both clients - both work simultaneously!

**What you'll observe:**
- Server shows `Active clients: 2`
- Both clients can send/receive messages concurrently
- Each client uses a unique local port (51000 and 52000)

### Demo 2: Multiple Clients CANNOT Use the Same Local Port

This demonstrates that **only one client can bind to a specific local port at a time**.

**Steps:**
1. Start the server: `python server.py`
2. Start first client on port 51000: `python client.py 51000`
3. Try to start second client on same port: `python client.py 51000`

**What you'll observe:**
```
Error: Could not bind to port 51000: [WinError 10048] Only one usage of each socket address...
The port may still be in TIME_WAIT state from a previous connection.
```

**Why this happens:**
- Each port can only be bound by one process at a time
- Even after closing, ports may stay in TIME_WAIT state briefly
- The OS reserves the port until the TCP connection fully terminates

### Demo 3: Socket Reuse After Disconnection

**Steps:**
1. Start client on port 51000: `python client.py 51000`
2. Type `quit` to disconnect cleanly
3. Immediately restart: `python client.py 51000`

**What you'll observe:**
- Thanks to `SO_REUSEADDR`, the port can be reused immediately
- Without this option, you'd need to wait ~30-120 seconds (TIME_WAIT period)

## Key Networking Concepts Demonstrated

1. **Port Binding**: Each socket must bind to a unique local address/port combination
2. **Server vs Client Ports**: 
   - Server always listens on port 50000
   - Clients bind to different local ports (51000, 52000, etc.)
3. **Concurrent Connections**: Multiple clients connect to the same server port because the server creates separate sockets for each accepted connection
4. **Socket States**: TCP sockets go through states (ESTABLISHED, TIME_WAIT, CLOSED)
5. **Socket Options**: `SO_REUSEADDR` allows immediate port reuse

### Demo 4:  Powershell Open Ports

```powershell
# Show only established IPv4 connections (active client-server connections, excluding localhost)
Get-NetTCPConnection -State Established | Where-Object {$_.LocalAddress -notmatch ':' -and $_.LocalAddress -notmatch '^127\.' -and $_.LocalAddress -ne '0.0.0.0'} | Sort-Object {[System.Version]$_.LocalAddress} | Select-Object State, LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Format-Table

# Show only listening ports
Get-NetTCPConnection -State Listen | Where-Object {$_.LocalAddress -notmatch ':'} | Sort-Object {[System.Version]$_.LocalAddress} | Select-Object LocalAddress, LocalPort, OwningProcess, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Format-Table

# Show all IPv4 connections (all states)
Get-NetTCPConnection | Where-Object {$_.LocalAddress -notmatch ':'} | Sort-Object State, {[System.Version]$_.LocalAddress} | Select-Object State, LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Format-Table
```

## Troubleshooting

### Port Already in Use

If you see "Address already in use" errors:

```powershell
# Find process using the port
Get-NetTCPConnection -LocalPort 51000

# Kill the process
Stop-Process -Id (Get-NetTCPConnection -LocalPort 51000).OwningProcess -Force
```

### Server Won't Stop with Ctrl+C

The server uses a 1-second timeout on `accept()` to handle interrupts properly on Windows. It should stop within 1 second of pressing Ctrl+C.

### Multiple Python Processes Running

To see all Python processes using network ports:

```powershell
Get-NetTCPConnection | Where-Object {(Get-Process -Id $_.OwningProcess).ProcessName -eq "python"} | Select-Object LocalPort, RemotePort, State, OwningProcess
```

## Technical Details

**Server Architecture:**
- Uses threading to handle multiple clients concurrently
- Each client gets its own thread with a dedicated socket
- Main thread continues accepting new connections

**Client Architecture:**
- Binds to specified local port (or gets OS-assigned port)
- Connects to server on port 50000
- Properly closes connection with shutdown() and close()

**Socket Options:**
- `SO_REUSEADDR`: Allows immediate port reuse after program termination
- Timeout on server accept: Allows clean shutdown on Windows
