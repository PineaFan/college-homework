for n in range(0, 8 + 1):
    history = [n]
    while len(history) == len(set(history)):
        n = sum(int(i)**2 for i in list(str(n)))
        history += [n]
    print(f"{history[0]}: {'Happy' if 1 in history else 'Unhappy'}")
