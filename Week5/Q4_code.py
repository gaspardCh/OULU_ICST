import argparse
import subprocess
import re

def ping_device(target):
    command = f"ping -c 4 {target}"
    
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {target}\n{e.output.decode()}")

def validate_ip_address(ip):
    # Regular expression pattern for IPv4 address
    ipv4_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    # Regular expression pattern for IPv6 address
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:?([0-9a-fA-F]{1,4}:)?(:[0-9a-fA-F]{1,4}){1,7}$|^(([0-9a-fA-F]{1,4}:){1,7}|:)(:[0-9a-fA-F]{1,4}){1,7}$"
    
    # Check if input matches either IPv4 or IPv6 pattern
    if re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip):
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description="Ping a device. WARNING: This tool is vulnerable to command injection.")
    parser.add_argument("target", type=str, help="IP address or DNS name of the target device")
    args = parser.parse_args()
    if validate_ip_address(args.target):
        ping_device(args.target)
    else:
        print("Invalid ip address")

if __name__ == "__main__":
    main()

