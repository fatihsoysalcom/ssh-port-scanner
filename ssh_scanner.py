import socket
import sys

def scan_ssh_port(host, port=22, timeout=1):
    """Scans a single host for an open SSH port."""
    try:
        # Create a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(timeout)
        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))
        # If connect_ex returns 0, the connection was successful (port is open)
        if result == 0:
            return True
        else:
            return False
    except socket.gaierror:
        # Handle cases where the hostname cannot be resolved
        print(f"Hostname could not be resolved: {host}")
        return False
    except socket.error:
        # Handle other socket-related errors
        print(f"Could not connect to {host}")
        return False
    finally:
        # Ensure the socket is closed
        sock.close()

def main():
    """Main function to get target and perform scan."""
    if len(sys.argv) < 2:
        print("Usage: python ssh_scanner.py <target_host>")
        sys.exit(1)

    target_host = sys.argv[1]
    ssh_port = 22  # Default SSH port
    scan_timeout = 1 # Timeout in seconds

    print(f"Scanning {target_host} for SSH port ({ssh_port})...")

    if scan_ssh_port(target_host, ssh_port, scan_timeout):
        print(f"SSH port {ssh_port} is OPEN on {target_host}.")
    else:
        print(f"SSH port {ssh_port} is CLOSED or unreachable on {target_host}.")

if __name__ == "__main__":
    main()
