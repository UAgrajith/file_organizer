#File Organizer PROJECT 01
#Author : U A FONSEKA
#DESCRIPTION:
#   Automatically organizes files in a folder


#import libraries
import os,shutil

#   Configuration
path = r"c:\Users\Lenovo\Desktop\FileOrganizerProject"
os.chdir(path)

#   File categories(Python Dictionary)
file_types = { "images":[".jpg",".png",".jpeg"],
 "documents":[".pdf",".docx",".txt"],
 "videos":[".mp4",".mkv"],
 "music":[".mp3"] }

#   Logic
for file in os.listdir():
    file_name,file_ext = os.path.splitext(file)
    for folder,extentions in file_types.items():
        if file_ext in extentions:
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(file,os.path.join(folder,file))    
            print(f"moved {file} to {folder}")
            break

#   End
print("\n All files have been organized correctly")
