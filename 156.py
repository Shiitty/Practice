def winPercentage(board):
	maxX = len(board[0])-1
	maxY = len(board)-1
	win = 0
	lost = 0
	for (y,row) in enumerate(board):
		for (x, char) in enumerate(row):
			if char == 'B':
				lost += 1
			#	print str(x)+','+str(y)+'is B\n'
				continue
			if y>0:
				if board[y-1][x] =='B':
			#		print str(x)+','+str(y)+'up is B\n'
					continue
				if x>0:
					if board[y-1][x-1] == 'B':
			#			print str(x)+','+str(y)+'left up is B\n'
						continue
				if x<maxX:
					if board[y-1][x+1] == 'B':
			#			print str(x)+','+str(y)+'right up is B\n'
						continue
			if y<maxY:
				if board[y+1][x] == 'B':
			#		print str(x)+','+str(y)+'bottom is B\n'
					continue
				if x>0:
					if board[y+1][x-1]=='B':
			#			print str(x)+','+str(y)+'left bottom is B\n'
						continue
				if x<maxX:
					if board[y+1][x+1]=='B':
			#			print str(x)+','+str(y)+'right bottom is B\n'
						continue
			if x>0:
				if board[y][x-1] == 'B':
			#		print str(x)+','+str(y)+'left is B\n'
					continue
			if x<maxX:
				if board[y][x+1] == 'B':
			#		print str(x)+','+str(y)+'right is B\n'
					continue
			#print str(x)+','+str(y) + 'a good one \n'
			win += 1
	result = float(win)/float(win+lost)
	return result
print winPercentage([".....", ".....", "..B..", ".....", "....."])
print winPercentage(["BBBBB", "B...B", "B...B", "B...B", "BBBBB"])
print winPercentage([".........", ".B..B..B.", ".........", ".........", ".B..B..B.", ".........", ".........", ".B..B..B.", "........."])
print winPercentage([".........................", ".........................", ".........................", "........................."])
print winPercentage(["......B.......B..B...........................B....",
 "..............B..................BB..B............",
 "B.B.B.............B.....B..............B..........",
 "...................B...B....................BB....",
 "...B.....B.........................B.......B.....B",
 "B.B.........B.....B.......B..B......B.B...B.BB....",
 "..B...................BB...............B..........",
 ".........B...B................B..B................",
 ".......BB.......B....B................B.....BBB...",
 ".......BB..........B..............B......BB.......",
 "...................BB.....................B.......",
 "...B.B.B......B..............B...B......B.........",
 "B................B................................",
 "....B..........B.....B..BB....B...............BB..",
 "..B....B.....B.............B.....B............B...",
 "...................B.B........B..B.........B.B....",
 ".....B.....B......................................",
 "...........BB......BB...B.B........B...B..........",
 ".....BBB..........................................",
 ".B...........B....B...BB......B......B...B.B......",
 "..................B........BB................B....",
 "...............................B..B....BBB.B....B.",
 "..........B.......................................",
 ".....B..........B....BB......B.B......B......B....",
 ".....B..................B........B................",
 "............B.....B..B....BB...B....BB........B...",
 "..B.................B.........B...................",
 ".BB..............B................................",
 "...B....B..................B.................B....",
 "......B...B......B......................B.B.......",
 "..............B..................B.......B........",
 ".....B........BB...B.....B........................",
 ".......B......B.B..B..........B...........B....B..",
 "B...B...........B...B...B......B.B...B..B......B..",
 "....B..B.....B.B.......BB..B............B.B....B..",
 "B.......B..........B.........B...B.BB......B......",
 "....B...............................B.............",
 ".....B.B..........................................",
 "..........B............B......B.B..B....B.........",
 "....B...B.......................B.................",
 "B.................B...........B..B....B...........",
 "...B.....B........................................",
 "...B..B......................................BBB..",
 ".B...B....................................B....B..",
 "...B...B..........B...B.B.........................",
 ".....B.............B...BB..........B..BBB.BB......",
 "....................B.....B.......................",
 "........B..BB..........B.B....B...........B......B",
 ".........B.....BB..B.............B....BB..........",
 "....B..B..............B...B..B..........B........."])