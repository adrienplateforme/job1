x = 1
y = 1
mod = 0

while x < 1000:
    x = x + 1
    y = 1
    mod = 0

    while x >= y:
        if x % y == 0:
            mod = mod + 1
            y = y + 1
        else:
            y = y + 1
    if mod == 2:
        print(x)