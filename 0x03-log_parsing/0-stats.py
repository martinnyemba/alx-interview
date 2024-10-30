#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys


def print_stats(total_size, cache):
    """Print the computed statistics"""
    print('File size: {}'.format(total_size))
    for key in sorted(cache.keys()):
        if cache[key] != 0:
            print('{}: {}'.format(key, value))


# Initialize variables
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        
        try:
            # Split the line and verify format
            line_list = line.split()
            if len(line_list) < 7:  # Check minimum required fields
                continue
                
            # Extract status code and file size from their correct positions
            status_code = line_list[-2]
            file_size = line_list[-1]
            
            # Validate and process status code
            if status_code in cache:
                cache[status_code] += 1
                
            # Validate and add file size
            total_size += int(file_size)
            
            # Print stats every 10 valid lines
            if counter % 10 == 0:
                print_stats(total_size, cache)
                
        except (IndexError, ValueError):
            # Skip lines that don't match the required format
            continue

except KeyboardInterrupt:
    # Handle CTRL+C gracefully
    print_stats(total_size, cache)
    raise

# Print final stats
print_stats(total_size, cache)
