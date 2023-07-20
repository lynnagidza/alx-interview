#!/usr/bin/env python3
"""Log Parsing"""

import sys

def print_stats(total_file_size, status_codes):
    """Prints the stats"""
    print("File size:", total_file_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """Main function"""
    total_file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for idx, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            parts = line.split()

            if len(parts) != 7:
                continue

            _, _, _, status_code_str, file_size_str = parts

            try:
                status_code = int(status_code_str)
                file_size = int(file_size_str)
            except ValueError:
                continue

            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if idx % 10 == 0:
                print_stats(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_codes)

if __name__ == "__main__":
    main()
