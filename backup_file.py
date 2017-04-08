# #!/usr/bin/python

# -*- coding:utf8 -*-  
# Filename: backup_ver4.py 
import os 
import time

import sys
import subprocess
   
# 1. The files and directories to be backed up are specified in a list. 
source = ['d:\\tmp\\src1\\']
for src in sys.argv[1:]:
    source.append(src)
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that 
# 2. The backup must be stored in a main backup directory 
target_dir = 'd:\\tmp\\dst\\' # Remember to change this to what you will be using 
# 3. The files are backed up into a zip file. 
# 4. The current day is the name of the subdirectory in the main directory 
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive 
now = time.strftime('%H%M%S')
   
# Take a comment from the user to create the name of the zip file

#comment = raw_input('Enter a comment --> ') 
#if len(comment) == 0: # check if a comment was entered
#    target = today + os.sep + now + '.7z' 
#else: 
#    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.7z'

# Notice the backslash! 
# Create the subdirectory if it isn't already there 
if not os.path.exists(today): 
    os.mkdir(today) # make directory 
    print 'Successfully created directory', today
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
for src in source:
    zip_command = 'copy %s %s' % (src, today)
    # Run the backup 
    if os.system(zip_command) == 0: 
        print 'Successful backup to', today 
    else: 
        print 'Backup FAILED'  

zip_command = '"C:\\Program Files\\7-Zip\\7z.exe" a "%s\\zip" "%s\\*"'% (today, today)

ps = subprocess.Popen(zip_command,shell=True)
retcode = ps.wait();

if retcode == 0: 
    print 'Successful' 
else: 
    print 'Failed'
