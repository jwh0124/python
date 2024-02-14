pi = [3, ".", 1, 4, 1, 5, 9]

print(pi.pop(1))
print(pi)
print(pi.pop())
print(pi)
print(pi.pop())
print(pi)

cities = "서울,대전,대구,부산,제주"
cities_sort = cities.split(",")
cities_sort.sort()
print(cities_sort)

def is_permutation(l1, l2):
    l1.sort()
    l2.sort()
    return l1 == l2

print(is_permutation([1,2,3], [3,1,2]))
print(is_permutation([1,1,1,2], [1,2,1,1]))
print(is_permutation([1,2,3,1], [1,2,3]))

def replace(d, v, e):
    for i in d:
        if d[i] == v :
            d[i] = e
    
    return d

print(replace({1:2, 3:4, 4:2}, 2, 7))
print(replace({1:2, 3:1, 4:2}, 1, 2))
            
