#removing old releases
import os
import shlex
import shutil
import subprocess
import zipfile


releases_files_list = os.listdir(os.getcwd() + '/artifacts')

    
if os.path.exists('deploy'):
    subprocess.run(shlex.split('rm -rf deploy'), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)
os.makedirs('deploy')


print(releases_files_list)
if len(releases_files_list)>0:
    sorted__release_list = sorted(releases_files_list)
    with zipfile.ZipFile(os.getcwd() + '/artifacts/' + sorted__release_list[0] ,"r") as zip_ref:
        zip_ref.extractall(os.getcwd() +'/deploy')
        print("last release correctly deployed i /deploy directory")
    
    dir_list = os.listdir(os.getcwd()+'/deploy')
    shutil.rmtree('deploy/'+dir_list[0]+'/.git', ignore_errors=False, onerror=None) 
   
