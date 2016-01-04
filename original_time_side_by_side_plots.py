import matplotlib.pyplot as plt

files = ["0pt15","0pt5","0pt9","1pt15"]
fileSpot = "/Volumes/PENNY/splitData/"

#packet_indices = [(0,40),(0,41),(0,42)] # 0pt15_3Transmits
#packet_indices = [(0,40),(0,641),(0,742)] # 0pt15_3Transmits100ApartZoomed
#packet_indices = [(0,40),(1,40),(2,40),(3,40)] # 
#packet_indices = [(0,40),(0,500),(0,700),(0,1000),(1,40),(1,500),(1,700),(1,1000),(2,40),(2,500),(2,700),(2,1000),(3,40),(3,500),(3,700),(3,1000)] # 
#packet_indices = [(0,40),(1,40),(2,40),(3,40)]
#packet_indices = [(0,40),(3,500)]
packet_indices = [(1,1091),(1,1092),(1,1093),(1,1094)]

i = 0
firstThreshold = []
x_vals = []
y_vals_channel_1 = []
y_vals_channel_2 = []
while i < len(packet_indices):
	with open(fileSpot+files[packet_indices[i][0]]+"/"+str(packet_indices[i][1])+".csv") as g:
		data_chunk = [data.rstrip('\n') for data in g]
	#print data_chunk[0]
	firstThreshold.append(0)
	x_vals.append([])
	y_vals_channel_1.append([])
	y_vals_channel_2.append([])
	j = 0
	for each in data_chunk:
		#print each
		#print 'DDDDDDD'
		s = each.strip().split(",")
		#print s
		try:
			if len(s) == 3:
				x_vals[i].append(s[0])
				j += 1
				y_vals_channel_1[i].append(s[1])
				y_vals_channel_2[i].append(s[2])
		except:
			pass
	print 'xvals ', len(x_vals[i])
	print 'yC1 ', len(y_vals_channel_1[i])
	print 'yC2 ', len(y_vals_channel_2[i])
	i += 1

i = 0
legends = []
while i < len(y_vals_channel_1)*2:
	if (i % 2 == 0):
		legends.append( (files[packet_indices[i/2][0]]+"_"+str([packet_indices[i/2][1]])+"_c1" ) )
	else: 
		legends.append( (files[packet_indices[i/2][0]]+"_"+str([packet_indices[i/2][1]])+"_c2" ) )
	i += 1

i = 0
while i < len(y_vals_channel_1):

	plt.plot( x_vals[i],y_vals_channel_1[i],x_vals[i],y_vals_channel_2[i] )
	plt.ylabel("(V) Volts")
	plt.xlabel("Timestep")
	i += 1

plt.legend(legends)
plt.show()