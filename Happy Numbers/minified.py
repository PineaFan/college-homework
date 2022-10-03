for n in range(30):print(n,(lambda n:f"{'H'if 1 in [n]+[n:=sum(int(i)**2 for i in list(str(n)))for _ in range(n+1)]else'U'}")(n))
