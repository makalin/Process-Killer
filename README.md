# Process Killer

A command-line tool to search and kill processes by partial name match. This Python script provides a simple and safe way to find and terminate processes matching a specified pattern.

## Features

- Case-insensitive partial name matching
- Lists matching processes with PID, name, and username before killing
- Interactive confirmation prompt (can be bypassed)
- Force kill option (SIGKILL)
- Detailed operation summary
- Error handling and access checking

## Requirements

- Python 3.6 or higher
- psutil library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/makalin/Process-Killer.git
cd Process-Killer
```

2. Install the required dependency:
```bash
pip install psutil
```

3. Make the script executable (Unix-like systems):
```bash
chmod +x process_killer.py
```

## Usage

Basic syntax:
```bash
python process_killer.py PATTERN [options]
```

### Options

- `-f, --force`: Use SIGKILL instead of SIGTERM for force killing processes
- `-y, --yes`: Skip the confirmation prompt
- `-h, --help`: Show help message

### Examples

Find and kill processes containing "firefox":
```bash
python process_killer.py firefox
```

Force kill processes containing "chrome" without confirmation:
```bash
python process_killer.py chrome -f -y
```

## Sample Output

```
Matching processes:
PID      Name                 User
----------------------------------------
1234     firefox.exe          user
5678     firefox-bin          user

Kill 2 matching process(es)? (y/N): y
Successfully killed process 1234 (firefox.exe)
Successfully killed process 5678 (firefox-bin)

Summary: 2 process(es) killed, 0 failed
```

## Exit Codes

- 0: Success
- 1: One or more processes failed to be killed
- 2: Invalid command line arguments

## Security Considerations

- The script only attempts to kill processes that the current user has permission to terminate
- A confirmation prompt is shown by default to prevent accidental termination
- Process information is retrieved safely using psutil's error-handled methods

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [psutil](https://github.com/giampaolo/psutil) library for process management
- Inspired by the need for a safer alternative to `killall` and `taskkill`

## Support

If you encounter any issues or have questions, please file an issue in the GitHub repository.
