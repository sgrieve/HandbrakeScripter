# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 21:28:03 2015

@author: Stuart Grieve
"""
def get_file_list(path):
    import os    
    with open(path+'vid_params.txt','w') as w:
    
        for f in os.listdir(path):
            if f.endswith('.avi'):
                w.write(path+f+',,\n')
    
def seconds(time):
    seconds = int(time.split(':')[1])
    mins = int(time.split(':')[0])
    
    return (mins*60)+seconds

def output_name_format(name):
    name = name.split('.')[0].title()+'.mp4'
    
    if ' Sa ' in name:
        return name.replace(' Sa ',' SA ')
    elif ' Pa ' in name:
        return name.replace(' Pa ',' PA ')
    else:
        return name
    
def make_commands(path,outpath,handbrakepath):
    filenames = []
    start = []
    end = []
    outnames = []
    with open(path+'vid_params.txt','r') as f:
        for l in f.readlines():
            split = l.split(',')
            filenames.append(split[0])
            outnames.append(outpath+output_name_format(split[0].split('\\')[-1]))
            start.append(str(seconds(split[1])))
            end.append(str(seconds(split[2]) - seconds(split[1])))
                
    with open(path+'vid_commands.bat','w') as w:
        w.write('@ECHO OFF\n')
        for i in range(len(end)):
            w.write('\"'+handbrakepath+'HandBrakeCLI.exe\" -i \"'+filenames[i]+'\" -t 1 --angle 1 --start-at duration:'+start[i]+' --stop-at duration:'+end[i]+' -o \"'+outnames[i]+'\"  -f mp4  -O  -w 720 -l 480 --crop 0:0:0:0 --modulus 2 -e x264 -q 20 --vfr -a 1 -E av_aac -6 dpl2 -R Auto -B 160 -D 0 --gain 0 --audio-fallback ac3 --encoder-preset=veryfast  --encoder-level=\"4.0\"  --encoder-profile=main\n')
    
#get_file_list('C:\\pd_vids\\to_split\\')        
make_commands('C:\\pd_vids\\to_split\\','C:\\pd_vids\\to_upload\\','C:\\Program Files\\Handbrake\\')

