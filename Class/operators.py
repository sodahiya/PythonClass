
# 1. Arithmetic Operators
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# 2. Relational (Comparison) Operators
x = 10
y = 20

print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# 3. Assignment Operators
x = 5
print(f"Initial value: x = {x}")

x += 3
print(f"x += 3: {x}")

x -= 2
print(f"x -= 2: {x}")

x *= 4
print(f"x *= 4: {x}")

x /= 2
print(f"x /= 2: {x}")

x %= 3
print(f"x %= 3: {x}")

x **= 2
print(f"x **= 2: {x}")

x //= 2
print(f"x //= 2: {x}")

# 4. Logical Operators
p = True
q = False

print(f"{p} and {q}: {p and q}")
print(f"{p} or {q}: {p or q}")
print(f"not {p}: {not p}")

# 5. Bitwise Operators
m = 5  # 0b0101
n = 3  # 0b0011

print(f"Bitwise AND: {m} & {n} = {m & n}")
print(f"Bitwise OR: {m} | {n} = {m | n}")
print(f"Bitwise XOR: {m} ^ {n} = {m ^ n}")
print(f"Bitwise NOT: ~{m} = {~m}")
print(f"Bitwise Left Shift: {m} << 1 = {m << 1}")
print(f"Bitwise Right Shift: {m} >> 1 = {m >> 1}")

# 6. Ternary Operator (Conditional Expression)
a = 10
b = 20
min_value = a if a < b else b
print(f"Ternary Operator: min_value = {min_value}")

# 7. Membership Operators
numbers = [1, 2, 3, 4, 5]

print(f"3 in numbers: {3 in numbers}")
print(f"6 not in numbers: {6 not in numbers}")

# 8. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b: {a is b}")  # True, both refer to the same object
print(f"a is c: {a is c}")  # False, different objects with the same content
print(f"a is not c: {a is not c}")  # True
