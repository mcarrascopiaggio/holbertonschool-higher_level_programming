#!/usr/bin/python3
for fn in range(9):
    for sc in range(10):
        if fn >= sc or (fn == 8 and sc == 9):
            continue
        else:
            print(f"{fn}{sc}, ", end="")
print(89)
