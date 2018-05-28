'''
Usage: splitmix seed [index]
Example:
> splitmix.py 0xffff  # no index = solve
0x02799f3b140b6d37 -> 0x000000000000ffff

> splitmix.py 0x02799f3b140b6d37 0
0x02799f3b140b6d37 -> 0x000000000000ffff

> splitmix.py 0x02799f3b140b6d37 1
0xa0b118f49355e94c -> 0x4a8893a266c24be8

> splitmix.py 0xa0b118f49355e94c -1
0x02799f3b140b6d37 -> 0x000000000000ffff
'''

bit64 = 0xffffffffffffffff
step  = 0x9e3779b97f4a7c15

def splitmix(x):
    z = (x + step) & bit64
    z = ((z ^ (z >> 30)) * 0xbf58476d1ce4e5b9) & bit64
    z = ((z ^ (z >> 27)) * 0x94d049bb133111eb) & bit64
    return z ^ (z >> 31)

def unsplitmix(z):
    z ^= (z >> 31) ^ (z >> 62)              # undo scrambler
    z = (z * 0x319642b2d24d8ec3) & bit64
    z ^= (z >> 27) ^ (z >> 54)
    z = (z * 0x96de1b173f119089) & bit64
    z ^= (z >> 30) ^ (z >> 60)
    return (z - step) & bit64               # undo step

if __name__ == '__main__':                  # splitmix solver
    import sys
    try:
        seed = int(sys.argv[1], 0) & bit64
        try: seed = (seed + int(sys.argv[2]) * step) & bit64
        except IndexError: seed = unsplitmix(seed)
    except:
        print __doc__
    else:
        print '0x%016x -> 0x%016x' % (seed, splitmix(seed))
