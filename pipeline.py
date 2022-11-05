

import shlex
import subprocess

git_clone_args= 'git clone https://github.com/cristiandrami/agile_lab_4_toy_pipeline.git'
subprocess.run(shlex.split(git_clone_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)
