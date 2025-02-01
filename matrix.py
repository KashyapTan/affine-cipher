    def euclidean_gcd(x, y):
        r = x % y
        while r != 0:
            q = x // y
            r = x % y
            print(f"{x} = {y} * {q} + {r}")
            x = y
            y = r
        print(f"GCD = {x}")
        return r

    euclidean_gcd(356519, 114151)