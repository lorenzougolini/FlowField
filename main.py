import argparse
from tqdm import tqdm
from config import TOT_FRAMES
from simulation import Simulation
from renderer import Renderer
from video_recorder import VideoRecorder

def main():
    parser = argparse.ArgumentParser(description="Flow field simulation")
    
    parser.add_argument(
        "-r","--record",
        action="store_true",
        help="Record the simulation as video"
    )
    parser.add_argument(
        "-p", "--particles",
        action = "store_true",
        help="Number of particles"
    )
    parser.add_argument(
        "-d","--drawfield",
        action="store_true",
        help="Draw the flow field"
    )
    parser.add_argument(
        "-f","--filepath",
        type=str,
        default="output_file",
        help="File path to save the video"
    )
    parser.add_argument(
        "-n","--numofparticles",
        type=int,
        default=500,
        help="Number of particles"
    )

    args = parser.parse_args()
    RECORD = args.record
    PARTICLES = args.particles
    DRAWFIELD = args.drawfield
    FILEPATH = args.filepath
    NUMOFPARTICLES = args.numofparticles 

    simulation = Simulation(DRAWFIELD, PARTICLES, num_particles = NUMOFPARTICLES)
    renderer = Renderer(simulation, RECORD)
    video_recorder = VideoRecorder(FILEPATH) if RECORD else None
    
    if RECORD:
        pbar = tqdm(total=TOT_FRAMES, desc="Frames to record") if RECORD else None

    # with tqdm(total=TOT_FRAMES, desc="Frames to record") as pbar:
    while not renderer.exit_requested():

        renderer.render_flow()

        simulation.update()

        if video_recorder:
            video_recorder.record_frame(renderer.get_frame())
            pbar.update(1)
            if video_recorder.exit_requested(TOT_FRAMES): break

    if video_recorder:
        video_recorder.close()
    renderer.close()

if __name__ == "__main__": 
    main()