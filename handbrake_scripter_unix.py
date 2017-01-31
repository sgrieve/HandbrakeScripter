# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 21:28:03 2015

@author: Stuart Grieve
"""


def get_file_list(path):
    import os
    with open(path + 'vid_params.txt', 'w') as w:

        for f in os.listdir(path):
            if f.endswith('.avi'):
                w.write(path + f + ',,\n')


def seconds(time):
    seconds = int(time.split(':')[1])
    mins = int(time.split(':')[0])

    return (mins * 60) + seconds


def out_name_format(name):
    name = name.split('.')[0].title() + '.mp4'
    name = name.replace('_', ' ')

    if ' Sa ' in name:
        return name.replace(' Sa ', ' SA ')
    elif ' Pa ' in name:
        return name.replace(' Pa ', ' PA ')
    else:
        return name


def make_commands(path, outpath):
    filenames = []
    start = []
    end = []
    outnames = []
    with open(path + 'vid_params.txt', 'r') as f:
        for l in f.readlines():
            split = l.split(',')
            filenames.append(split[0])
            outnames.append(outpath + out_name_format(split[0].split('/')[-1]))
            start.append(str(seconds(split[1])))
            end.append(str(seconds(split[2]) - seconds(split[1])))

    with open(path + 'vid_commands.sh', 'w') as w:
        w.write('#!/bin/sh\n')
        for i in range(len(end)):
            w.write(('HandBrakeCLI -i \"{0}\" -o \"{3}\" -e x264 -q 22 -r 29.97 -B '
                     '64 -O --start-at duration:{1} --stop-at duration:{2}\n')
                    .format(filenames[i], start[i], end[i], outnames[i]))


#get_file_list('/media/sgrieve/Seagate Backup Plus Drive/new_pd/')
make_commands('/home/sgrieve/handbrake/vids/', '/home/sgrieve/handbrake/final/')
