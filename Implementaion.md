# Implementation
## Alex Wu

## Explain
1. **Explain why programmers use stubs.**

Programmers use stubs to test the code without fully completeing the implementation of the program.

2. **Explain why version control is important.**

Version is important as it has multiple benefits. These include allowing multiple collaborators to work on the same thing, being able to backup and restore different versions, tracking the history of the files, being able to make branches for things without affecting the main files, as well as letting the branches merge back into the main program once finished.

3. **Explain code optimisation in software engineering.**

Code optimisation is making a program run faster by doing things such as rewriting the code to make it smaller, removing useless parts, resulting in better performance aspects such as reducing memory usage.

4. **Explain how the following systems handle message passing (complete (a) and (b))**
a:
```
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other_player, damage):
        print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        other_player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}'s health is now {self.health}")


# Create two Player objects
alice = Player("Alice", 100)
bob = Player("Bob", 100)

# One player sends a message (method call) to another
alice.attack(bob, 25)
```

b:
```
class Chest:
    def __init__(self, gold_amount):
        self.gold_amount = gold_amount
        self.is_open = False

    def open(self, player):
        if not self.is_open:
            print(f"{player.name} opens the chest and finds {self.gold_amount} gold!")
            player.collect_gold(self.gold_amount)
            self.is_open = True
        else:
            print("The chest is already empty.")

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0

    def open_chest(self, chest):
        chest.open(self)  # Message passing: player sends message to chest

    def collect_gold(self, amount):
        self.gold += amount
        print(f"{self.name} now has {self.gold} gold.")


# Creating objects
player = Player("Lara")
treasure_chest = Chest(50)

# Interactions using message passing
player.open_chest(treasure_chest)   # Lara opens chest, chest gives her gold
player.open_chest(treasure_chest)   # Trying to open again
```

5. **Optimise the code in these examples**