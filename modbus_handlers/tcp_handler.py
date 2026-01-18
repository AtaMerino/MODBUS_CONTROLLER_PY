"""TCP communication handler for Modbus protocol.

This module handles Modbus TCP communication over network sockets.
"""

import socket
import logging

logger = logging.getLogger(__name__)


class TCPHandler:
    """Handles Modbus TCP communication.
    
    Attributes:
        host (str): TCP server host address
        port (int): TCP server port number
        socket (socket.socket): TCP socket object
        initialized (bool): Whether the handler is initialized
    """
    
    DEFAULT_TIMEOUT = 5.0  # seconds
    DEFAULT_BUFFER_SIZE = 256
    
    def __init__(self):
        """Initialize TCP handler."""
        self.host = None
        self.port = None
        self.socket = None
        self.initialized = False
        print("[TCPHandler] Initialized")
    
    def connect(self, host, port):
        """Connect to a TCP Modbus server.
        
        Args:
            host (str): Server host address or IP
            port (int): Server port number (default Modbus TCP: 502)
            
        Returns:
            bool: True if connected successfully, False otherwise
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.DEFAULT_TIMEOUT)
            self.socket.connect((host, port))
            
            self.host = host
            self.port = port
            self.initialized = True
            print(f"[TCPHandler] Connected to {host}:{port}")
            return True
            
        except socket.error as e:
            print(f"[TCPHandler] Error: Cannot connect to {host}:{port}: {e}")
            self.initialized = False
            if self.socket:
                try:
                    self.socket.close()
                except:
                    pass
            self.socket = None
            return False
    
    def disconnect(self):
        """Disconnect from the TCP server.
        
        Returns:
            bool: True if disconnected successfully, False otherwise
        """
        if self.socket:
            try:
                self.socket.close()
                self.initialized = False
                print("[TCPHandler] Disconnected")
                self.socket = None
                return True
            except Exception as e:
                print(f"[TCPHandler] Error disconnecting: {e}")
                return False
        return False
    
    def send(self, data):
        """Send data over the TCP connection.
        
        Args:
            data (bytes or bytearray): Data to send
            
        Returns:
            int: Number of bytes sent, -1 if error
        """
        if not self.initialized:
            print("[TCPHandler] Error: Handler not initialized")
            return -1
        
        try:
            # Ensure data is bytes
            if isinstance(data, list):
                data = bytes(data)
            elif not isinstance(data, (bytes, bytearray)):
                data = bytes(data)
            
            bytes_sent = self.socket.send(data)
            print(f"[TCPHandler] Sent {bytes_sent} bytes")
            return bytes_sent
            
        except Exception as e:
            print(f"[TCPHandler] Error sending data: {e}")
            return -1
    
    def receive(self, max_length=None):
        """Receive data from the TCP connection.
        
        Args:
            max_length (int): Maximum number of bytes to receive 
                            (default: 256)
            
        Returns:
            bytes: Data received, empty bytes if error or no data
        """
        if not self.initialized:
            print("[TCPHandler] Error: Handler not initialized")
            return b''
        
        if max_length is None:
            max_length = self.DEFAULT_BUFFER_SIZE
        
        try:
            data = self.socket.recv(max_length)
            if len(data) > 0:
                print(f"[TCPHandler] Received {len(data)} bytes")
            return data
            
        except socket.timeout:
            # Timeout is normal in non-blocking operations
            return b''
            
        except Exception as e:
            print(f"[TCPHandler] Error receiving data: {e}")
            return b''
    
    def process(self):
        """Process TCP communications.
        
        Called regularly to handle TCP protocol processing.
        """
        if self.initialized:
            # Process TCP communications
            pass
            # Uncomment for debugging:
            # print("[TCPHandler] Processing...")
    
    def is_connected(self):
        """Check if the TCP connection is active.
        
        Returns:
            bool: True if connected and initialized, False otherwise
        """
        return self.initialized and self.socket is not None
    
    def __repr__(self):
        """Return string representation of TCP handler."""
        return (
            f"TCPHandler(host={self.host}, port={self.port}, "
            f"initialized={self.initialized})"
        )
