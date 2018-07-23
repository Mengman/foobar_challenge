import sys

def gen_prime():
    """
    prime number generator
    """
    yield 2
    yield 3
    D = {}

    def set_next_m(c, s):
        m = c + s
        while m in D:
            m += s
        D[m] = s

    ps = gen_prime()
    c = p = next(ps) and next(ps)
    q = p * p

    while True:
        c += 2
        if c in D:
            set_next_m(c, D.pop(c))
        else:
            if c != q:
                yield c
            else:
                set_next_m(c, p + p)
                p = next(ps)
                q = p * p


def gen_prime_str(length):
    prime_str = ""
    size = 0
    ps = gen_prime()

    while size < length:
        prime = next(ps)
        p_str = str(prime)
        size += len(p_str)
        prime_str += p_str

    return prime_str


def answer(n):
    return gen_prime_str(n+5)[n:n+5]

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(answer(n))