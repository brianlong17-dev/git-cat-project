import random
import string
print("hello world")
name = "Brian"
# No changes needed to this section

def randomName():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    return random.choice(names)

randomNameL = lambda: random.choice(["Johny", "Saraho", "Mikey", "Emma", "David"])


name = randomName()
print("hello world", randomNameL())