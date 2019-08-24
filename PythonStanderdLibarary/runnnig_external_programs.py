import subprocess

# for windows we need to add paramter for shell=True
completed = subprocess.run(["dir"], capture_output=True, text=True, shell=True)

# running other python script
complicated = subprocess.run(
    ["python", "PythonStanderdLibarary/other.py"], capture_output=True, text=True, check=True, shell=True)

# print("args", completed.args)
# print("returncode", completed.returncode)
# print("stderr", completed.stderr)
# print("stdout", completed.stdout)

if complicated.returncode != 0:
    print("complicated:stdout", complicated.stderr)
