# Development Guide - Modbus Controller (Python)

## Development Setup

### Clone Repository
```bash
cd /path/to/modbus_controller_py
```

### Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Optional Development Dependencies
```bash
pip install pytest pytest-cov black flake8 mypy
```

## Project Structure

```
modbus_controller_py/
├── main.py                    # Application entry point
├── __init__.py                # Package init
├── README.md                  # User documentation
├── DEVELOPMENT.md             # This file
├── requirements.txt           # Runtime dependencies
│
├── config/                    # Configuration module
│   ├── __init__.py
│   └── settings.py            # Settings class and functions
│
├── devices/                   # Device management module
│   ├── __init__.py
│   └── device_manager.py      # Device and DeviceManager classes
│
├── modbus_handlers/           # Modbus protocol handlers
│   ├── __init__.py
│   ├── rtu_handler.py         # RTU (serial) handler
│   └── tcp_handler.py         # TCP network handler
│
└── tests/                     # Unit tests (optional)
    ├── __init__.py
    ├── test_settings.py
    ├── test_device_manager.py
    ├── test_rtu_handler.py
    └── test_tcp_handler.py
```

## Running the Application

```bash
python main.py
```

## Code Style

This project follows PEP 8 standards. Use the following tools:

### Format Code
```bash
black .
```

### Check Code Quality
```bash
flake8 .
```

### Type Checking
```bash
mypy .
```

## Writing Tests

Create tests in the `tests/` directory:

```python
# tests/test_device_manager.py
import unittest
from devices.device_manager import Device, DeviceManager

class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.manager = DeviceManager()
    
    def test_add_device(self):
        result = self.manager.add_device(1, "Test Device", 1)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.devices), 1)
    
    def test_get_device(self):
        self.manager.add_device(1, "Test Device", 1)
        device = self.manager.get_device(1)
        self.assertIsNotNone(device)
        self.assertEqual(device.name, "Test Device")

if __name__ == '__main__':
    unittest.main()
```

## Running Tests

```bash
python -m pytest
python -m pytest --cov=.  # With coverage
```

## Module Responsibilities

### config/settings.py
- Loads configuration parameters
- Provides Settings class for accessing configuration
- Default values for RTU and TCP communication

### devices/device_manager.py
- Device class for representing Modbus devices
- DeviceManager class for managing multiple devices
- Add/remove/enable/disable device operations
- Device listing and processing

### modbus_handlers/rtu_handler.py
- RTUHandler class for serial port communication
- Open/close serial connections
- Send/receive data over serial
- Configuration of serial parameters (baud rate, parity, etc.)

### modbus_handlers/tcp_handler.py
- TCPHandler class for network socket communication
- Connect/disconnect to TCP servers
- Send/receive data over TCP
- Socket timeout configuration

## Extending the Project

### Adding New Protocol Handler
1. Create new handler file in `modbus_handlers/`
2. Implement handler class with open/close/send/receive methods
3. Integrate in main.py

### Example: Custom Handler
```python
# modbus_handlers/custom_handler.py
class CustomHandler:
    def __init__(self):
        self.initialized = False
    
    def open(self, **kwargs):
        print("[CustomHandler] Opening...")
        self.initialized = True
    
    def close(self):
        print("[CustomHandler] Closing...")
        self.initialized = False
    
    def send(self, data):
        if not self.initialized:
            print("[CustomHandler] Error: Not initialized")
            return -1
        # Implementation
        return len(data)
    
    def receive(self):
        if not self.initialized:
            print("[CustomHandler] Error: Not initialized")
            return b''
        # Implementation
        return b''
    
    def process(self):
        if self.initialized:
            # Process communications
            pass
```

### Adding Configuration File Support
Extend `config/settings.py` to load from JSON/YAML:

```python
import json

class Settings:
    def load_from_file(self, filepath):
        with open(filepath, 'r') as f:
            config = json.load(f)
        self.rtu_port = config.get('rtu_port', '/dev/ttyUSB0')
        self.rtu_baud = config.get('rtu_baud', 9600)
        # ... other settings
```

## Debugging

### Enable Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Add Debug Output
```python
print(f"[ModuleDebug] Variable: {var}")
logger.debug(f"Debug message: {info}")
```

### Common Issues

**Issue: Serial port not found**
- Check port name: `ls /dev/tty*` (Linux/macOS)
- Verify device permissions
- Use correct port name for your platform

**Issue: TCP connection refused**
- Verify server is running
- Check host and port are correct
- Ensure firewall allows connection

**Issue: Import errors**
- Verify Python path includes project directory
- Check __init__.py files exist in packages
- Run `pip install -r requirements.txt`

## Performance Optimization

### For Better Performance:
1. Add connection pooling
2. Implement caching
3. Use threading/async for concurrent operations
4. Optimize serial communication timing
5. Batch device processing

### Example: Async Version
```python
import asyncio

async def process_device_async(device):
    await asyncio.sleep(0.1)
    # Process device

async def main():
    tasks = [process_device_async(d) for d in devices]
    await asyncio.gather(*tasks)
```

## Documentation

### Docstring Format (Google Style)
```python
def function(param1, param2):
    """Brief description.
    
    Longer description if needed.
    
    Args:
        param1 (type): Description
        param2 (type): Description
    
    Returns:
        type: Description
    
    Raises:
        ExceptionType: Description
    """
    pass
```

## Release Checklist

- [ ] Update version in __init__.py
- [ ] Update CHANGELOG
- [ ] Run all tests
- [ ] Check code coverage
- [ ] Update README
- [ ] Tag release in git

---

For questions or issues, please refer to README.md or the individual module documentation.
