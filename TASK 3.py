
# start

i = 0
_count = 0


# count 10 loops

for _ in range(10):
    _age = int(input("please enter player age: "))
    if _age < 12:
        continue
    if _age > 18:
        print("illegal age")
        break
    i += 1
    if _age >= 16:
        _count += 1

print("total count:", i, "players above age 16:", _count)

# stop