
#start

_index = 0 # indexer
x = None #variable

while True: #endless loop
    _num = int(input("Enter a number: "))
    if _index == 0: #saves first number
        x = _num
        _index += 1
        continue
    if _index == 2: #break loop when reached goal
        break
    if _num > x: #second loop check if num higher then privous
        x = _num
        _index += 1
        continue
    else: # else drop the indexer
        _index = 0

