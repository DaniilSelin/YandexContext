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
        if b > 0:
            k0 = (10 ** 6) + c
            if c == 0:
                #  and (2 * k0) // r > 0 and b >= 2 and ((2 * k0) - r) <= d
                t = (r // (10 ** 6)) + 1
                if (t * k0) // r > 0 and b >= t and ((t * k0) - r) <= d:
                    b -= t
                    d -= t * k0 - r
                    c += t * k0 - r
                    count += 1
                # print(b, c, d, count)
            elif (r // (10 ** 6)) > 1:
                t = (r // (10 ** 6)) + 1
                if (t * (10 ** 6) + c) // r > 0 and b >= t and (t * (10 ** 6) + c - r) <= d:
                    b -= t
                    d -= t * (10 ** 6) + c - r
                    c += t * (10 ** 6) + c - r
                    count += 1
                pass
            elif k0 // r > 0 and k0 - r <= d and c <= r % (10 ** 6):
                b -= 1
                d -= k0 - r
                c += k0 - r
                if not (k0 - r):
                    d += c
                    c = 0
                count += 1
            elif k0 // r > 0 and c > r % (10 ** 6):
                b -= 1
                d += r % (10 ** 6)
                c -= r % (10 ** 6)
                count += 1
            else:
                break
            pass
    z = b * (10 ** 6) + c
    # print(b, c, d, count)

print(count)