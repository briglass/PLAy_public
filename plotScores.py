from numpy import *
import matplotlib.pyplot as plt

########################################################
# This function takes dates as an array of strings and scores as an array of numbers. 
# path is optionally where you want the output file saved.
# the function returns the plot figure if interactivity is desired (likely not).
# this function assumes following:
# from numpy import *
# import matplotlib.pyplot as plt
# which much of which can easily be removed a bit.
########################################################
def PlotScore(dates,scores,path="./"):

	fig=plt.figure()
	ax=fig.add_subplot(111)

	ax.plot(arange(len(dates)),scores)
	plt.xticks(arange(len(dates)))

	ax.set_xticklabels(dates)
	ax.set_ylabel('PlayIQ Score')
	ax.set_xlabel('Date of Test')

	plt.savefig(path + 'scores.png')

	return plt
########################################################	


###below is just for demo purposes to try out

#temp=PlotScore(array(["12-9-2014","22-9-2014","03-2-2015","3-9-2015"]),array([1.1,2,3,7]))
#temp.show() # this just makes it interactive
	
	


        

