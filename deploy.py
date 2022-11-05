#removing old releases
import os
import zipfile


releases_files_list = os.listdir(os.getcwd() + '/artifacts')

if not os.path.exists('deploy'):
    os.makedirs('deploy')

print(releases_files_list)
if len(releases_files_list)>0:
    sorted__release_list = sorted(releases_files_list)
    with zipfile.ZipFile(os.getcwd() + '/artifacts/' + sorted__release_list[0] ,"r") as zip_ref:
        zip_ref.extractall(os.getcwd() +'/deploy')
        print("last release correctly deployed i /deploy directory")