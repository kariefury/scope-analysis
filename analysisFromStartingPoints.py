import matplotlib.pyplot as plt

lengthOfWire = "1pt15"
fname = "/Volumes/PENNY/0xFF00_"+lengthOfWire+"AllWaveforms.csv"
finame = "/Volumes/PENNY/0xFF00_"+lengthOfWire+"_hightolowC1.csv"
saveName = "/Volumes/PENNY/0xFF00_"+lengthOfWire+"_decoded_values.csv"
fileSpot = "/Volumes/PENNY/splitData/"+lengthOfWire+"/"

with open(finame) as f:
	indices =  [index.rstrip('\n') for index in f]

with open(fname) as f:
	lines = [line.rstrip('\n') for line in f]

saveFile = open(saveName, 'w')

print len(lines)
print lines[0]
print lines[1]
print lines[2]
print lines[3]
print lines[4]
print lines[5]
print lines[6]
print lines[7]
print lines[8]
print lines[9]
print lines[10]
print lines[11]
print lines[12]
print lines[13]
print lines[14]
print lines[15]
print lines[16]
print lines[17]
print lines[18]
print lines[19]
print lines[20]
print lines[21]
print lines[22]


data_chunks = []
chunk_size = 2000
i = 0
while i < len(indices):
	try:
		data_chunks.append(lines[int(indices[i])-chunk_size:int(indices[i])+chunk_size+chunk_size])
	except:
		pass
	i += 8

x_vals = []
y_vals_channel_1 = []
y_vals_channel_2 = []

print 'number of chunks of data ',  len(data_chunks)
i = 0
j = 0


while j < len(data_chunks):
#while j < 50:
	x_vals = []
	y_vals_channel_1 = []
	y_vals_channel_2 = []
	c1_binary = []
	c2_binary = []
	tFile = open(fileSpot+str(j)+".csv", 'w')
	for each in data_chunks[j]:
		tFile.write(each)
		s = each.strip().split(",")
		try:
			if len(s) == 3:
				x_vals.append(s[0])
				if float(s[1]) > 0.2:
					c1_binary.append(1)
				else:
					c1_binary.append(0)

				if float(s[2]) > 0.2:
					c2_binary.append(1)	
				else:
					c2_binary.append(0)
				
				y_vals_channel_1.append(s[1])
				y_vals_channel_2.append(s[2])
		except:
			pass
	j += 1
	tFile.close()
	print c1_binary
	#print len(x_vals)
	#print len(y_vals_channel_2)
	#print len(y_vals_channel_1)
	#plt.plot(x_vals,c1_binary,x_vals,c2_binary,x_vals,y_vals_channel_1,x_vals,y_vals_channel_2)
	#plt.show()

	i = 0
	x_count = len(x_vals)
	c1_start = c1_binary[0]
	c2_start = c2_binary[0]
	c1_pause = 0
	c2_pause = 0
	decoded_value = []

	while i < x_count:
		if c1_binary[i] != c1_start:
			print 'Channel 1 switch at count ', c1_pause
			if c1_start == 0:
				print 'switch c1 low to high'
				print 'indices from j range ', j
				decoded_value.append('1')
			else:
				print 'switch c1 high to low'
			c1_start = c1_binary[i]
			c1_pause = 0
		else:
			c1_pause += 1
		if c2_binary[i] != c2_start:
			print 'Channel 2 switch at count ', c2_pause
			if c2_start == 0:
				print 'switch c2 low to high'
				decoded_value.append('0')
			else:
				print 'switch c1 high to low'
			c2_start = c2_binary[i]
			c2_pause = 0
		else:
			c2_pause += 1
		i += 1

	decoded_value.append('\n')
	str_dec = ''.join(decoded_value)
	print str_dec
	saveFile.write(str_dec)
	print 'data batch Done'
print "complete"