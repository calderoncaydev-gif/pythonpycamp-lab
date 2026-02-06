"""
06_loops.py
-----------
Bucles en Python.
"""

# for
for i in range(5):
    print(i)

# for con rango
for i in range(1, 6):
    print(i)

# for con step
for i in range(0, 10, 2):
    print(i)

# while
count = 0
while count < 3:
    print(count)
    count += 1

# break y continue
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)
