lengths = [1,3,5,8,10,12,15]
total = 0
for i in range(len(lengths)):
    total += sum(lengths[:i])
    print(i, lengths[:i], sum(lengths[:i]))
print(total)