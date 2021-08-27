list = [' ','A',' ','B',' ','C',' ','D',' ','E']
for x in range(0,5):
    print("".join(str(x) for x in list))
    del list[-1]
    del list[-1]