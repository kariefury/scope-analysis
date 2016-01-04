import matplotlib.pyplot as plt

files = ["0pt15","0pt5","0pt9","1pt15"]
frontFileName = "/Volumes/PENNY/0xFF00_"
endFileName = "_decoded_values.csv"
fileSpot = "/Volumes/PENNY/splitData/"
i = 0
while i < len(files):
	with open(frontFileName+files[i]+endFileName) as f:
		decodedBits = [bits.rstrip('\n') for bits in f]
	j = 0 
	count_16_bits = 0
	correct_16_bits = 0
	zero_16_bits = 0
	while j < len(decodedBits):
		if len(decodedBits[j]) == 16:
			count_16_bits += 1
			if decodedBits[j] == "1111111100000000":
				correct_16_bits += 1
			else:
				print files[i], "file. Error! 16 bits is ", decodedBits[j] , "bits at index ", j
		elif len(decodedBits[j]) != 0:
			print files[i], "file. Error! length is ", len(decodedBits[j]), "bits at index ", j
			with open(fileSpot+files[i]+"/"+str(j)+".csv") as g:
				data_chunk = [data.rstrip('\n') for data in g]
			#print data_chunk[0]
			x_vals = []
			y_vals_channel_1 = []
			y_vals_channel_2 = []
			for each in data_chunk:
				#print each
				#print 'DDDDDDD'
				s = each.strip().split(",")
				#print s
				try:
					if len(s) == 3:
						x_vals.append(s[0])
						y_vals_channel_1.append(s[1])
						y_vals_channel_2.append(s[2])
				except:
					pass
			#print len(x_vals)
			#print len(y_vals_channel_1)
			#print len(y_vals_channel_2)
			plt.plot(x_vals,y_vals_channel_1,x_vals,y_vals_channel_2)
			plt.show()
		else: 
			print files[i], "file. Zero Error! length is ", len(decodedBits[j]), "bits at index ", j
			with open(fileSpot+files[i]+"/"+str(j)+".csv") as g:
				data_chunk = [data.rstrip('\n') for data in g]
			x_vals = []
			y_vals_channel_1 = []
			y_vals_channel_2 = []
			for each in data_chunk:
				#print each
				#print 'DDDDDDD'
				s = each.strip().split(",")
				#print s
				try:
					if len(s) == 3:
						x_vals.append(s[0])
						y_vals_channel_1.append(s[1])
						y_vals_channel_2.append(s[2])
				except:
					pass
			#print len(x_vals)
			#print len(y_vals_channel_1)
			#print len(y_vals_channel_2)
			plt.plot(x_vals,y_vals_channel_1,x_vals,y_vals_channel_2)
			plt.show()
			zero_16_bits += 1
		if j == len(decodedBits)-1:
			print "number of correct transmittances ", correct_16_bits
			print "number of zero transmittances ", zero_16_bits
		j += 1
	i += 1