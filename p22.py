"""Names scores"""

with open("names.txt") as f:
    names = f.read().translate(None, '"').lower().split(',')

sorted_names = sorted(names)
res = 0
substract = ord('a') - 1
for index, name in enumerate(sorted_names, start=1):
    res += sum(ord(i)-substract for i in name) * index
print res
