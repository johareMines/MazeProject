discovered = set()

tuple = ('a', 'b', 'c', ('d', 'e'))
discovered.add(tuple)


tupleTriple = ('a', 'b', 'c')

if any(t[:3] == tupleTriple for t in discovered):
    print(t)
    print("Yes")
else:
    print("no")