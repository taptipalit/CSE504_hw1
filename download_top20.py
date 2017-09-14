import urllib2
import re
import os

os.chdir('download')
response = urllib2.urlopen('http://popcon.ubuntu.com/main/by_inst')
popcon_data = response.read()
popcon_recs = popcon_data.split('\n')
limit = 50
count = 0

# Download the source code
for rec in popcon_recs:
    if not rec.startswith('#'):
        tokens = re.split('\s+', rec)
        app_name = tokens[1]
        os.system('sudo apt-get -y build-dep ' + app_name)
        os.system ('apt-get source --compile ' + app_name)
        count = count + 1
        if (count > limit):
            break

os.chdir('../')
