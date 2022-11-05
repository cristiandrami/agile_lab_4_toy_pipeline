

import shlex
import subprocess

#cloning 
git_clone_args= 'git clone https://github.com/cristiandrami/agile_lab_4_toy_pipeline.git'
subprocess.run(shlex.split(git_clone_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)


#testing 
tests_args = 'pytest -v --trace'
result = subprocess.run(shlex.split(tests_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)
print(result.stdout)