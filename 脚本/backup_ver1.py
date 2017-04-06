#来源：www.open-open.com
#编写一个Python脚本，实现为重要的文件或文件夹在指定的目录下创建备份。
#[设计思路]
#[1] 将需要备份的文件和目录由一个列表指定，通过传入参数获得并保存到列表中。
#[2] 备份应该保存在主备份目录中。
#[3] 将文件备份成一个压缩文件。
#[4] 每一次备份都根据当前的日期在主备份目录中创建一个子文件夹，而所备份的文件命名为当期的时间保存在这个子文件夹中。
#[5] 压缩命令由本地用户决定。可以使用任何本地的存档压缩命令，只要它有命令行界面就可以了，那样就可以从脚本中传递参数给它。
# [参考]
# [1] A Byte of Python, 2005
# [2] Python Manuals 2.6

#! /usr/bin/python
# Filename: backup_ver1.py
# 2010-7-12 wcdj
import os
import time
import sys
# 1, The files and directories to be backed up are specified in a list
# source = ['/home/wcdj/my_prog', '/home/wcdj/local_installed']
# The following information is the debug used
 print '--------------------------------'
source=[]
print 'The command line arguments are: '
    for i in sys.argv:  
        print i  
        if i == sys.argv[0]:  
            continue  
        source.append(i)  
    print source  
    print '--------------------------------'  
    # check input, if error app exit  
    if len(source) == 0:  
        print '''''You should input the files or directories, like 
    python backup_ver1.py /home/wcdj/myfile /home/wcdj/mydir ...'''  
        exit()  
    else:  
        print 'Some files or directorier will be saved into .tar.gz format: '  
        print source  
    # If you are using Windows, use   
    # source=[r'c:/Documents', r'd:/work'] or   
    # source=['c://Documents', 'd://work'] or   
    # something like that  
    # 2, The backup must be stored in a main backup directory  
    # Remember to change this to what you will be using  
    target_dir = '/home/wcdj/backup/'  
    # 3, The files are backed up into a tar file  
    # 4, The name of subdirectory and tar file  
    today = target_dir + time.strftime('%Y%m%d')  
    now = time.strftime('%H%M%S')  
    # Take a comment from the user to create the name of the tar file  
    comment = raw_input('Enter a comment: ')  
    if len(comment) == 0:# check if a comment was entered  
        target = today + os.sep + now + '.tar.gz'  
    else:  
        target = today + os.sep + now + '_' + /  
        comment.replace(' ', '_') + '.tar.gz'  
    #Create the subdirectory if it isn't already there  
    if not os.path.exists(today):  
        os.mkdir(today)# make directory  
        print 'Successfully created directory', today  
    # 5, We use the tar command(in Unix/Linux) to put the files in a tgz archive  
    tar_command = "tar -zcf %s %s" % (target, ' '.join(source))  
    # Run the backup  
    if os.system(tar_command) == 0:  
        print 'Successful backup to', target  
    else:  
        print 'Backup failed'  
    # end
