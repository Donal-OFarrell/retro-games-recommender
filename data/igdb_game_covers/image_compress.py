# https://www.geeksforgeeks.org/how-to-compress-images-using-python-and-pil/
# run this in any directory 
# add -v for verbose 
# get Pillow (fork of PIL) from 
# pip before running --> 
# pip install Pillow 

# import required libraries 
import os 
import sys 
from PIL import Image 

# define a function for 
# compressing an image 
def compressMe(file, verbose = False): 
	
	# Get the path of the file 
	filepath = os.path.join(os.getcwd()+'/original', file) 
	
	# open the image 
	picture = Image.open(filepath) 

	# sometimes get error if image saved in wrong format. This fixes.
	if picture.mode in ("RGBA", "P", "LA"): 
		picture = picture.convert("RGB")
	
	# quality parameter defaults to 75, can up to 95 if feel losing quality but ups file size. Can also lower if necessary.
	picture.save(os.path.join(os.getcwd()+'/compressed',file), "JPEG", optimize = True) 
	return

# Define a main function 
def main(): 
	
	verbose = False
	
	# checks for verbose flag 
	if (len(sys.argv)>1): 
		
		if (sys.argv[1].lower()=="-v"): 
			verbose = True
					
	# finds current working dir 
	cwd = os.getcwd()+'/original'

	formats = ('.jpg', '.jpeg') 
	
	# looping through all the files 
	# in a current directory 
	for file in os.listdir(cwd): 
		
		# If the file format is JPG or JPEG 
		if os.path.splitext(file)[1].lower() in formats: 
			print('compressing', file) 
			compressMe(file, verbose) 

	print("Done") 

# Driver code 
if __name__ == "__main__": 
	main() 
