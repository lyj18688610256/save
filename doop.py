#! /usr/bin/python3 python3
import time
import subprocess
import os

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,encoding="utf-8")
    subp.wait(3600)
    print(subp.stdout)
    if subp.poll() == 0:
        print("success")
        os.system('sed \'s/\]//g\' ~/Documents/doop/downloads/out/securibench6/database/C.csv |sed \'s/\[//g\'|sed \'s/nil,//g\'|sed \'s/, </ -> </g\'|sed \'s/^/"/g\'|sed \'s/$/";/g\' |sed \'1i\strict digraph{ \'|sed \'s/ -> /" -> "/g\' > ~/Documents/doop/downloads/out/securibench6/database/F.dot')
        os.system('echo \'}\' >> ~/Documents/doop/downloads/out/securibench6/database/F.dot')
        os.system('dot -Tsvg ~/Documents/doop/downloads/out/securibench6/database/F.dot -o ~/Documents/doop/downloads/out/securibench6/database/output2.svg')
        os.system('xdg-open ~/Documents/doop/downloads/out/securibench6/database/output2.svg') 
    else:
        print("失败")

#cmd("java -version")
#cmd("exit 1")
cmd("cd ~/Documents/doop/downloads;./doop  -a micro  --input-file ~/Documents/doop/test34/securibench6.jar --platform java_8_mini  --id securibench6 --generate-jimple")
