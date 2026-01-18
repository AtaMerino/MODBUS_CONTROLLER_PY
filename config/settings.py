"""Settings management module for Modbus Controller.

This module handles loading and managing configuration settings
for RTU and TCP communication handlers.
"""


class Settings:
    """Configuration settings for Modbus Controller.
    
    Attributes:
        rtu_port (str): Serial port for RTU communication (e.g., '/dev/ttyUSB0')
        rtu_baud (int): Baud rate for RTU communication (default: 9600)
        tcp_host (str): TCP host address for TCP communication
        tcp_port (int): TCP port number for TCP communication
        timeout_ms (int): Communication timeout in milliseconds
    """
    
    def __init__(self):
        """Initialize settings with default values."""
        self.rtu_port = "/dev/ttyUSB0"
        self.rtu_baud = 9600
        self.tcp_host = "127.0.0.1"
        self.tcp_port = 502
        self.timeout_ms = 5000
    
    def load(self):
        """Load settings and print configuration.
        
        In a full implementation, this would load from a JSON or YAML file.
        Currently loads default values and logs them.
        """
        print(f"[Settings] RTU Port: {self.rtu_port}, Baud: {self.rtu_baud}")
        print(f"[Settings] TCP Host: {self.tcp_host}, Port: {self.tcp_port}")
        print(f"[Settings] Timeout: {self.timeout_ms}ms")
    
    def __repr__(self):
        """Return string representation of settings."""
        return (
            f"Settings(rtu_port={self.rtu_port}, rtu_baud={self.rtu_baud}, "
            f"tcp_host={self.tcp_host}, tcp_port={self.tcp_port}, "
            f"timeout_ms={self.timeout_ms})"
        )


def load_settings():
    """Factory function to load and initialize settings.
    
    Returns:
        Settings: Configured Settings object.
    """
    settings = Settings()
    settings.load()
    return settings
