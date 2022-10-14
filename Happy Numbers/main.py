happy = 0
n = 1
while happy < 8:
    history = [n]
    while len(history) == len(set(history)):
        n = sum(int(i)**2 for i in str(n))
        history += [n]
    if 1 in history:
        print(f"{history[0]} Happy")
        happy += 1
    n = history[0] + 1
