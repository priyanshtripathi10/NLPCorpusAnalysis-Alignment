#Below code will take raw txt file as input and will split in individual sentences





fout = open("eng_sen_13","w")
with open("eng_sen_13") as f:	
	content = f.read()                                                        #Reading the data from txt fie
	lines = content.split('.')                                                #Segregate all sentences
	for line in lines:                                                        #for each line
			if '\n'or'\n\n' in line:
				fout.write("\n"+ str(line))
				
				
			else:
				print("Not present")
				
f.close()
           

