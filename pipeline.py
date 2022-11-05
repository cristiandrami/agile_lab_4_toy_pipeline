

import shlex
import subprocess

#cloning 
git_clone_args= 'git clone https://github.com/cristiandrami/agile_lab_4_toy_pipeline.git'
subprocess.run(shlex.split(git_clone_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)


#testing 
tests_args = 'pytest -v'
result = subprocess.run(shlex.split(tests_args), stdout=subprocess.PIPE, stderr=None, stdin=subprocess.PIPE)

result_string = str(result.stdout)
test_failure = ' FAILED '
test_summary_failure = ' failed, '
if test_failure not in result_string and test_summary_failure not in result_string:
    print('tests ok')
else:
    print('tests not ok')