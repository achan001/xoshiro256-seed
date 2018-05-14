import sys, z3
bit64 = 0xffffffffffffffff

def LShL(x, n): return (x << n) & bit64
def LShR(x, n): return (x >> n)

def xoshiro256(s, LShR = LShR): # inplace update
    t = LShL(s[1], 17)
    s[2] ^= s[0]
    s[3] ^= s[1]
    s[1] ^= s[2]
    s[0] ^= s[3]
    s[2] ^= t
    s[3] = LShL(s[3],45) | LShR(s[3],19)

def scramble(s, func, LShR = LShR):
    if func == '+': return (s[0] + s[3]) & bit64
    t = (s[1] * 5) & bit64      # ** scrambler
    t = LShL(t,7) | LShR(t,57)  # = rotl(s[1] * 5, 7) * 9
    return (t * 9) & bit64

func = sys.argv[1]              # '+' = plus scrambler
if func not in ('+', '**'):     # '**' = mul-rotate-mul
    print 'Unknown scrambler'
    sys.exit()

if sys.argv[2] == 'seed':       # usage xo256.py func seed x0 x1 x2 x3
    x = [int(sys.argv[i], 0) for i in range(3,7)]
    for i in range(10):         # generate random numbers
        print '0x%x' % scramble(x, func)
        xoshiro256(x)
    sys.exit()

x0, x1, x2, x3 = z3.BitVecs('x0 x1 x2 x3', 64)
x = [x0, x1, x2, x3]            # mutable state, allow update
s = z3.SimpleSolver()

for v in sys.argv[2:]:          # usage xo256.py func seq1 seq2 seq3 ...
    s.add(scramble(x, func, z3.LShR) == int(v, 0))
    xoshiro256(x, z3.LShR)

for i in xrange(1, sys.maxint):
    print '\n#%d = %s' % (i, s.check())
    if s.check().r != 1: break  # quit if failed
    soln = s.model()
    x = [soln[i].as_long() for i in (x0,x1,x2,x3)]
    print 'seed = 0x%016x,%016x,%016x,%016x' % tuple(x)
    for j in range(10):         # show predictions
        print '0x%x' % scramble(x, func)
        xoshiro256(x)
    s.add(z3.Or(x0 != soln[x0], # look for next soln
                x1 != soln[x1],
                x2 != soln[x2],
                x3 != soln[x3]))
