# HandbrakeScripter

Python code to create batch scripts to split and encode `*.avi` files using handbrake. Contains 2 methods which should be run in order.
Requires [Handbrake](http://handbrake.fr/) and Python, it is tested on 2.7.

## get_file_list(path)

Generates a list of `*.avi` files in the directory of interest in a comma delimited text file called `vid_params.txt`. This file has 
the format:

`filename,start:time,end:time`

Start and end times must be added manually in the mm:ss format before running the next method.

## make_commands(path,outpath,handbrakepath)

This generates a batch file which will contain a Handbrake command to split each video to the specified length and encode
it to `*.mp4`.

`handbrakepath` is the path to the directory where handbrake is installed.

Run the batch file normally in windows and the video files will be generated in the specified output directory.
