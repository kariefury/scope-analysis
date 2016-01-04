import matplotlib.pyplot as plt

fname = "/Volumes/PENNY/0xFF00_0pt5AllWaveforms.csv"
with open(fname) as f:
	lines = [line.rstrip('\n') for line in f]

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
#i = 1022
i = 222977
chunk_size = 7000
while i < len(lines):
	try:
		data_chunks.append(lines[i:i+chunk_size-1])
	except:
		pass
	i = i + chunk_size

x_vals = []
y_vals_channel_1 = []
y_vals_channel_2 = []

print 'number of chunks of data ',  len(data_chunks)
i = 0

#while i < len(data_chunks):
while i < 4:
	x_vals = []
	y_vals_channel_1 = []
	y_vals_channel_2 = []
	c1_binary = []
	c2_binary = []
	for each in data_chunks[i]:
		s = each.strip().split(",")
		#print s
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
	i += 1
	print len(x_vals)
	print len(y_vals_channel_2)
	print len(y_vals_channel_1)
	plt.plot(x_vals,c1_binary,x_vals,c2_binary,x_vals,y_vals_channel_1,x_vals,y_vals_channel_2)
	plt.show()

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
			decoded_value.append(1)
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
			decoded_value.append(0)
		else:
			print 'switch c1 high to low'
		c2_start = c2_binary[i]
		c2_pause = 0
	else:
		c2_pause += 1
	i += 1

print decoded_value
print len(decoded_value)

print "complete"