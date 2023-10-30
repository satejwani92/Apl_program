s = {'a','b','c','d'}
# add
s.add('e')
print(s)

#discard
s.discard('b')
print(s)

#remove
s.remove('c')
print(s)

#pop
s.pop()
print(s)

#clear
s.clear()
print(s)

#another set function
s1 = {1,2,3}
s2 = {2,3,4}

#intersection
print(s1.intersection(s2))

#union
print(s1.union(s2))

#symmetric_difference
print(s1.symmetric_difference(s2))

#update
s1.update(s2)
print(s2)
l1 = [1,2,3,4]
s1 = set(l1)
print(s1)