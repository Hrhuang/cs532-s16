
readfile = open('relations.txt', 'r')
readfile2 = open('mainfollowers.txt', 'r')
savefile = open('sorceData.json', 'a')

savefile.write('{')
savefile.write('\n')
savefile.write('  "nodes":[')
savefile.write('\n')

for line in readfile2:

	savefile.write('    {"name":"')
	savefile.write(line.strip())
	savefile.write('","group":1},')
	savefile.write('\n')

savefile.write('  ],')
savefile.write('\n')
savefile.write('  "links":[')
savefile.write('\n')

for line in readfile:
	elements = line.split(',')
	savefile.write('    {"source":')
	savefile.write('"')
	savefile.write(elements[0])
	savefile.write('",')
	savefile.write('"target":')
	savefile.write('"')
	savefile.write(elements[1])
	savefile.write('",')
	savefile.write('"value":')
	savefile.write(elements[2].strip())
	savefile.write('},')
	savefile.write('\n')

savefile.write('  ]')
savefile.write('\n')
savefile.write('}')

