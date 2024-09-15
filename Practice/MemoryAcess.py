from ctypes import string_at
from sys import getsizeof

a = 0x000000245a9ff78f
print(string_at(id(a),getsizeof(a)).hex() , " ")