def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif. Persamaan tidak mempunyai akar real."
    return  "determinan positif. Persamaan mempunyai akar real."
print(selesaikanABC(1,2,3))
