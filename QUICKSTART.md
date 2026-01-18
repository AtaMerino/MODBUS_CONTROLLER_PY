# Quick Start Guide - Modbus Controller Python

## Installation (2 minutes)

```bash
# 1. Navigate to project directory
cd modbus_controller_py

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Running the Demo (1 minute)

```bash
python main.py
```

Expected output:
- Initialization messages
- 3 sample devices created
- Event loop running for 5 seconds
- Graceful shutdown

## Basic Usage Examples

### Example 1: Using the Device Manager

```python
from devices.device_manager import DeviceManager

# Create manager
manager = DeviceManager()

# Add devices
manager.add_device(1, "Sensor A", 1)
manager.add_device(2, "Sensor B", 2)

# Display all devices
manager.print_devices()

# Get specific device
device = manager.get_device(1)
print(f"Found: {device.name}")

# Enable/disable devices
manager.disable_device(1)
manager.enable_device(1)
```

### Example 2: Serial Communication (RTU)

```python
from modbus_handlers.rtu_handler import RTUHandler

# Create handler
rtu = RTUHandler()

# Open serial port
if rtu.open("/dev/ttyUSB0", 9600):
    # Send Modbus RTU frame (example)
    frame = bytes([0x01, 0x03, 0x00, 0x00, 0x00, 0x02, 0xC4, 0x0B])
    rtu.send(frame)
    
    # Receive response
    response = rtu.receive()
    print(f"Received: {response.hex()}")
    
    # Close port
    rtu.close()
else:
    print("Failed to open serial port")
```

### Example 3: TCP Communication

```python
from modbus_handlers.tcp_handler import TCPHandler

# Create handler
tcp = TCPHandler()

# Connect to server
if tcp.connect("192.168.1.100", 502):
    # Send Modbus TCP frame (example)
    frame = bytes([0x00, 0x01, 0x00, 0x00, 0x00, 0x06, 
                   0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
    tcp.send(frame)
    
    # Receive response
    response = tcp.receive()
    print(f"Received: {response.hex()}")
    
    # Disconnect
    tcp.disconnect()
else:
    print("Failed to connect")
```

### Example 4: Using Settings

```python
from config.settings import load_settings

# Load settings
settings = load_settings()

# Access settings
print(f"RTU Port: {settings.rtu_port}")
print(f"RTU Baud: {settings.rtu_baud}")
print(f"TCP Host: {settings.tcp_host}")
print(f"TCP Port: {settings.tcp_port}")
```

### Example 5: Complete Application

```python
from config.settings import load_settings
from devices.device_manager import DeviceManager
from modbus_handlers.rtu_handler import RTUHandler
from modbus_handlers.tcp_handler import TCPHandler
import time

# Initialize
settings = load_settings()
device_manager = DeviceManager()
rtu = RTUHandler()
tcp = TCPHandler()

# Setup
device_manager.add_device(1, "Device 1", 1)
rtu.open(settings.rtu_port, settings.rtu_baud)
tcp.connect(settings.tcp_host, settings.tcp_port)

# Main loop
try:
    for i in range(10):
        device_manager.process()
        rtu.process()
        tcp.process()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Interrupted")
finally:
    # Cleanup
    rtu.close()
    tcp.disconnect()
```

## File Organization

```
modbus_controller_py/
├── main.py                    # Run this to see demo
├── README.md                  # Full documentation
├── DEVELOPMENT.md             # Development guide
├── requirements.txt           # Dependencies
├── config/
│   └── settings.py           # Configuration
├── devices/
│   └── device_manager.py     # Device management
└── modbus_handlers/
    ├── rtu_handler.py        # Serial communication
    └── tcp_handler.py        # Network communication
```

## Common Tasks

### Task 1: Add a New Device
```python
from devices.device_manager import DeviceManager

manager = DeviceManager()
manager.add_device(10, "New Device", 10)
manager.print_devices()
```

### Task 2: Send Serial Data
```python
from modbus_handlers.rtu_handler import RTUHandler

rtu = RTUHandler()
if rtu.open("COM3", 9600):  # Windows
    rtu.send(b'\x01\x03\x00\x00\x00\x02\xC4\x0B')
    response = rtu.receive(256)
    rtu.close()
```

### Task 3: Connect to TCP Server
```python
from modbus_handlers.tcp_handler import TCPHandler

tcp = TCPHandler()
if tcp.connect("192.168.1.1", 502):
    tcp.send(b'...your data...')
    data = tcp.receive()
    tcp.disconnect()
```

### Task 4: Check Device Status
```python
from devices.device_manager import DeviceManager

manager = DeviceManager()
manager.add_device(1, "Device 1", 1)

device = manager.get_device(1)
if device:
    print(f"Status: {'Enabled' if device.enabled else 'Disabled'}")
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'serial'"
```bash
# Install pyserial
pip install pyserial
```

### "Cannot open port /dev/ttyUSB0"
```bash
# Check available ports
ls /dev/tty*

# Fix permissions (Linux)
sudo chmod 666 /dev/ttyUSB0
```

### "Connection refused" for TCP
```bash
# Check if server is running at the specified address/port
netstat -tuln | grep 502
```

## Next Steps

1. **Read Full Documentation**: Open `README.md`
2. **Learn Development**: Check `DEVELOPMENT.md`
3. **Explore Code**: Start with `main.py`
4. **Integrate**: Use the modules in your project
5. **Extend**: Create custom handlers and devices

## API Reference

### Settings
- `Settings.rtu_port` - Serial port path
- `Settings.rtu_baud` - Baud rate
- `Settings.tcp_host` - TCP host
- `Settings.tcp_port` - TCP port
- `Settings.timeout_ms` - Timeout

### Device
- `Device.id` - Device identifier
- `Device.name` - Device name
- `Device.address` - Modbus address
- `Device.enabled` - Active status

### DeviceManager
- `add_device(id, name, address)` - Add device
- `remove_device(id)` - Remove device
- `get_device(id)` - Find device
- `enable_device(id)` - Enable device
- `disable_device(id)` - Disable device
- `print_devices()` - Display all

### RTUHandler
- `open(port, baud)` - Open serial port
- `close()` - Close port
- `send(data)` - Send bytes
- `receive(max_len)` - Get response
- `is_open()` - Check status

### TCPHandler
- `connect(host, port)` - Connect
- `disconnect()` - Disconnect
- `send(data)` - Send bytes
- `receive(max_len)` - Get response
- `is_connected()` - Check status

---

**For more information**: See README.md
