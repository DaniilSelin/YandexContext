b, c = map(int, input().split(" "))
r, d = map(int, input().split(" "))

count = 0
z = b * (10 ** 6) + c

while z >= r:
    k = c // r
    if k > 0:
        d += k * r
        c -= k * r
        z -= k * r
        count += k
    else:
        t = r // (10 ** 6)
        if b >= t:
            k0 = t * (10 ** 6) + c
            r0 = r % (10 ** 6)
            if k0 >= r:
                if c >= r0:
                    b -= t
                    c -= r0
                    d += r0
                    count += 1
            else:
                k0 = (t + 1) * (10 ** 6)
                if b < t + 1:
                    break
                elif k0 - r <= d:
                    b -= t + 1
                    d -= k0 - r
                    c += k0 - r
                    count += 1
                else:
                    break
    z = b * (10 ** 6) + c
print(count)