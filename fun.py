def sort_a_line(a):
    for i in a:
        int(i)
    return a.sort()

i = [x for int(x) in input()]

print(i)
print(sort_a_line(i))