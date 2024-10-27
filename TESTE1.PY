import random
count = 0

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]
row = spin_row()
for x in range(2000):
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    x=[random.choice(symbols) for _ in range(3)]
    row = spin_row()
    print(row)
    
    if row[0] == row[1] == row[2]:
        count += 1

print(count)
        