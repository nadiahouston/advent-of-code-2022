score = 0
resultScores = [3, 6, 0] # Points scored for [draw, win, loss]

for line in open('input.txt'):
	
	oppo = ord(line[0]) - 65 # 1, 2, 3 for Rock, Paper, Scissors
	""" Part 1
	your = ord(line[2]) - 87 # 1, 2, 3 for Rock, Paper, Scissors	
	result = (your - oppo) % 3 # 0, 1, 2 for draw, win, loss
	"""
	# Part 2
	result = (ord(line[2]) - 89) % 3 # 0, 1, 2 for draw, win, loss
	your = (oppo + result) % 3 + 1	# 1, 2, 3 for Rock, Paper Scissors
	
	score += your
	score += resultScores[result]
	
print("Score: " + str(score))
