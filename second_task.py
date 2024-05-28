from itertools import combinations

def Up(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def Down(l):
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False
    return True

n = int(input())
l = list(map(int, input().split(" ")))

comb1 = []
for k in range(2, n + 1):
    for el in combinations(l, k):
        comb1.append(el)
comb2 = [x for x in comb1]

i = 0
while i < len(comb1):
    if not Up(comb1[i]):
        comb1.remove(comb1[i])
    else:
        i += 1
i = 0
while i < len(comb2):
    if not Down(comb2[i]):
        comb2.remove(comb2[i])
    else:
        i += 1

comb1 = comb1[::-1]
comb2 = comb2[::-1]

fl = 0
NVP = []
NUP = []
for el1 in comb1:
    for el2 in comb2:
        f = 0
        for k in el1:
            if k in el2:
                f = 1
                break
        if f:
            continue
        else:
            NVP.append(list(el1))
            NUP.append(list(el2))

if NVP:
    if len(NVP) == 1:
        print(len(NVP[0]))
        NVP_ind = []
        for el in NVP[0]:
            NVP_ind.append(l.index(el) + 1)
        print(*NVP_ind)
        print(len(NUP[0]))
        NUP_ind = []
        for el in NUP[0]:
            NUP_ind.append(l.index(el) + 1)
        print(*NUP_ind)
    else:
        if len(NVP[0]) > len(NUP[1]):
            print(len(NVP[0]))
            NVP_ind = []
            for el in NVP[0]:
                NVP_ind.append(l.index(el) + 1)
            print(*NVP_ind)
            print(len(NUP[0]))
            NUP_ind = []
            for el in NUP[0]:
                NUP_ind.append(l.index(el) + 1)
            print(*NUP_ind)
        else:
            max_len = []
            for i in range(len(NVP)):
                max_len = len(NVP[i]) + len(NUP[i])
            k = max_len.index(max(max_len))
            print(len(NVP[k]))
            NVP_ind = []
            for el in NVP[k]:
                NVP_ind.append(l.index(el) + 1)
            print(*NVP_ind)
            print(len(NUP[k]))
            NUP_ind = []
            for el in NUP[k]:
                NUP_ind.append(l.index(el) + 1)
            print(*NUP_ind)
else:
    print("IMPOSSIBLE")