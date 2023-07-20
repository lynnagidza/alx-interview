 #!/usr/bin/python3
"""Log Parsing"""
import sys


def print_stats(status_codes, file_size):
    """Prints the statistics"""
    print(f"File size: {file_size}")
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    counter = 0
    try:
        for line in sys.stdin:
            args = line.split()
            if len(args) > 2:
                file_size += int(args[-1])
                if args[-2] in status_codes:
                    status_codes[args[-2]] += 1
                counter += 1
                if counter % 10 == 0:
                    print_stats(status_codes, file_size)
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
