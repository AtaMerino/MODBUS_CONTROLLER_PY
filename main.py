"""Modbus Controller - Python Implementation

Main entry point for the Modbus Controller application.
Handles initialization of settings, device manager, and communication handlers.
"""

import logging
import time
import sys
from config.settings import load_settings
from devices.device_manager import DeviceManager
from modbus_handlers.rtu_handler import RTUHandler
from modbus_handlers.tcp_handler import TCPHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ModbusController:
    """Main Modbus Controller application.
    
    Coordinates initialization and operation of device manager
    and communication handlers.
    """
    
    def __init__(self):
        """Initialize the Modbus Controller."""
        print("Modbus Controller (Python) - Initializing...")
        
        # Initialize settings
        self.settings = load_settings()
        print("Settings loaded successfully")
        
        # Initialize device manager
        self.device_manager = DeviceManager()
        print("Device manager initialized")
        
        # Initialize Modbus handlers
        self.rtu_handler = RTUHandler()
        self.tcp_handler = TCPHandler()
        print("Modbus handlers initialized")
        
        print("Modbus Controller started successfully\n")
    
    def add_sample_devices(self):
        """Add some sample devices for demonstration."""
        self.device_manager.add_device(1, "Temperature Sensor", 1)
        self.device_manager.add_device(2, "Pressure Sensor", 2)
        self.device_manager.add_device(3, "Flow Meter", 3)
    
    def run(self, duration=None):
        """Run the main event loop.
        
        Args:
            duration (float): How long to run in seconds. 
                            If None, runs indefinitely.
        """
        start_time = time.time() if duration else None
        
        try:
            print("Starting main event loop...")
            iteration = 0
            
            while True:
                # Check duration limit
                if duration and (time.time() - start_time) > duration:
                    print(f"\nReached duration limit ({duration}s), stopping...")
                    break
                
                iteration += 1
                
                # Process devices
                self.device_manager.process()
                
                # Handle RTU communications
                self.rtu_handler.process()
                
                # Handle TCP communications
                self.tcp_handler.process()
                
                # Small sleep to prevent CPU spinning
                time.sleep(0.1)
                
                # Print status every 10 iterations (1 second)
                if iteration % 10 == 0 and iteration <= 50:
                    print(f"[Main] Event loop iteration {iteration}")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
        
        except Exception as e:
            print(f"\n\nError in main loop: {e}")
            logger.exception("Main loop exception")
        
        finally:
            self.shutdown()
    
    def shutdown(self):
        """Gracefully shutdown the controller."""
        print("\nShutting down Modbus Controller...")
        
        # Close handlers
        if self.rtu_handler.is_open():
            self.rtu_handler.close()
        
        if self.tcp_handler.is_connected():
            self.tcp_handler.disconnect()
        
        print("Modbus Controller stopped")
    
    def connect_rtu(self, port=None, baud=None):
        """Connect RTU handler.
        
        Args:
            port (str): Serial port path. Uses setting if None.
            baud (int): Baud rate. Uses setting if None.
            
        Returns:
            bool: True if connected, False otherwise
        """
        port = port or self.settings.rtu_port
        baud = baud or self.settings.rtu_baud
        return self.rtu_handler.open(port, baud)
    
    def connect_tcp(self, host=None, port=None):
        """Connect TCP handler.
        
        Args:
            host (str): Server host. Uses setting if None.
            port (int): Server port. Uses setting if None.
            
        Returns:
            bool: True if connected, False otherwise
        """
        host = host or self.settings.tcp_host
        port = port or self.settings.tcp_port
        return self.tcp_handler.connect(host, port)


def main():
    """Main entry point for the application."""
    # Create and initialize controller
    controller = ModbusController()
    
    # Add sample devices
    controller.add_sample_devices()
    
    # Print devices
    print()
    controller.device_manager.print_devices()
    print()
    
    # Run for 5 seconds for demonstration
    controller.run(duration=5)


if __name__ == "__main__":
    main()
