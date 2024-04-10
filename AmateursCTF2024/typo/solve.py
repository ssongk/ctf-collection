import random as my_random
seed = int('1665663c', 20)
my_random.seed(seed)
result = bytearray(bytes.fromhex(open('output.txt', 'r').read()))

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
right = lambda byte_arr: bytearray([_byte_arr - 1 for _byte_arr in byte_arr])
left = lambda byte_arr: bytearray([_byte_arr + 1 for _byte_arr in byte_arr])

def func(hex):
    for list in range(1, len(hex) - 1, 2):
        hex[list], hex[list + 1] = hex[list + 1], hex[list]
    for id in range(0, len(hex) - 1, 2):
        hex[id], hex[id + 1] = hex[id + 1], hex[id]
    return hex

tmp = [func, right, left]
tmp = [my_random.choice(tmp) for _byte_arr in range(128)]

def my_random(arr, ar):
    for r in ar:
        arr = tmp[r](arr)
    return arr

def hex_to_base17(hex_val):
    decimal_value = hex_val
    base17_str = ""
    while decimal_value > 0:
        remainder = decimal_value % 17
        base17_str = hex(remainder)[2:] + base17_str
        decimal_value //= 17
    return base17_str

def func(arr, ar):
    ar = int(ar.hex(), 16)
    for r in arr:
        ar -= int(r, 35)
    return hex_to_base17(ar)

result = func(byte_rrr, result)
result = bytearray(bytes.fromhex(result))
result = my_random(result, rrr.encode())
print(result)