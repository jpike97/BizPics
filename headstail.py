import random
win = 0
lose = 0

for x in range(0, 1000):
	flip = random.randint(1, 100)
	if flip > 49:
		win += 1
	else:
		lose += 1

print("Wins is: " + str(win))
print("Losses is:  " + str(lose))
print("net gain/loss is: $" + str((win - lose) * 100))
