# 0x03-log_parsing

'Log Parsing'

## Description
This project implements a log parsing script in Python that reads from standard input (stdin) line by line and computes metrics. The script processes log entries in a specific format and generates statistical summaries of the processed data.

## Project Information
- **Language**: Python
- **Project Directory**: 0x03-log_parsing

## Technical Concepts
- File I/O Operations
- Signal Handling (CTRL + C)
- Real-time Data Processing
- Regular Expressions
- Dictionary Operations
- Exception Handling

## Requirements

### General
- **Python Version**: 3.4.3
- **Operating System**: Ubuntu 20.04 LTS
- **Style Guide**: PEP 8 (version 1.7.x)
- **File Endings**: All files must end with a newline
- **Shebang Line**: First line must be exactly `#!/usr/bin/python3`
- **Documentation**: README.md file is mandatory
- **File Permissions**: All files must be executable

### Allowed Editors
- vi
- vim
- emacs

## Task: Log Parsing

### Input Format
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
- Lines not matching this format must be skipped

### Output Requirements
The script must print statistics after every 10 lines and/or keyboard interruption (CTRL + C):

1. **Total File Size**:
   ```
   File size: <total size>
   ```
   Where `<total size>` is the sum of all previous file sizes

2. **Status Code Statistics**:
   - Print number of lines by status code in ascending order
   - Only print status codes: 200, 301, 400, 401, 403, 404, 405, and 500
   - Format: `<status code>: <number>`
   - Skip status codes that don't appear or aren't integers

### Example Usage
```bash
./0-generator.py | ./0-stats.py 
```

Sample Output:
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

### Implementation Files
- **Script File**: `0-stats.py`
- **Test Generator**: `0-generator.py` (provided for testing)

## Testing
The length of files will be tested using the `wc` command. The script should handle interruption gracefully and print final statistics when interrupted with CTRL + C.

## Repository Information
- **GitHub Repository**: alx-interview
- **Directory**: 0x03-log_parsing
- **Main File**: 0-stats.py

## License
Copyright © 2024 ALX, All rights reserved.


## Example in detail

    alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
    #!/usr/bin/python3
    import random
    import sys
    from time import sleep
    import datetime

    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
        sys.stdout.flush()

    alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    ^CFile size: 17146
    200: 4
    301: 3
    400: 4
    401: 2
    403: 6
    404: 6
    405: 4
    500: 4
    Traceback (most recent call last):
    File "./0-stats.py", line 15, in <module>
    Traceback (most recent call last):
    File "./0-generator.py", line 8, in <module>
        for line in sys.stdin:
    KeyboardInterrupt
        sleep(random.random())
    KeyboardInterrupt
    alexa@ubuntu:~/0x03-log_parsing$ 
