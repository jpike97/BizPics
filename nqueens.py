numqueen = int(input("Enter num queens: "))

board = [[0 for x in range(numqueen)] for y in range(numqueen)]
row = 0
column = 0


def placeQueens(theboard, row, column):
	while (column < numqueen):
		theboard[row][column] = 1
		print(theboard)
		if check(theboard, row, column) == 1:
			print("worked")
			column += 1
		else:
			theboard[row][column] = 0
			row += 1
			if column == 0:
				column += 1
	print("the board is: ")
	print(theboard)


def check(boardCheck, row, column):
	count = 0
	count2 = 0
	#check horizontal and vertical
	for j in range(0, numqueen):
		count = count + boardCheck[row][j]
		if count > 1:
			return 0
		count2 = count2 + boardCheck[j][column]
		if count2 > 1:
			return 0

	return 1


print(placeQueens(board, row, column))
