for n in range(30):print(n,(lambda n:'H'if 1in[n:=sum(int(i)**2for i in list(str(n)))for _ in range(n)]else'U')(n))
