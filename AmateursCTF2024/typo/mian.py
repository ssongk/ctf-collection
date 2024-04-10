import random as my_random
seed = int('1665663c', 20)
my_random.seed(seed)
flag = bytearray(open('flag.txt', 'rb').read())
rrr = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'
byte_rrr = [
    b'arRRrrRRrRRrRRrRr',
    b'aRrRrrRRrRr',
    b'arRRrrRRrRRrRr',
    b'arRRrRrRRrRr',
    b'arRRrRRrRrrRRrRR'
    b'arRRrrRRrRRRrRRrRr',
    b'arRRrrRRrRRRrRr',
    b'arRRrrRRrRRRrRr'
    b'arRrRrRrRRRrrRrrrR',
]
right = lambda byte_arr: bytearray([_byte_arr + 1 for _byte_arr in byte_arr])
left = lambda byte_arr: bytearray([_byte_arr - 1 for _byte_arr in byte_arr])

def func(hex):
    print(hex)
    for id in range(0, len(hex) - 1, 2):
        hex[id], hex[id + 1] = hex[id + 1], hex[id]
    print(hex)
    
    for list in range(1, len(hex) - 1, 2):
        hex[list], hex[list + 1] = hex[list + 1], hex[list]
    print(hex)
    
    return hex

tmp = [func, right, left]
tmp = [my_random.choice(tmp) for _byte_arr in range(128)]

def my_random(arr, ar):
    for r in ar:
        arr = tmp[r](arr)
    return arr

def func(arr, ar):
    ar = int(ar.hex(), 17)
    for r in arr:
        ar += int(r, 35)
    return bytes.fromhex(hex(ar)[2:])

result = my_random(flag, rrr.encode())
result = func(byte_rrr, result)
print(result)
# print(result.hex())