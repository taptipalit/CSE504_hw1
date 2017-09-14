import urllib2
import re
import os

from collections import OrderedDict

os.system('grep gcc compilation_log  > compiler_cmds')
os.system('grep g++ compilation_log  >> compiler_cmds')

flag_file = open('compiler_cmds', 'r')

cmd_data = flag_file.read()

cmds = cmd_data.split('\n')

flag_count_dict = {}

for cmd in cmds:
    tokens = cmd.split(' ')
    for token in tokens:
        # check if it is a flag
        if token.startswith('-') and (not token.startswith('-W')) and (not token == '-o') and (not token.startswith('-I')) and (not token.startswith('-D')) and (not token.startswith('-L')) and (not token.startswith('-l')):
            if token in flag_count_dict:
                flag_count_dict[token] = flag_count_dict[token] + 1
            else:
                flag_count_dict[token] = 1


sorted_dict = OrderedDict(sorted(flag_count_dict.items(), key=lambda x: x[1]))

for k, v in sorted_dict.items():
    print "%s: %s" % (k, v)
