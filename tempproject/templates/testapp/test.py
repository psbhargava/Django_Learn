l = [1,2,3,4,1,2,3,4,5]
d = {}
for i in l:
    if i not in d.keys():
        d[i] = [i]
    else:
        d[i].append(i)

print(list(d.values()))
