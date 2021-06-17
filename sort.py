import os,shutil
#os will help to deal with operating system and folders in the pc
#shutil will help move remaining files in folders
folders={
      'videos':['.mp4'],
      'audios':['.wav','.mp3'],
      'images':['.jpg','.png'],
      'documents':['.doc','.xlsx','.xls','.pdf','.zip','.rar','.docx'],
      'notepad':['.c']
}
#print(folders)
#To print only key values of dictionary
#for folder_name in folders:
    #print(folder_name,folders[folder_name])
    #This will print key and values of the dictionary

def rename_folder():
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder))==True:
            os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))


def create_mov(ext,file_name):
    find=False
    for folder_name in folders:
        #this if loop will run through the dictionary to check which type of file exists in list
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))#this creates the folders from the dictionaryif they are not present
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
            find=True
            break
            #print("found",folder_name)
    if find!=True:
        if other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,other_name))


        #print(ext,file_name)
    #when ext and file name is passed it will check from the key value n from that key value we will make folder

directry=input("Enter the location:")
other_name=input("Enter the folder name for unknown files:")
rename_folder()

all_files=os.listdir(directry)
length=len(all_files)
count=1
#listdir function will convert all files,folders into a list format
#print(all_files)

for i in all_files:
    if os.path.isfile(os.path.join(directry,i))==True:
        create_mov(i.split(".")[-1],i)#through split we will get ext of any file means type of file
    print(f"Total Files: {length} | Done: {count} | Left: {length-count}")
    count+=1
    #if os.path.isfile(directry+"\\"+i)==True:
        #print("yes")
    #isfile is used to check whether it is file or folder
