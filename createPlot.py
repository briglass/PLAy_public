from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
#make resource directory.

#takes Perception, Learning, Attention, and overall scores as an argument.
#saves a file to local directory

################################################################################
#####Helper function plots one score from start position.
################################################################################
def PlotHelper(score,start,icon0,icon100,xSize,ySize,mainImg,draw):
	if int(round(score/10.0))>0:
		for i in xrange(int(round(score/10.0))):
			mainImg.paste(icon100, (start[0]+i*xSize,start[1],start[0]+(i+1)*xSize,start[1]+ySize))
			end=i  
	else:
		i=-1
	for j in xrange(i+1,10):
			mainImg.paste(icon0, (start[0]+j*xSize,start[1],start[0]+(j+1)*xSize,start[1]+ySize))
			end=j
	
	font = ImageFont.truetype("static/resourcePlot/Arial.ttf", 42) #font size here is hacked, should scale to image
	draw.text((20+start[0]+(end+1)*xSize, start[1]),str(int(round(score)))+"%",(0,0,0),font=font)	# goes to 255, rgb  ## the first x number, 20 is a complete hack, should be scaled.

			
################################################################################	
######Main Plotting Function takes the scores.
################################################################################
		
def PlotPLAyScore(pS,lS,aS,oS,userName="defaultName"):
#####set up back ground image that will be plotted over
	mainImg = Image.open("static/resourcePlot/shareLayoutNew.jpg")	
	#print(mainImg.size)
	draw = ImageDraw.Draw(mainImg)
########load up and scale the plotting icons, will need fractional ones in final product
	icon100 = Image.open("static/resourcePlot/FullCrop2.jpg")	#made these in illustrator, then graphic converter to trim and export
	scale=5*float(mainImg.size[0])/icon100.size[0]	# scale result icon in terms of overall image, 5 is something to fiddle with to fit size correctly. The bigger the number, the smaller the icon

	xSize=int(icon100.size[0]/scale)
	ySize=int(icon100.size[1]/scale)
	
	icon100 = icon100.resize((xSize, ySize), Image.ANTIALIAS) 
	
	icon0 = Image.open("static/resourcePlot/brainEmptyCrop.jpg")
	icon0 = icon0.resize((xSize, ySize), Image.ANTIALIAS) #all icons need to be same size.
######################## past in icons to communicate results

##Perception
	start=(350,105)	# hacked, fix later to scale with background
	PlotHelper(pS,start,icon0,icon100,xSize,ySize,mainImg,draw)
##Learning
 	start=(350,205)	#hacked, fix later to scale with background
 	PlotHelper(lS,start,icon0,icon100,xSize,ySize,mainImg,draw)
##Attention
 	start=(350,305)	#hacked, fix later to scale with background
 	PlotHelper(aS,start,icon0,icon100,xSize,ySize,mainImg,draw)
##Overall
 	start=(350,390)	#hacked, fix later to scale with background
 	PlotHelper(oS,start,icon0,icon100,xSize,ySize,mainImg,draw)
 	
########################Write in text for scores
	fileName=userName+".jpg"
        folderName="static/img/userplots/"
        print folderName+fileName
	mainImg.save(folderName+fileName)
	return
	
	# font = ImageFont.truetype(<font-file>, <font-size>)
# 	font = ImageFont.truetype("static/resourcePlot/Arial.ttf", 16)
# 	draw.text((100, 100),"Sample Text",(100,200,100))	# goes to 255, rgb
# 	draw.text((0, 0),"Sample Text",(0,0,0),font=font)
 	#mainImg.save('sample-out.jpg')
# 


#PlotPLAyScore(55,74,83.9,98)