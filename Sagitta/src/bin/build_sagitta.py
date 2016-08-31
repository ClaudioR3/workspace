import os

#file name of the main.py
main_file="Sagitta.py"
#file name of the script
file_name="sagitta"

#detect current path
path=os.path.dirname(os.path.abspath(__file__))
dirs=path.split('/')
#select right path
path=""
for i in range(0,len(dirs)-1):
	path+=dirs[i]+'/'

#text in 'sagitta' script
text="#!/bin/bash\n"
text+="\npython %s%s $@"%(path,main_file)

#create 'sagitta' script and write all text into the file
f=open(file_name,'w')
f.write(text)
f.close()