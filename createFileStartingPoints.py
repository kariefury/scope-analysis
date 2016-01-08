import matplotlib.pyplot as plt

lengthOfWire = ["0pt15"]


q = 0
while q < len(lengthOfWire):

	fname = "/Volumes/PENNY/"+lengthOfWire[q]+"_counter.csv"
	#fname = "/Volumes/PENNY/0xFF00_"+lengthOfWire[q]+"AllWaveforms.csv"
	saveName = "/Volumes/PENNY/counter_"+lengthOfWire[q]+"_hightolowC1.csv"

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

	c1_indices = []
	c1_indices_low_to_high = []
	data_chunks = []
	start_point = 23
	threshold = 0.2
	i = start_point
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
	j = 0

	while j < len(data_chunks):
	#while j < 20:
		x_vals = []
		y_vals_channel_1 = []
		y_vals_channel_2 = []
		c1_binary = []
		c2_binary = []
		for each in data_chunks[j]:
			s = each.strip().split(",")
			#print s
			try:
				if len(s) == 3:
					x_vals.append(s[0])
					if float(s[1]) > threshold:
						c1_binary.append(1)
					else:
						c1_binary.append(0)

					if float(s[2]) > threshold:
						c2_binary.append(1)	
					else:
						c2_binary.append(0)
					
					y_vals_channel_1.append(s[1])
					y_vals_channel_2.append(s[2])
			except:
				pass
		j += 1
		#print c1_binary
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
				#print 'Channel 1 switch at count ', c1_pause
				if c1_start == 0:
				#	print 'switch c1 low to high'
				#	print 'indices from j range ', j
					decoded_value.append(1)
					c1_indices.append({'pause':c1_pause, 'data_chunk_index':j, 'low_to_high':1} )
				else:
				#	print 'switch c1 high to low'
					c1_indices.append({'pause':c1_pause, 'data_chunk_index':j, 'low_to_high':0} )
				c1_start = c1_binary[i]
				c1_pause = 0
			else:
				c1_pause += 1
			if c2_binary[i] != c2_start:
				#print 'Channel 2 switch at count ', c2_pause
				if c2_start == 0:
				#	print 'switch c2 low to high'
					decoded_value.append(0)
				else:
					print 'switch c1 high to low'
				c2_start = c2_binary[i]
				c2_pause = 0
			else:
				c2_pause += 1
			i += 1

		#print decoded_value
		#print len(decoded_value)
		#print c1_indices
		print 'data batch Done'

	k = 0
	offset = 0
	c1_indices_low_to_high = []
	while k < len(c1_indices)-1:
		#print c1_indices[k]
		if c1_indices[k]['low_to_high'] == 1:
			if c1_indices[k]['data_chunk_index'] == c1_indices[k-1]['data_chunk_index']:
				offset = offset + c1_indices[k]['pause']
			else: 
				offset = c1_indices[k]['pause']
			c1_indices_low_to_high.append( chunk_size*(c1_indices[k]['data_chunk_index']-1)+start_point+offset )
		else:
			offset = offset + c1_indices[k]['pause']
		k += 1
		#print c1_indices_low_to_high

	k = 0
	s = open(saveName, 'w')
	while k < len(c1_indices_low_to_high)-1:
		s.write(str(c1_indices_low_to_high[k])+'\n')
		#print c1_indices_low_to_high[k+1] - c1_indices_low_to_high[k]
		k += 1
	q += 1
print "complete"
