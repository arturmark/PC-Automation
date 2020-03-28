
'''
• Code timer:
================================================='''
# print('>>>>:',sys._getframe().f_lineno); sys.exit()
import time
t_code_start = time.perf_counter()
import sys, os
pause_code=True
# print('\n>>>',sys._getframe().f_lineno); sys.exit()


# Remove copy of old one:
# -----------------------------------------------
# Check if exists   E:\Sample folder/
# Remove            E:\Sample folder-old/
# Copy              E:\Sample folder/ -> E:\Sample folder-old/
# Remove            E:\Sample folder/
# Copy              C:\Sample folder/ -> E:\Sample folder/

from distutils.dir_util import copy_tree
# import shutil

FolderToBackup = 'C:\Sample folder'
DestDrive = 'E:\\'

tag_old = '-old'
tag_copy = '-copy'
folder_copy = "E:\Sample folder"+tag_copy
folder_copy_old = folder_copy+tag_old
print('\n Backup Folder: ',FolderToBackup,'')
print('------------------------------------------------------------------------')


# Check directories to backup if exists:
if os.path.exists(FolderToBackup):pass
else:
    print('\n!Error - no file to backup:\n',FolderToBackup,'\n')
    if pause_code:
        os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    sys.exit()                  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if os.path.exists(DestDrive):pass
else:
    print('\n!Error - no destination drive:\n',DestDrive,'\n')
    if pause_code:
        os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    sys.exit()                  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# REMOVE folders:
if on:
    # Check if folder-copy exists:
    if os.path.exists(folder_copy):
        import shutil
        # Check if folder-copy-old exists:
        if os.path.exists(folder_copy_old):
            print('\n  *Removing...',folder_copy_old)

            # Remove old folder:
            try:
                shutil.rmtree(folder_copy_old)
            except OSError as e:
                print("\nError: %s - %s." % (e.filename, e.strerror))

        # COPY folder-copy to folder-copy-old:
        if on:
            # Check if folder-copy exists:
            if os.path.exists(folder_copy):
                print('  *Copying... ',folder_copy,'->',folder_copy_old)
                copy_tree(folder_copy, folder_copy_old)     # Copy!
                pass

        # Remove folder-copy:
        print('  *Removing...',folder_copy)
        try:
            shutil.rmtree(folder_copy)
        except OSError as e:
            print("\nError: %s - %s." % (e.filename, e.strerror))

# print('\n>>>',sys._getframe().f_lineno) #;sys.exit()


# COPY new one:
if on:
    if os.path.exists(FolderToBackup):
        print('  *Copying... ',FolderToBackup,'->',folder_copy)
        copy_tree(FolderToBackup, folder_copy)     # Copy!
        pass
    else:print('!No Folder...', FolderToBackup)


print('\n\n Folder backup completed.')
print('------------------------------------------------------------------------')

if os.path.exists(folder_copy):print(' ',folder_copy,'       - created!')
else:print(folder_copy, '- doesn\'t exist!')

if os.path.exists(folder_copy_old):print(' ',folder_copy_old,'   - created!')
else:print(folder_copy_old, '- doesn\'t exist!')


t_code_sec = round(time.perf_counter() - t_code_start, 3) ; print('\n  Total time:',t_code_sec,'[s]\n')
if pause_code: os.system("pause")      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
