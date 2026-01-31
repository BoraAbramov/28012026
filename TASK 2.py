
while True:
    _min = int(input("please enter a number: "))
    _max = int(input("please enter a higher number: "))
    if _max <= _min:
        continue
    else:
        for i in range(_min, _max + 1):
            print(i)
        break