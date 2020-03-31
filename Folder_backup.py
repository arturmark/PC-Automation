
'''
• Control Panel:
================================================='''
'on=True; off=False; exe=(); pause_code=(); debug_mode=()'
# --------------------------------------------------------
exe=True            # Execu/te code (copy, remove)   [#...] [X]
pause_code=True     # Pause code

# Print code mode:
if exe:pass
else:print("\n >>> {exe} mode is disabled!!!\n\n")


'''
• Define Variables:
================================================='''
FolderToBackup = 'C:\Sample_folder'
DestDrive = 'E:\\'
tag_copy = '-copy'
tag_old = '-old'
folder_copy = "E:\Sample_folder"+tag_copy
folder_copy_old = folder_copy+tag_old


'''
• Code timer:
================================================='''
import time


'''
• Check directories to backup if exists:
================================================='''
import sys, os

if os.path.exists(FolderToBackup):pass
else:
    print('\n !Error, no folder to backup:\n',FolderToBackup,'\n')
    if pause_code:
        os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    sys.exit()                  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if os.path.exists(DestDrive):pass
else:
    print('\n !Error - no destination drive:\n',DestDrive,'\n')
    if pause_code:
        os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    sys.exit()                  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


'''
• Timestamp:
================================================='''

from datetime import datetime
timestamp = datetime.now().strftime("%a, %d %b %Y, %H:%M:%S")
print(''+timestamp)


'''
• Folder size:
================================================='''
from pathlib import Path

root_directory = Path(FolderToBackup)
# root_directory = Path('D:\data')
x= sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
if x <= 1024:       # <  1 KB
    unit = 'Bytes'
    x= x
elif x <= 1024**2:  # <  1 MB
    unit = 'KB'
    x= x/1024
elif x <= 1024**3:  # <  1 GB
    unit = 'MB'
    x= x/1024**2
else:               # >= 1 GB
    unit = 'GB'
    x= x/1024**3

x= round(x,2)
x= '|  Size: '+str(x)+' '+unit
# print('\n',x)


'''
• Number of items:
================================================='''
folder_list=0


# List all files in the directory tree: FolderToBackup
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles
dirName = FolderToBackup
listOfFiles = getListOfFiles(dirName) # Get the list of all files in directory tree at given path


folder_list= listOfFiles
folder_list= len(folder_list)
x= x+'  |  Items: '+str(folder_list)


print('\nBackup Folder: ',FolderToBackup,'',x)
print()
# print('------------------------------------------------------------------------')
if pause_code: os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print()

# Start timer:
t_code_start = time.perf_counter()


'''
• Backup folder:
================================================='''

# Remove copy of old one:
# -----------------------------------------------
# Check if exists   E:/DEV-old/
# Remove            E:/DEV-old/
# Copy              E:/DEV/ to E:/DEV-old/
# Remove            E:/DEV/
# Copy              D:/DEV/ to E:/DEV/

# from distutils.dir_util import copy_tree
# import shutil


'''
• Copy/Remove:
================================================='''
if on:
    from distutils.dir_util import copy_tree
    # Check if folder-copy exists:
    if os.path.exists(folder_copy):
        import shutil
        # Check if folder-copy-old exists:
        # print('\nRemoving folder...',folder_copy_old)
        if os.path.exists(folder_copy_old):
            print(' [#...] removing...',folder_copy_old)

            # Remove old folder:
            try:
                if exe: shutil.rmtree(folder_copy_old)
            except OSError as e:
                print("\n Error: %s - %s." % (e.filename, e.strerror))

        # COPY folder-copy to folder-copy-old:
        if on:
            # Check if folder-copy exists:
            if os.path.exists(folder_copy):
                print(' [##..] copying... ',folder_copy,'->',folder_copy_old)
                if exe: copy_tree(folder_copy, folder_copy_old)     # Copy!


        # Remove folder-copy:
        print(' [###.] removing...',folder_copy)
        try:
            if exe: shutil.rmtree(folder_copy)
        except OSError as e:
            print("\n Error: %s - %s." % (e.filename, e.strerror))


    # COPY new one:
    if on:
        if os.path.exists(FolderToBackup):
            print(' [####] copying... ',FolderToBackup,'->',folder_copy)
            if exe: copy_tree(FolderToBackup, folder_copy)     # Copy!
        else:print(' !No Folder...', FolderToBackup)


'''
• Folder backup completed:
================================================='''
print('\n\n Folder backup completed.')
print('------------------------------------------')

if os.path.exists(folder_copy):print(' '+folder_copy,'       - created!')
else:print(' '+folder_copy, '- doesn\'t exist!')

if os.path.exists(folder_copy_old):print(' '+folder_copy_old,'   - created!')
else:print(' '+folder_copy_old, '- doesn\'t exist!')


'''
• Code execution time:
================================================='''
t_code_sec = round(time.perf_counter() - t_code_start, 3) ; print('\n Time:',t_code_sec,'[s]\n')
# if pause_code: os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


'''
• List files and folders:
================================================='''
if on:
    import keyboard

    print('\nPress [L] to list all items... or any key to EXIT:')
    while True:
        x= keyboard.read_key()
        if x == "l":break
        sys.exit()

    # Start time
    t_code_start = time.perf_counter()

    # List folders and files in dir tree: FolderToBackup
    if off:
        print()
        for i in listOfFiles:
            print(i)
        # x= len(listOfFiles)
        # print('\n',x)
    
    # List folders and files in dir: folder_copy
    if off: 
        folder_list= os.listdir(path=folder_copy)
        for i in folder_list:
            print(i)
        x= len(folder_list)
        print('\n',x)

    # List files only:
    if on:
        print()
        path = 'c:\\projects\\hc2\\'
        path = folder_copy

        files = []
        # r= root, d= directories, f= files
        for r, d, f in os.walk(path):
            for file in f:
                # print(file)
                # files.append(os.path.join(file))                          # all items
                # if '.txt' in file: files.append(os.path.join(r, file))    # .txt files only
                # if '.py' in file: files.append(os.path.join('', file))    # .py files only
                # if '.lnk' in file: files.append(os.path.join(r, file))    # .lnk files only
                if '.lnk' in file:pass                                      # .lnk files excluded
                else: files.append(os.path.join('', file))

        files.sort(reverse=False)    # sort list ascending
        
        for f in files:
            print(f)
        print('\n',len(files),'files')


    # End time:
    t_code_sec = round(time.perf_counter() - t_code_start, 3) ; print('\n Time:',t_code_sec,'[s]\n')

    # print('\n')
    if pause_code: os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
