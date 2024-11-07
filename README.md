# FlowField

This is a flow field simulation written in python.
There are two options:
- display the flow field
- run the program and save it as an mp4 video

## Show the flow field
Run
```
pyhton main.py
```
options:
- `-p`, `--particlenumber`          Set the number of particles to be generated
- `-d`, `--drawflowfield`           Used to visualize also the generated vectors on the field

## Save as mp4 video
```
python main.py -r -f [path]
```
options:
- `-r`, `--record`         Record the simulation as video
- `-p`, `--particlenumber` Set the number of particles to be generated
- `-f`, `--filepath`       File path to save the video
- `-d`, `--drawfield`      Used to visualize also the generated vectors on the field

