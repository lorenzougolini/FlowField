import numpy as np
import cv2
from config import WIDTH, HEIGHT, FPS

class VideoRecorder():
    def __init__(self, filepath) -> None:
        self.filepath = f"videos/{filepath}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(self.filepath, fourcc, FPS, (WIDTH, HEIGHT))
        self.frames_recorded = 0

    def record_frame(self, frame):
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = frame_bgr.astype(np.uint8)
        self.video_writer.write(frame)
        self.frames_recorded += 1
    
    def exit_requested(self, frames_to_record: int):
        return self.frames_recorded >= frames_to_record
    
    def close(self):
        self.video_writer.release()