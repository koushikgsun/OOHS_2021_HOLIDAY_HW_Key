for no in range(100, 1001):
   o = len(str(no))
   z = 0
   te = no
   while te > 99:
       di = te % 10
       z += di ** o
       te //= 10

   if no == z:
       print(no)