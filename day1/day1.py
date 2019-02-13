#!/usr/bin/env python3

with open("input.txt") as f:
    input_data = f.read()

frequency = 0
frequencies = {0}
duplicate = False
first_iter = True
while not duplicate:
    for line in input_data.splitlines():
       frequency += int(line)
       if frequency not in frequencies:
           frequencies.add(frequency)
       elif not duplicate:
            first_duplicate = frequency
            duplicate = True
            if not first_iter:
                break
    if first_iter:
        first_iter = False
        print(frequency)
print(first_duplicate)
