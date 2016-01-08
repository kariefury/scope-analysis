import matplotlib.pyplot as plt

lengthOfWire = ["0pt15"]

k = 0
spacing = []
while k < len(lengthOfWire):
	spacing.append([])
	fname = "/Volumes/PENNY/"+lengthOfWire[k]+"_counter.csv"
	finame = "/Volumes/PENNY/counter_"+lengthOfWire[k]+"_hightolowC1.csv"
	sname = "/Volumes/PENNY/counter_"+lengthOfWire[k]+"_chunkStarts.csv"
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
			outFile.write(indices[i+1] + '\n')
		spacing[k].append(space)
		i += 1

	plt.hist(spacing[k], 50, normed=1, facecolor='green', alpha=0.75)
	plt.show()
	k += 1
