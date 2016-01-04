import matplotlib.pyplot as plt

lengthOfWire = ["0pt15","0pt5","0pt9","1pt15"]

k = 0
spacing = []
while k < len(lengthOfWire):
	spacing.append([])
	fname = "/Volumes/PENNY/0xFF00_"+lengthOfWire[k]+"AllWaveforms.csv"
	finame = "/Volumes/PENNY/0xFF00_"+lengthOfWire[k]+"_hightolowC1.csv"
	sname = "/Volumes/PENNY/0xFF00_"+lengthOfWire[k]+"_chunkStarts.csv"
	with open(finame) as f:
		indices =  [index.rstrip('\n') for index in f]
	
	outFile = open(sname, "w")
	i = 0
	average = 0
	while i < len(indices)-1:
		space = int(indices[i+1]) - int(indices[i])
		if (space > 200) and (space < 10000):
			print k , i, space
		if space > 10000:
			spacing[k].append(space)
			outFile.write(indices[i+1] + '\n')
		i += 1

	plt.hist(spacing[k], 50, normed=1, facecolor='green', alpha=0.75)
	plt.show()
	k += 1
