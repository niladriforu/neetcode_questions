import ctypes

# Example value
x = 42

# Get the memory address of x
address = id(x)

# Dereference the memory address to get the value
value = ctypes.cast(address, ctypes.py_object).value

print("Memory address:", hex(address))
print("Value at memory address:", value)

x = 50
address1 = id(x)
value1 = ctypes.cast(address1, ctypes.py_object).value

print("Memory address:", hex(address1))
print("Value at memory address:", value1)

y = 82
address2 = id(y)
value2 = ctypes.cast(address2, ctypes.py_object).value

print("Memory address:", hex(address2))
print("Value at memory address:", value2)

