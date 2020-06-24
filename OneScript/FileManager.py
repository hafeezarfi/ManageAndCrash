import os
import shutil

path = '/home/aiwithab/Downloads/'      # Path: to where you want to sort the files

files = os.listdir(path) # list all the files and store list in files variable

folder_name = ['Images', 'Audios', 'Videos', 'Documents', 'Softwares'] # name of folders to be created if not already present

    # Extensions are categorised based on our prefrence and already provided to be searched in every file name
    # if found it will be moved to the folder based on the file extension.
    # If you want to add or remove any extension do it in list below.


image_extensions = ['.png','.jpg','.jpeg','.fig','.bmp','.gif','.tiff','.psd','.raw','.svg']
audio_extensions = ['.mp3','.m4a','.wav']
video_extensions = ['.mp4','.ts','.mkv','.web','.mpg','.mp2','.mpe','.mpe','.mpv','.ogg','.m4v','.m4p','.avi','.wmv','.mov','.qt' ,'.flv','.swf']
document_extensions = ['.EXE','.csv','.mdj','.TXT','.txt','.html','.tex','.pdf','.PDF','.xps','.doc','.docx','.ppt','.pptx','.xls','.xml','.xslx']
software_extensions = ['.json','.img','.exe','.deb','.tgz','.sh','.tar','.tar','.zip','.tar','.iso','.apk','.app','.7z','.zip','.rpm','.sit','.rar','.pkg']

# Creating folders if not already present

for x in range(0,5):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])


# Function to move files based on its extension
# extension is provided from list and folder is given manually

def moveFile(extension,folder_as_per_extension):
    
    for file in files:

        if f"{extension}" in file and not os.path.exists(path+f'{folder_as_per_extension}/'+file): # checks if extension is present in file name and location of file
            shutil.move(path+file, path+f'{folder_as_per_extension}/'+file) # moves file to desired folder
    

#*****************Image*******************

for extension in image_extensions:
    moveFile(extension,'Images')


#*****************Audio*******************

for extension in audio_extensions:
    moveFile(extension,'Audios')


#*****************Video*******************

for extension in video_extensions:
    moveFile(extension,'Videos')


#**************Document*******************

for extension in document_extensions:
    moveFile(extension,'Documents')


#**************Software*******************

for extension in software_extensions:
    moveFile(extension,'Softwares')
