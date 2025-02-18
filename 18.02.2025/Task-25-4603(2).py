from fnmatch import fnmatch

for i in range(141, 10**8,141 ):
    if i % 141 == 0:
        print(i,i//141)
