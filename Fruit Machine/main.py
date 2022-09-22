import random
import time


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

    def play(self):
        print(f"\033[92mYou have {int_to_money(self.cash)}\033[0m")
        i = input("[Q]uit or [Enter] to play: ")
        if i.lower() == "q":
            return False
        self.cash -= 20
        print("\n"*10)
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


game = Machine()
while game.cash > 0:
    if not game.play():
        break
else:
    print("\033[91mYou are out of money")
    print("Game over")
    exit()
print(f"You left with £{int_to_money(game.cash)}")

