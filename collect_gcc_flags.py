import os

os.system('python download_top20.py > compilation_log 2>&1')
os.system('python extract_common_flags.py')


