import random
import time
from matplotlib import pyplot
import json


def int_to_money(amount):
    return f"£{round(abs(amount)/100, 2):.2f}"



class Machine:
    def __init__(self):
        self.icons = {
            0: "🍒",
            1: "🔔",
            2: "🍋",
            3: "🍊",
            4: "⭐",
            5: "💀"
        }
        self.cash = 100

    def _roll(self):
        return [random.randint(0, 5) for _ in range(3)]

    def _reward(self, roll):
        def double_reward(roll):
            if roll == 5:
                return -100
            return 50
        if roll[0] == roll[1] == roll[2]:
            if roll[0] == 1:
                return 500
            if roll[0] == 5:
                return -self.cash
            return 100
        for n in range(3):
            if roll[n] == roll[(n + 1) % 3]:
                return double_reward(roll[n])
        return 0

    def play(self, auto: bool = False):
        if auto:
            roll = self._roll()
            reward = self._reward(roll)
            self.cash += reward - 20
            return True
        print(f"\033[92mYou have {int_to_money(self.cash)}\033[0m")
        i = input("[Q]uit or [Enter] to play: ")
        if i.lower() == "q":
            return False
        self.cash -= 20
        print("\n"*50)
        print("Rolling...")
        roll = self._roll()
        reward = self._reward(roll)
        self.cash += reward
        time.sleep(1)
        print(f"You rolled {self.icons[roll[0]]} {self.icons[roll[1]]} {self.icons[roll[2]]}")
        if reward > 0:
            print(f"\033[92mYou won {int_to_money(reward)}\033[0m")
        elif reward < 0:
            print(f"\033[91mYou lost {int_to_money(reward)}\033[0m")
        else:
            print("\033[33mYou gained no coins\033[0m")
        print("-" * 20)
        return True


def controlled():
    played = 0
    total_rounds = 0
    while True:
        game = Machine()
        rounds = 0
        while game.cash > 0:
            rounds += 1
            if not game.play():
                break
        else:
            print("\033[91mYou are out of money.")
        print(f"You left with {int_to_money(game.cash)}")
        played += 1
        total_rounds += rounds
        if total_rounds % 10000 == 0:
            print(f"Played {played} games with {total_rounds} rounds, average {total_rounds/played} rounds per game")


def auto() -> int:
    game = Machine()
    rounds = 0
    while game.cash > 0:
        rounds += 1
        if not game.play(auto=True):
            break
    return rounds


def generateGraph(plot, report):
    # Generates a graph which updates every time a game is played
    # The bar graph shows the counts of each game length
    lengths = {}
    if plot:
        plt = pyplot
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel("Rounds")
        ax.set_ylabel("Games")
        ax.set_title("Slot Machine")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.grid()

    count = 0
    while True:
        length = auto()
        if length in lengths:
            lengths[length] += 1
        else:
            lengths[length] = 1
        count += 1

        if count % 10000 == 0:
            if report:
                with open("lengths.json", "w") as f:
                    json.dump(dict(sorted(lengths.items())), f, indent=4)
            if plot:
                ax.clear()
                ax.set_xlim(0, max(lengths.keys()) + 10)
                ax.set_ylim(0, max(lengths.values()) + 10)
                ax.grid()
                ax.bar(lengths.keys(), lengths.values(), width=1, align="edge")

                ax.text(0.5, 0.9, f"Simulations: {count}", transform=ax.transAxes)
                ax.text(0.5, 0.85, f"Mean: {sum([a * b for a, b in lengths.items()]) / sum(lengths.values())}", transform=ax.transAxes)
                ax.text(0.5, 0.8, f"Mode: {lengths[max(lengths, key=lengths.get)]}", transform=ax.transAxes)
                ax.text(0.5, 0.75, f"Max: {max(lengths.keys())}", transform=ax.transAxes)

                x = list(range(1, max(lengths.keys()) + 1))
                y = [(a ** -1.5) * count for a in x]
                ax.plot(x, y, color="red")

                fig.canvas.draw()
                fig.canvas.flush_events()

# generateGraph(True, False)
controlled()
