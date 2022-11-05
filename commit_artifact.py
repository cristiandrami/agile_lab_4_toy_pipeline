import datetime
from glob import glob
import os
import re
import shlex
import shutil
import subprocess
import sys
import zipfile

def addFolderToZip(zip_file, folder):
    for file in glob(folder+"/*"):
            if os.path.isfile(file):
                zip_file.write(file, os.path.basename(file), zipfile.ZIP_DEFLATED)
            elif os.path.isdir(file):
                addFolderToZip(zip_file, file.encode('ascii'))


#cloning 
git_clone_args= 'git clone https://github.com/cristiandrami/agile_lab_4_toy_pipeline.git'
git_clone_proc = subprocess.run(shlex.split(git_clone_args), stdin=subprocess.PIPE, capture_output=True, text=True)

dir_name = git_clone_proc.stderr.split("'")[1]
#new_dir_name = new_dir_name.replace("'", '*')
print(dir_name)


print(git_clone_proc.stderr)
#git clone returns 0 if is all ok
if git_clone_proc.returncode != 0:
    print('is not possible to clone this directory, check if the url is correct or check if there is already this repository on the')
    if os.path.exists(dir_name):
        print('we can do the pull')
        subprocess.run(shlex.split('git pull'), stdin=subprocess.PIPE, capture_output=True, text=True)
        
        print('pull done')
    
    else: 
        sys.exit()




#new_dir_name = new_dir_name[new_dir_name.find('*')+1 : new_dir_name.find('*')]
#print(new_dir_name)
#testing 
tests_args = 'pytest -v --ignore=deploy'
tests_proc = subprocess.run(shlex.split(tests_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)


print(tests_proc.returncode)
if tests_proc.returncode != 0:
    print('there is something wrong with test, take a look here:\n')
    print(re.sub(r"\\n", "\n", str(tests_proc.stdout)))
    sys.exit()
    


if not os.path.exists('artifacts'):
    os.makedirs('artifacts')
    
    
#adding a time stamp to the dir
date_time = datetime.datetime.now()
time_stamp=date_time.timestamp()

new_dir_name = '[' + str(date_time) + '] '+ dir_name
shutil.copytree(dir_name, new_dir_name)
#os.rename(dir_name, new_dir_name)
print('tag added to the release directory\n')


#zip file creating
subprocess.run(['zip', '-r', new_dir_name+".zip", new_dir_name, '-x', '/.git'],  capture_output=True)

    
shutil.move(os.getcwd() + '/'+ new_dir_name+'.zip', os.getcwd() + '/artifacts')
print('release zip file moved to the /artifacts directory\n')
shutil.rmtree(os.getcwd() + '/'+ new_dir_name, ignore_errors=False, onerror=None)
print('release folder deleted\n')


#removing old releases
releases_files_list = os.listdir(os.getcwd() + '/artifacts')
releases_name_list= []

for elem in releases_files_list:
    releases_name_list.append(os.fsdecode(elem))


if len(releases_name_list)>3:
    sorted__release_list = sorted(releases_name_list, reverse=True)
    #print("sorted list : " + str(sorted__release_list))
    for index, elem in enumerate(sorted__release_list):
        if index > 2:
            os.remove(os.getcwd() + '/artifacts/'+elem)

print('you have imported the last release present on github, with the deploy.py you can unzip it in deploy directory and work on it')
#print(os.listdir(os.getcwd() + '/artifacts'))
    
        











