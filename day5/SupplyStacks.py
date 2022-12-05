import re

stacks = ['HCR',
		  'BJHLSF',
		  'RMDHJTQ',
		  'SGRHZBJ',
		  'RPFZTDCB',
		  'THCG',
		  'SNVZBPWL',
	 	  'RJQGC',
	 	  'LDTRHPFS']		  
		 
def move1(num, source, dest):
	for i in range(num):
		dest += source[-1]
		source = source[:-1]
	return source, dest
	
def move2(num, source, dest):
	dest += source[-num:]
	source = source[:-num]
	return source, dest

p = re.compile(r"move (\d+) from (\d+) to (\d+)")

for line in open('input.txt'):
	result = p.match(line)
	if result:
		num, source, dest = int(result[1]), int(result[2])-1, int(result[3])-1
		stacks[source], stacks[dest] = move2(num, stacks[source], stacks[dest])

output = ''

for string in stacks:
	output += string[len(string)-1]
	
print(output)
