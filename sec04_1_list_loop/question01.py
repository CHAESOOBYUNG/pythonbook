list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
print(list_a)

list_b = [0, 1, 2, 3, 4, 5, 6, 7]
list_b.append(10)
print(list_b)

list_c = [0, 1, 2, 3, 4, 5, 6, 7]
list_c.insert(3, 0)
print(list_c)

list_d = [0, 1, 2, 3, 4, 5, 6, 7]
list_d.remove(3)
print(list_d)

list_e = [0, 1, 2, 3, 4, 5, 6, 7]
list_e.pop(3)
print(list_e)

list_f = [0, 1, 2, 3, 4, 5, 6, 7]
list_f.clear()
print(list_f)