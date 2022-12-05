d = open('input.txt', 'r')
max = [0, 0, 0]
cur = 0

lines = d.readlines()

for line in lines:
	if(line == "\n"):
		
		if(cur > max[0]):
			max[2] = max[1]
			max[1] = max[0]
			max[0] = cur
		elif(cur > max[1]):
			max[2] = max[1]
			max[1] = cur
		elif(cur > max[2]):
			max[2] = cur
		cur = 0
	else:
		cur += int(line)


print("Highest: " + str(max[0]) + "\nSum of three highest: " + str(sum(max)))