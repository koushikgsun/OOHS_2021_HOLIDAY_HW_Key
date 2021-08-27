f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def s(m):
    n = str(m)
    sa = 0
    for i in range (len(n)):
        sa += f[ord(n[i]) - ord('0')]
    if sa == m:
       return True
    else:
       return False
def p(m):
    for i in range (1, m + 1):
        if (s(i)):
            print (i, end = " \n")
if True:
    m = int(input('number : '))
    p(m)