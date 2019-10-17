#! python3
#its the next gen WinRar. The only new feature is that you dont get spammed to purchase something.

import zipfile, os
def backupToZip(folder):
	#backup all of "folder" into a zip file
	folder = os.path.abspath(folder)
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1
	print('Done.')



	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFileName):
			break
		number = number + 1
	for foldername, subfolder, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		backupZip.write(foldername)
		for filename in filenames:
			newBase / os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip') 
				continue
			
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done.')
	
			
			
