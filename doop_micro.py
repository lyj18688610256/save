#! /usr/bin/python3 python3
import time
import subprocess
import os
import sys

str_ID='securibench3'
str='/home/lee/Documents/doop/downloads/out/{mstr_ID}/database'.format(mstr_ID=str_ID)

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",universal_newlines=True)
#    subp.wait(3600)   如果调用了该句,就不会实时打印出调试信息
    while True:
        nextline = subp.stdout.readline()
        if nextline == '' and subp.poll() is not None:  #subp.poll()为None时,表示进程正在运行
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()
    if subp.poll() == 0:
        sizeC = os.path.getsize('{mstr}/C.csv'.format(mstr=str))
        sizeB = os.path.getsize('{mstr}/B.csv'.format(mstr=str))
        if sizeC == 0:
            print('\n\n\n\n')
            print('--------')
            print('Taint Path是空的')
            print('\n\n\n\n')
       
        else:
            strC1='sed \'s/\]//g\' {mstr}/C.csv |sed \'s/\[//g\'|sed \'s/nil,//g\'|sed \'s/, </ -> </g\'|sed \'s/^/"/g\'|sed \'s/$/";/g\' |sed \'1i\strict digraph{{ \'|sed \'s/ -> /" -> "/g\' > {mstr}/C.dot'.format(mstr=str)
            strC2='echo \'}}\' >> {mstr}/C.dot'.format(mstr=str)
            strC3='dot -Tsvg {mstr}/C.dot -o {mstr}/outputC.svg'.format(mstr=str)
            strC4='xdg-open {mstr}/outputC.svg'.format(mstr=str)

            
            os.system(strC1)
            os.system(strC2)
            os.system(strC3)
            os.system(strC4) 

            print('\n\n\n\n')
            print('--------')
            print('Success')
            print('\n\n\n\n')

        if sizeB == 0:
            print('\n\n\n\n')
            print('--------')
            print('SmallVFlow Path是空的')
            print('\n\n\n\n')
        else:
            
            strB1='sed \'s/\]//g\' {mstr}/B.csv |sed \'s/\[//g\'|sed \'s/nil,//g\'|sed \'s/, </ -> </g\'|sed \'s/^/"/g\'|sed \'s/$/";/g\' |sed \'1i\strict digraph{{ \'|sed \'s/ -> /" -> "/g\' > {mstr}/B.dot'.format(mstr=str)
            strB2='echo \'}}\' >> {mstr}/B.dot'.format(mstr=str)
            strB3='dot -Tsvg {mstr}/B.dot -o {mstr}/outputB.svg'.format(mstr=str)
            strB4='xdg-open {mstr}/outputB.svg'.format(mstr=str)

            os.system(strB1)
            os.system(strB2)
            os.system(strB3)
            os.system(strB4) 

            print('\n\n\n\n')
            print('--------')
            print('Success')
            print('\n\n\n\n')
    else:
            print('\n\n\n\n')
            print('--------')
            print('Failed')
            print('\n\n\n\n')

str_doop='/home/lee/Documents/doop/downloads'
str_input='/home/lee/Documents/doop/test34/{mstr_ID}.jar'.format(mstr_ID=str_ID)
str_analysis='micro'  #tfa micro
str_cmd='cd {mstr_doop}; ./doop  -a {mstr_analysis}  --input-file {mstr_input} --platform java_8_mini  --id {mstr_ID} --generate-jimple'.format(mstr_doop=str_doop,mstr_input=str_input,mstr_ID=str_ID,mstr_analysis=str_analysis)
cmd(str_cmd)
