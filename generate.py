import ffmpeg
import sys
import random

video = sys.argv[1]
overlay = sys.argv[2]
length = sys.argv[3]

video_duration = ffmpeg.probe(video)
overlay_duration = ffmpeg.probe(overlay)
print(video_duration)

def randomSecondGen(duration):
    second = random.randint(0, duration)

    return second

"""if __name__ == "__main__":
    videoRandomSec = randomSecondGen(video_duration)-length
    overlayRandomSec = randomSecondGen(overlay_duration)-length

    edited_video = (
        ffmpeg
        .input(video)
        .trim(start=videoRandomSec, end=videoRandomSec+length)
        .output("edited-video.mp4")
        .run()
    )
    edited_overlay = (
        ffmpeg
        .input(overlay)
        .trim(start=overlayRandomSec, end=overlayRandomSec+length)
        .output("edited-overlay.mp4")
        .run()
    )   """   