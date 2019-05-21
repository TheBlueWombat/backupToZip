#! python3
# backupToZip.py - Copies entire folder and its contents into
# a ZIP file whose filename incremenets

import zipfile, os

def  backupToZip(folder):
	# BAckup the entire conents of "folder" into a ZIP file.
	
	folder = os.path.abspath(folder) # make sure folder is absolute
	
	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1
		
	# Create the ZIP file
	print('Creating %s...' % (zipFilename))
	backupToZip = zipfile.ZipFile(zipFilename, 'w')
	
	# TODO: Walk the entire folder tree and compress the files in each folder
	
	print('Done')
	
	
backupToZip('C:\\Users\\cruz\\Desktop\\Python++')