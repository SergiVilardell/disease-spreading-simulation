from random import *
import numpy
import decimal
N=250
T=250
peasant=numpy.zeros(shape=(N,T))
beta=0.0
ratio_average = 0



f = open('data','w')

while(beta<=1):
	#this sets the number of realizations for each beta
	for r in range (100):
		#Set the inital (healthy/sick) population (0/1) appox 50% of each
		for n in range (125):
			peasant[randint(0,249)][0]=1
		for t in range (T-1):

			#periodic boundary conditions
			for n in range (N):
				peasant[n][t+1]=peasant[n][t]
			#infection function: in order to see which individuals are infected in the current time step we increase its previous value by 2 when infected. Therefore the new infected ind are 2 and 3.
			if peasant[0][t]==1 and uniform(0.0,1.0) <= beta:
				peasant[1][t+1]= peasant[1][t]+ 2
			if peasant[0][t]==1 and uniform(0.0,1.0) <= beta:
				peasant[N-2][t+1]= peasant[N-2][t]+ 2
			#for the rest
			for i in range(1,N-2):
				if peasant[i][t]==1 and uniform(0.0,1.0)<= beta:
					peasant[i-1][t+1]= peasant[i-1][t] + 2
				if peasant[i][t]==1 and uniform(0.0,1.0)<= beta:
					peasant[i+1][t+1]= peasant[i+1][t] + 2
			#for the N-2 peasant
			if peasant[N-2][t+1] == 1 and uniform(0.0 , 1.0) <= beta:
				peasant[0][t+1] = peasant[0][t]+ 2
			if peasant[N-2][t+1] == 1 and uniform(0.0 , 1.0) <= beta:
				peasant[N-3][t+1] = peasant[N-3][t]+ 2
			peasant[0][t+1]=peasant[N-1][t+1]
			#heal function: only the 1s can be healed, as they have not been infected in this time step
			for n in range (N):
				if peasant[n][t+1]==1 and uniform(0.0, 1.0)< 0.5:
					peasant[n][t+1]=0
				if peasant[n][t+1]==2 or peasant[n][t+1]==3:
					peasant[n][t+1]=1

		healthy=0.0
		infected=0.0
		#count the number of sick individuals and compute the ratio
		for n in range (N-1):
			if peasant[n][T-1]==0:
				healthy = healthy + 1.0
			else:
				infected = infected +1.0
		ratio=infected/249.0

		ratio_average=ratio_average+ratio

	ratio_average=(ratio_average)/100.0

	f.write("%f %f\n"%(beta,ratio_average))
	ratio_average = 0
	beta=beta+0.01
	#this is printed in order to know the progression of the simulation, becuase it's rather long
	print (beta)

f.close()


#CHANGE LINES 22 TO 64 WITH THE CODE BELOW FOR FIXED EXTREMES CONDITION
		# 	#infection function
		# 	for n in range (N):
		# 		peasant[n][t+1]=peasant[n][t]

		# 	if peasant[0][t]==1 and uniform(0.0,1.0) <= beta:
		# 		peasant[1][t+1]= peasant[1][t]+ 2

		# 	if peasant[0][t+1] == 1 and uniform(0.0 , 1.0) <= beta:
		# 		peasant[1][t+1] = peasant[1][t]+2
		# 	#for the rest
		# 	for i in range(1,N-1):
		# 		if peasant[i][t]==1 and uniform(0.0,1.0)<= beta:
		# 			peasant[i-1][t+1]= peasant[i-1][t] + 2
		# 			peasant[i+1][t+1]= peasant[i+1][t] + 2
		# 	#for the Nth peasant
		# 	if peasant[N-1][t+1] == 1 and uniform(0.0 , 1.0) <= beta:
		# 		peasant[N-2][t+1] = peasant[N-2][t]+ 2
		# 	for n in range (N):
		# 		if peasant[n][t+1]==1 and uniform(0.0, 1.0)< 0.5:
		# 			peasant[n][t+1]=0
		# 		if peasant[n][t+1]==2 or peasant[n][t+1]==3:
		# 			peasant[n][t+1]=1

		# healthy=0.0
		# infected=0.0

		# for n in range (N):
		# 	if peasant[n][T-1]==0:
		# 		healthy = healthy + 1.0
		# 	else:
		# 		infected = infected +1.0


	# 	healthy=0.0
	# 	infected=0.0

	# 	for n in range (N):
	# 		if peasant[n][T-1]==0:
	# 			healthy = healthy + 1.0
	# 		else:
	# 			infected = infected +1.0
	# 	ratio=infected/250.0

	# 	ratio_average=ratio_average+ratio

	# ratio_average=(ratio_average)/100.0

	# f.write("%f %f\n"%(beta,ratio_average))
	# ratio_average = 0
	# beta=beta+0.01
	# print (beta)















