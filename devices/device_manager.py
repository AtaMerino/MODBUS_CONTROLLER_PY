"""Device manager module for Modbus Controller.

This module handles device registration, storage, and processing.
"""


class Device:
    """Represents a Modbus device.
    
    Attributes:
        id (int): Unique device identifier
        name (str): Human-readable device name
        address (int): Modbus address of the device
        enabled (bool): Whether the device is active
    """
    
    def __init__(self, device_id, name, address):
        """Initialize a device.
        
        Args:
            device_id (int): Unique device identifier
            name (str): Human-readable device name
            address (int): Modbus address of the device
        """
        self.id = device_id
        self.name = name
        self.address = address
        self.enabled = True
    
    def __repr__(self):
        """Return string representation of device."""
        return (
            f"Device(id={self.id}, name={self.name}, "
            f"address={self.address}, enabled={self.enabled})"
        )


class DeviceManager:
    """Manages multiple Modbus devices.
    
    Attributes:
        devices (list): List of Device objects
        max_devices (int): Maximum number of devices allowed
    """
    
    MAX_DEVICES = 100
    
    def __init__(self):
        """Initialize device manager."""
        self.devices = []
        print("[DeviceManager] Initialized")
    
    def add_device(self, device_id, name, address):
        """Add a new device to the manager.
        
        Args:
            device_id (int): Unique device identifier
            name (str): Human-readable device name
            address (int): Modbus address of the device
            
        Returns:
            bool: True if device added successfully, False if max reached
        """
        if len(self.devices) >= self.MAX_DEVICES:
            print("[DeviceManager] Error: Maximum devices reached")
            return False
        
        device = Device(device_id, name, address)
        self.devices.append(device)
        print(
            f"[DeviceManager] Added device: {name} "
            f"(ID: {device_id}, Address: {address})"
        )
        return True
    
    def remove_device(self, device_id):
        """Remove a device from the manager.
        
        Args:
            device_id (int): ID of device to remove
            
        Returns:
            bool: True if device removed, False if not found
        """
        for device in self.devices:
            if device.id == device_id:
                self.devices.remove(device)
                print(f"[DeviceManager] Removed device: {device.name} (ID: {device_id})")
                return True
        print(f"[DeviceManager] Device not found: ID {device_id}")
        return False
    
    def get_device(self, device_id):
        """Get a device by ID.
        
        Args:
            device_id (int): ID of device to retrieve
            
        Returns:
            Device: Device object if found, None otherwise
        """
        for device in self.devices:
            if device.id == device_id:
                return device
        return None
    
    def process(self):
        """Process all enabled devices.
        
        Iterates through devices and processes those that are enabled.
        """
        for device in self.devices:
            if device.enabled:
                # Process device
                pass
                # Uncomment for debugging:
                # print(f"[DeviceManager] Processing: {device.name}")
    
    def print_devices(self):
        """Print information about all managed devices."""
        print(f"[DeviceManager] Total devices: {len(self.devices)}")
        for device in self.devices:
            enabled_str = "Yes" if device.enabled else "No"
            print(
                f"  Device {device.id}: {device.name} "
                f"(Address: {device.address}, Enabled: {enabled_str})"
            )
    
    def enable_device(self, device_id):
        """Enable a device.
        
        Args:
            device_id (int): ID of device to enable
            
        Returns:
            bool: True if successful, False if device not found
        """
        device = self.get_device(device_id)
        if device:
            device.enabled = True
            print(f"[DeviceManager] Enabled device: {device.name}")
            return True
        return False
    
    def disable_device(self, device_id):
        """Disable a device.
        
        Args:
            device_id (int): ID of device to disable
            
        Returns:
            bool: True if successful, False if device not found
        """
        device = self.get_device(device_id)
        if device:
            device.enabled = False
            print(f"[DeviceManager] Disabled device: {device.name}")
            return True
        return False
