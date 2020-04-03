import os
import shutil

path = 'C:/Users/Hafeez/Downloads/'
names = os.listdir(path)
folder_name = ['Images', 'Audio', 'Videos', 'Documents', 'Softwares']
       
for x in range(0,5):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in  names:
    # Images
    if ".svg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
    if ".jpg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
    if ".jpeg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
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


    # Audio
    if ".mp3" in files and not os.path.exists(path+'Audio/'+files):
        shutil.move(path+files, path+'Audio/'+files)
    if ".m4a" in files and not os.path.exists(path+'Audio/'+files):
        shutil.move(path+files, path+'Audio/'+files)
    if ".wav" in files and not os.path.exists(path+'Audio/'+files):
        shutil.move(path+files, path+'Audio/'+files)
    
    # Videos
    if ".mp4" in files and not os.path.exists(path+'Videos/'+files):
        shutil.move(path+files, path+'Videos/'+files)
    if ".mkv" in files and not os.path.exists(path+'Videos/'+files):
        shutil.move(path+files, path+'Videos/'+files)
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
        shutil.move(path+files, path+'Documents/'+files)
    if ".xps" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".doc" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".docx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".pptx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".xlsx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".xml" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)

    # Software
    if ".exe" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".deb" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".sh" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.gz" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.xz" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".zip" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.bz2" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".iso" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
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

    
