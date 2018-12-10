N=input();exec("min(map(lambda x: 'impossible' if x[0]/x[1] > 1 else x[0]/x[1] ,zip(sorted(map(float,raw_input().split())),range(1,N+1))))")
