print(n,(lambda n:'H'if 1 in[n]+[n:=sum(int(i)**2for i in list(str(n)))for _ in range(n+1)]else'U')(n))
