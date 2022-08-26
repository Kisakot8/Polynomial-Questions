debug = False

from random import sample, choice

def polynomial():
    # m = multiplier & fac = factor (eg 2x-1 has a multiplier of 2 and a factor of -1)
    facs = sample([-3,-2,-1,1,2,3],3)

    ms = sample([-3,-2,-1,1,2,3],3)

    bi = [ms[0]*ms[1], (facs[0]*ms[1]) + (facs[1]*ms[0]), facs[0]*facs[1]]
    a, b, c = bi
    x, y = ms[2], facs[2]

    poly = [a*x, (b*x) + (a*y), (c*x) + (b*y), c*y]

    syms = ["", "+", "+", "+"]
    for i, n in enumerate(poly):
        if n < 0:
            syms[i] = "-"
            poly[i] = int(str(poly[i])[1:])

        if poly[i] == 1:
            poly[i] = ""

    if debug:
        print(poly)
        print(str(bi[0]) + "x² + " + str(bi[1]) + "x + " + str(bi[2]))
        print(f"({ms[0]}x+{facs[0]})({ms[1]}x+{facs[1]})({ms[2]}x+{facs[2]})")

    if choice([True, False]):
        qsym = ""
        if facs[0] > 0:
            qsym = "+"
        question = f"Prove that {ms[0]}x{qsym}{facs[0]} is a factor of f(x)."
        parta, partb = "a. ", "\nb. Factorise f(x) fully."
    
    else:
        qsym = ""
        if facs[0] > 0:
            qsym = "+"
        question = f"Prove that {ms[0]-choice([-3,-2,-1,1,2,3])}x{qsym}{facs[0]-choice([-3,-2,-1,1,2,3])} is NOT a factor of f(x)."
        parta, partb = "", ""

    print(f"""f(x) = {syms[0]}{poly[0]}x³ {syms[1]} {poly[1]}x² {syms[2]} {poly[2]}x {syms[3]} {poly[3]}
{parta}{question}{partb}""")

polynomial()
