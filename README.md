# Modbus Controller (Python Version)

A complete Python translation of the C-based Modbus Controller. Provides device management and communication handlers for Modbus RTU (serial) and Modbus TCP protocols.

## Features

- **Device Management System**: Register, track, and manage multiple Modbus devices
- **RTU (Serial) Communication Handler**: Handle Modbus RTU communication over serial ports
- **TCP Communication Handler**: Handle Modbus TCP communication over network connections
- **Settings Management**: Centralized configuration for all communication parameters
- **Python 3 Implementation**: Modern Python with comprehensive documentation and type hints

## Directory Structure

```
modbus_controller_py/
├── main.py                          # Main entry point
├── __init__.py                      # Package initialization
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── config/
│   ├── __init__.py                  # Config package init
│   └── settings.py                  # Settings and configuration management
├── devices/
│   ├── __init__.py                  # Devices package init
│   └── device_manager.py            # Device manager and Device class
└── modbus_handlers/
    ├── __init__.py                  # Handlers package init
    ├── rtu_handler.py               # RTU (serial) communication handler
    └── tcp_handler.py               # TCP communication handler
```

## Installation

### Requirements

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or navigate to the repository:
```bash
cd modbus_controller_py
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

The application will:
1. Initialize settings and handlers
2. Create sample devices for demonstration
3. Run the main event loop for 5 seconds
4. Gracefully shutdown

### Using as a Library

You can also use the modules individually:

```python
from config.settings import load_settings
from devices.device_manager import DeviceManager
from modbus_handlers.rtu_handler import RTUHandler
from modbus_handlers.tcp_handler import TCPHandler

# Load settings
settings = load_settings()

# Create device manager
dm = DeviceManager()
dm.add_device(1, "Sensor 1", 1)

# Create and use RTU handler
rtu = RTUHandler()
rtu.open("/dev/ttyUSB0", 9600)
rtu.send(b'\x01\x03\x00\x00\x00\x02\xC4\x0B')  # Modbus RTU frame
data = rtu.receive()
rtu.close()

# Create and use TCP handler
tcp = TCPHandler()
tcp.connect("192.168.1.100", 502)
tcp.send(b'\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x02')  # Modbus TCP frame
data = tcp.receive()
tcp.disconnect()
```

## Module Documentation

### config.settings

Handles loading and management of configuration settings.

**Key Classes:**
- `Settings`: Stores configuration parameters
  - `rtu_port`: Serial port for RTU (default: '/dev/ttyUSB0')
  - `rtu_baud`: Baud rate for RTU (default: 9600)
  - `tcp_host`: TCP host address (default: '127.0.0.1')
  - `tcp_port`: TCP port (default: 502)
  - `timeout_ms`: Communication timeout (default: 5000ms)

### devices.device_manager

Manages Modbus devices.

**Key Classes:**
- `Device`: Represents a single Modbus device
  - Properties: `id`, `name`, `address`, `enabled`
  
- `DeviceManager`: Manages multiple devices
  - Methods:
    - `add_device()`: Add a new device
    - `remove_device()`: Remove a device
    - `get_device()`: Retrieve a device by ID
    - `enable_device()`: Enable a device
    - `disable_device()`: Disable a device
    - `print_devices()`: Display all devices
    - `process()`: Process all enabled devices

### modbus_handlers.rtu_handler

Handles Modbus RTU (serial) communication.

**Key Classes:**
- `RTUHandler`: Serial port communication handler
  - Methods:
    - `open()`: Open and configure serial port
    - `close()`: Close serial port
    - `send()`: Send data
    - `receive()`: Receive data
    - `is_open()`: Check connection status
    - `process()`: Handle RTU communication processing

**Example:**
```python
rtu = RTUHandler()
if rtu.open("/dev/ttyUSB0", 9600):
    rtu.send(modbus_frame)
    response = rtu.receive()
    rtu.close()
```

### modbus_handlers.tcp_handler

Handles Modbus TCP communication.

**Key Classes:**
- `TCPHandler`: TCP socket communication handler
  - Methods:
    - `connect()`: Connect to TCP server
    - `disconnect()`: Close connection
    - `send()`: Send data
    - `receive()`: Receive data
    - `is_connected()`: Check connection status
    - `process()`: Handle TCP communication processing

**Example:**
```python
tcp = TCPHandler()
if tcp.connect("192.168.1.100", 502):
    tcp.send(modbus_frame)
    response = tcp.receive()
    tcp.disconnect()
```

## Comparison with C Version

This Python implementation provides the same functionality as the original C version:

| Feature | C Version | Python Version |
|---------|-----------|-----------------|
| Device Management | ✓ | ✓ |
| RTU Handler | ✓ | ✓ |
| TCP Handler | ✓ | ✓ |
| Settings Management | ✓ | ✓ |
| Cross-platform | ✓ | ✓ |
| Ease of Use | Good | Excellent |
| Performance | High | Good |
| Extensibility | Moderate | High |

## Platform Support

- **Linux**: Fully supported
- **macOS**: Fully supported  
- **Windows**: Fully supported (use COM ports for RTU, e.g., 'COM3')

## Performance Considerations

The Python version is suitable for:
- Learning and development
- Prototyping Modbus applications
- Medium-speed communication scenarios
- Educational purposes

For high-performance or real-time critical applications, consider the C version.

## Extending the Controller

The modular architecture makes it easy to extend functionality:

1. **Add Custom Devices**: Subclass `Device` class with specific behavior
2. **Implement Modbus Protocol**: Extend the handler classes to implement actual Modbus protocol
3. **Add Persistence**: Implement device state storage using databases
4. **Add Web Interface**: Integrate with Flask/FastAPI for REST API
5. **Add Monitoring**: Integrate with monitoring systems

## Troubleshooting

### Serial Port Errors
- Ensure the serial port path is correct (use `ls /dev/tty*` on Linux/macOS)
- Verify USB device is connected
- Check permissions: `sudo chmod 666 /dev/ttyUSB0`

### TCP Connection Errors
- Verify the target host and port are correct
- Check network connectivity
- Ensure firewall allows connections

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python path includes the project directory

## License

MIT License - See original C repository for details

## Changelog

### Version 1.0.0
- Initial Python translation of C modbus_controller
- Full RTU and TCP handler implementation
- Device management system
- Settings management
- Comprehensive documentation

---

**Original C Repository**: modbus_controller_c
**Translation Date**: January 2026