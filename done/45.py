import time

def tri_gen():
    n = 1
    while True:
        yield int(n*(n+1)/2)
        n += 1

def pent_gen():
    n = 1
    while True:
        yield int(n*(3*n-1)/2)
        n += 1

def hex_gen():
    n = 1
    while True:
        yield int(n*(2*n-1))
        n += 1

def main():
    start = time.time()
    t = tri_gen()
    p = pent_gen()
    h = hex_gen()
    for _ in range(285):
        next(t)
    for _ in range(165):
        next(p)
    for _ in range(143):
        next(h)

    while True:
        goal = next(h)
        pent = next(p)
        tri = next(t)
        while pent < goal:
            pent = next(p)
        if pent == goal:
            while tri < goal:
                tri = next(t)
            if tri == goal:
                print(f"Answer is {goal}")
                print(f"Time: {time.time() - start} seconds.")
                return

main()
# 1533776805
# 0.06 seconds
# 5/31/2018