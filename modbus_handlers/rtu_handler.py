"""RTU (serial) communication handler for Modbus protocol.

This module handles Modbus RTU communication over serial ports.
"""

import serial
import logging

logger = logging.getLogger(__name__)


class RTUHandler:
    """Handles Modbus RTU (serial) communication.
    
    Attributes:
        port (str): Serial port path (e.g., '/dev/ttyUSB0')
        baud_rate (int): Serial communication baud rate
        serial_connection (serial.Serial): Serial port connection object
        initialized (bool): Whether the handler is initialized
    """
    
    DEFAULT_TIMEOUT = 1.0  # seconds
    
    def __init__(self):
        """Initialize RTU handler."""
        self.port = None
        self.baud_rate = 9600
        self.serial_connection = None
        self.initialized = False
        print("[RTUHandler] Initialized")
    
    def open(self, port, baud=9600):
        """Open and configure serial port for RTU communication.
        
        Args:
            port (str): Serial port path (e.g., '/dev/ttyUSB0', 'COM3')
            baud (int): Baud rate (default: 9600)
            
        Returns:
            bool: True if port opened successfully, False otherwise
        """
        try:
            self.serial_connection = serial.Serial(
                port=port,
                baudrate=baud,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.DEFAULT_TIMEOUT,
                write_timeout=self.DEFAULT_TIMEOUT
            )
            
            self.port = port
            self.baud_rate = baud
            self.initialized = True
            print(f"[RTUHandler] Opened port {port} at {baud} baud")
            return True
            
        except serial.SerialException as e:
            print(f"[RTUHandler] Error: Cannot open port {port}: {e}")
            self.initialized = False
            return False
    
    def close(self):
        """Close the serial port connection.
        
        Returns:
            bool: True if closed successfully, False otherwise
        """
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.close()
                self.initialized = False
                print("[RTUHandler] Closed port")
                return True
            except Exception as e:
                print(f"[RTUHandler] Error closing port: {e}")
                return False
        return False
    
    def send(self, data):
        """Send data over the serial port.
        
        Args:
            data (bytes or bytearray): Data to send
            
        Returns:
            int: Number of bytes sent, -1 if error
        """
        if not self.initialized:
            print("[RTUHandler] Error: Handler not initialized")
            return -1
        
        try:
            # Ensure data is bytes
            if isinstance(data, list):
                data = bytes(data)
            elif not isinstance(data, (bytes, bytearray)):
                data = bytes(data)
            
            bytes_written = self.serial_connection.write(data)
            self.serial_connection.flush()
            print(f"[RTUHandler] Sent {bytes_written} bytes")
            return bytes_written
            
        except Exception as e:
            print(f"[RTUHandler] Error sending data: {e}")
            return -1
    
    def receive(self, max_length=256):
        """Receive data from the serial port.
        
        Args:
            max_length (int): Maximum number of bytes to receive (default: 256)
            
        Returns:
            bytes: Data received, empty bytes if error or no data
        """
        if not self.initialized:
            print("[RTUHandler] Error: Handler not initialized")
            return b''
        
        try:
            data = self.serial_connection.read(max_length)
            if len(data) > 0:
                print(f"[RTUHandler] Received {len(data)} bytes")
            return data
            
        except Exception as e:
            print(f"[RTUHandler] Error receiving data: {e}")
            return b''
    
    def process(self):
        """Process RTU communications.
        
        Called regularly to handle RTU protocol processing.
        """
        if self.initialized:
            # Process RTU communications
            pass
            # Uncomment for debugging:
            # print("[RTUHandler] Processing...")
    
    def is_open(self):
        """Check if the serial port is open.
        
        Returns:
            bool: True if port is open and initialized, False otherwise
        """
        return (
            self.initialized and 
            self.serial_connection is not None and 
            self.serial_connection.is_open
        )
    
    def __repr__(self):
        """Return string representation of RTU handler."""
        return (
            f"RTUHandler(port={self.port}, baud={self.baud_rate}, "
            f"initialized={self.initialized})"
        )
