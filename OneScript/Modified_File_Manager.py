# [warning: do not run this script in the partiiton where system files are stored]
# use it with caution
import os
import shutil

path = '/home/hafeez/Downloads/'
names = os.listdir(path)
folder_name = ['Images', 'Audio', 'Videos', 'Documents', 'Softwares','System']

for x in range(0,6):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for (main_dir,sub_dir,file_in_sub_dir) in os.walk(path):
    print(main_dir)
    for files in  file_in_sub_dir:
    	#Images
        if ".svg" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".jpg" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".jpeg" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".bmp" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".png" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".gif" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".tiff" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".psd" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        if ".raw" in files and not os.path.exists(path+'Images/'+files):
            shutil.move(main_dir+'/'+files, path+'Images/'+files)
        
        
        #Audio / Music
        if ".mp3" in files and not os.path.exists(path+'Audio/'+files):
            shutil.move(main_dir+'/'+files, path+'Audio/'+files)
        if ".m4a" in files and not os.path.exists(path+'Audio/'+files):
            shutil.move(main_dir+'/'+files, path+'Audio/'+files)
        if ".wav" in files and not os.path.exists(path+'Audio/'+files):
            shutil.move(main_dir+'/'+files, path+'Audio/'+files)
	
	# Video / Movies
        if ".mp4" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mkv" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".webm" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mpg" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mp2" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mpeg" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mpe" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mpv" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".ogg" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".m4v" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".m4p" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".avi" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".wmv" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".mov" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".qt" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".flv" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        if ".swf" in files and not os.path.exists(path+'Videos/'+files):
            shutil.move(main_dir+'/'+files, path+'Videos/'+files)
        
	
	# Documents
        if ".pdf" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".xps" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".doc" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".docx" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".pptx" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".xlsx" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)
        if ".xml" in files and not os.path.exists(path+'Documents/'+files):
            shutil.move(main_dir+'/'+files, path+'Documents/'+files)

	# Software / Comperessed Packages
        if ".exe" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".deb" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".zip" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".tar.gz" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".tar.xz" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".tar.bz2" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
        if ".iso" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".apk" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".app" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".7z" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".zipx" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".rpm" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".sitx" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".rar" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	if ".pkg" in files and not os.path.exists(path+'Softwares/'+files):
            shutil.move(main_dir+'/'+files, path+'Softwares/'+files)
	


	# System files 
        if ".cdd" in files and not os.path.exists(path+'System/'+files): # Conserved Domain Database
            shutil.move(main_dir+'/'+files, path+'System/'+files)
        if ".dll" in files and not os.path.exists(path+'System/'+files): # Dynamic Link Library
            shutil.move(main_dir+'/'+files, path+'System/'+files)
        if ".dlc" in files and not os.path.exists(path+'System/'+files): # Dlc
            shutil.move(main_dir+'/'+files, path+'System/'+files)
        if ".bin" in files and not os.path.exists(path+'System/'+files): # Binary
            shutil.move(main_dir+'/'+files, path+'System/'+files)
        if ".cab" in files and not os.path.exists(path+'System/'+files): # Windows Cabinet File
            shutil.move(main_dir+'/'+files, path+'System/'+files)
	if ".sh" in files and not os.path.exists(path+'System/'+files): # Shell Script
            shutil.move(main_dir+'/'+files, path+'System/'+files)
	if ".cgz" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".cpl" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".crash" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".cur" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".deskthemepack" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".dmp" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".drv" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".ds_store" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".fir" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".fpbf" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".fw" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".cpl" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".hlp" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".hpj" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".ico" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".idx" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".its" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".key" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".lnk" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".log" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".log1" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".log2" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".metadata_never_index" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".mi4" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".mum" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".nrl" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".nt" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".pbp" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".pdr" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".pk2" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".ppm_b" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".prefpane" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".rmt" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".ruf" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".savedsearch" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".saver" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".scr" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files
	if ".sfcache" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".spi" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".swp" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".sys" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	if ".themepack" in files and not os.path.exists(path + 'System/' + files):
	    shutil.move(main_dir + '/' + files, path + 'System/' + files)
	
